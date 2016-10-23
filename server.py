from flask import Flask, render_template, request
from flask_restful import Api

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.models import *

import json

import simulations

app = Flask(__name__)
api = Api(app)

@app.route("/")
def simulate():
    args = request.args

    options = {}
    options['coupon_rate'] = float(args['coupon_rate']) if 'coupon_rate' in args else 0.1
    options['num_years'] = int(args['num_years']) if 'num_years' in args else 1
    options['acceptance_rate'] = float(args['acceptance_rate']) if 'acceptance_rate' in args else 0.60
    options['acceptance_period'] = int(args['acceptance_period']) if 'acceptance_period' in args else 3
    options['baseline'] = float(args['baseline']) if 'baseline' in args else 0.80


    base_case_simulation_x, base_case_simulation_y = simulations.base_case(options)
    pred_case_simulation_x, pred_case_simulation_y = pred_case_simulation_x, pred_case_simulation_y = simulations.pred_case(options)

    TOOLS = [BoxZoomTool(), PanTool(), ResetTool(), WheelZoomTool(), BoxSelectTool(), HoverTool(tooltips=[
            ("Revenue ($)", "@y{1.11}")
        ])]

    fig = figure(title="Cumulative Revenue($)", x_axis_type="datetime", tools=TOOLS, plot_width=600, plot_height=300, sizing_mode="scale_width")
    fig.line(base_case_simulation_x, base_case_simulation_y, color="#2ecc71", line_width=2, legend="Base Case")
    fig.line(pred_case_simulation_x, pred_case_simulation_y, color="#9b59b6", line_width=2, legend="Prediction Case")
    fig.yaxis[0].formatter.use_scientific = False

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(fig)
    html = render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
        options=options,
        revenues=json.dumps({'base': base_case_simulation_y[-1], 'pred': pred_case_simulation_y[-1]})
    )
    return encode_utf8(html)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
