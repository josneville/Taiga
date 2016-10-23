from __future__ import division

from flask import Flask, render_template, request
from flask_restful import Api

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.models import *

import json
import numpy as np

import simulations

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    acceptance_period = 2
    baseline = 0.9
    coupon_rate_max = 0.3

    html = render_template(
        'index.html',
        options={'acceptance_period': acceptance_period, 'baseline': baseline, 'coupon_rate_max': coupon_rate_max},
        simulation = False
    )
    return encode_utf8(html)

@app.route("/simulate")
def simulate():
    args = request.args

    acceptance_period = int(args['acceptance_period']) if 'acceptance_period' in args else 2
    baseline = float(args['baseline']) if 'baseline' in args else 0.9
    coupon_rate_max = float(args['coupon_rate_max']) if 'coupon_rate_max' in args else 0.3

    colors = ['#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#f1c40f', '#e67e22', '#e74c3c', '#95a5a6']

    base_cases = []
    for _ in range(0, 50):
        options = {'num_years': 5}
        base_case_simulation_x, base_case_simulation_y = simulations.base_case(options)
        base_cases.append(base_case_simulation_y)
    base_case_avg = np.array([0] * len(base_cases[0]))
    for base_case in base_cases:
        base_case_avg = base_case_avg + np.array(base_case)
    base_case_avg = base_case_avg / len(base_cases)
    base_case_cum_rev = base_case_avg[-1]

    revenue_by_acceptance_rate = {}

    for acceptance_rate in np.arange(.1,0.8,0.1):

        best_pred_case_cum_rev = 0
        best_coupon = 0
        best_pred_case_avg = []
        best_pred_case_avg_dates = []

        for coupon_rate in np.linspace(0.20, coupon_rate_max * (1.7), 20):

            coupon_rate = coupon_rate * (1 - acceptance_rate) # Increase coupon as acceptance rate increases, as that is true in the universe

            pred_cases = []
            pred_cases_dates = []
            for _ in range(0, 50):
                options = {'num_years': 5}
                options['coupon_rate'] = coupon_rate
                options['acceptance_rate'] = acceptance_rate
                options['acceptance_period'] = acceptance_period
                options['baseline'] = baseline
                pred_case_simulation_x, pred_case_simulation_y = simulations.pred_case(options)
                pred_cases_dates.append(pred_case_simulation_x)
                pred_cases.append(pred_case_simulation_y)

            smallest_length = 10000000
            for idx, pred_case in enumerate(pred_cases):
                if len(pred_case) < smallest_length:
                    smallest_length = len(pred_case)

            pred_case_avg = [0] * smallest_length
            pred_case_avg_dates = [None] * smallest_length
            for idx, value in enumerate(pred_case_avg):
                counter = 0
                for pred_case_idx, pred_case in enumerate(pred_cases):
                    if len(pred_case) > idx:
                        counter = counter + 1
                        pred_case_avg[idx] += pred_case[idx]
                pred_case_avg_dates[idx] = pred_cases_dates[counter - 1]
                pred_case_avg[idx] = int(pred_case_avg[idx] / counter)

            pred_case_cum_rev = pred_case_avg[-1]

            if pred_case_cum_rev > best_pred_case_cum_rev:
                best_pred_case_cum_rev = pred_case_cum_rev
                best_coupon = coupon_rate
                best_pred_case_avg = pred_case_avg
                best_pred_case_avg_dates = pred_case_avg_dates

        revenue_by_acceptance_rate[str(round(acceptance_rate * 100))] = {}
        revenue_by_acceptance_rate[str(round(acceptance_rate * 100))]['coupon_rate'] = best_coupon
        revenue_by_acceptance_rate[str(round(acceptance_rate * 100))]['revenue'] = best_pred_case_cum_rev
        revenue_by_acceptance_rate[str(round(acceptance_rate * 100))]['best_simulation'] = best_pred_case_avg
        revenue_by_acceptance_rate[str(round(acceptance_rate * 100))]['best_simulation_dates'] = best_pred_case_avg_dates

    TOOLS = [BoxZoomTool(), PanTool(), ResetTool(), WheelZoomTool(), BoxSelectTool(), HoverTool(tooltips=[
            ("Revenue ($)", "@y{1.11}")
        ])]

    fig = figure(title="Cumulative Revenue($)", x_axis_type="datetime", tools=TOOLS, plot_width=700, plot_height=400)
    fig.line(base_case_simulation_x, base_case_avg, color=colors[-1], line_width=4, legend="Base Case")
    for idx, j in enumerate(sorted(revenue_by_acceptance_rate.keys())):
        fig.line(revenue_by_acceptance_rate[j]['best_simulation_dates'][0], revenue_by_acceptance_rate[j]['best_simulation'], color=colors[idx], line_width=4, legend="Pred Case: Acceptance Rate (" + j + "%)")
        del revenue_by_acceptance_rate[j]['best_simulation_dates']
        del revenue_by_acceptance_rate[j]['best_simulation']

    fig.yaxis[0].formatter.use_scientific = False
    fig.legend.location = "top_left"
    fig.title.text_color = "white"
    fig.xaxis.major_label_text_color = "white"
    fig.yaxis.major_label_text_color = "white"
    fig.xaxis.axis_line_color = "white"
    fig.yaxis.axis_line_color = "white"
    fig.background_fill_color = None
    fig.border_fill_color = None

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(fig)
    html = render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
        options={'acceptance_period': acceptance_period, 'baseline': baseline, 'coupon_rate_max': coupon_rate_max},
        simulation = True,
        revenue_by_acceptance_rate = revenue_by_acceptance_rate,
        base_case_cum_rev = base_case_cum_rev
    )
    return encode_utf8(html)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
