from flask import Flask, render_template
from flask_restful import Api

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.models import *

import simulations

app = Flask(__name__)
api = Api(app)

@app.route("/")
def simulate():
    base_case_simulation_x, base_case_simulation_y = simulations.base_case()
    pred_case_simulation_x, pred_case_simulation_y = simulations.pred_case()

    base_TOOLS = [BoxZoomTool(), PanTool(), ResetTool(), WheelZoomTool(), BoxSelectTool(), HoverTool(tooltips=[
            ("Revenue ($)", "@y{1.11}")
        ])]
    pred_TOOLS = [BoxZoomTool(), PanTool(), ResetTool(), WheelZoomTool(), BoxSelectTool(), HoverTool(tooltips=[
            ("Revenue ($)", "@y{1.11}")
        ])]

    base_fig = figure(title="Base Case: Cumulative Revenue($)", x_axis_type="datetime", tools=base_TOOLS, plot_width=600, plot_height=300, sizing_mode="scale_width")
    base_fig.line(base_case_simulation_x, base_case_simulation_y, color="#2ecc71", line_width=2)
    base_fig.yaxis[0].formatter.use_scientific = False

    pred_fig = figure(title="10% Coupon Case: Cumulative Revenue($)", x_axis_type="datetime", tools=pred_TOOLS, plot_width=600, plot_height=300, sizing_mode="scale_width")
    pred_fig.line(pred_case_simulation_x, pred_case_simulation_y, color="#9b59b6", line_width=2)
    pred_fig.yaxis[0].formatter.use_scientific = False

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    base_script, base_div = components(base_fig)
    pred_script, pred_div = components(pred_fig)
    html = render_template(
        'index.html',
        base_plot_script=base_script,
        base_plot_div=base_div,
        base_cum_revenue = sum(base_case_simulation_y),
        pred_plot_script=pred_script,
        pred_plot_div=pred_div,
        pred_cum_revenue = sum(pred_case_simulation_y),
        js_resources=js_resources,
        css_resources=css_resources
    )
    return encode_utf8(html)

if __name__ == "__main__":
    app.run(debug=True)
