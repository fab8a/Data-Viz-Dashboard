import pandas as pd
from dash import Dash, html, dcc
from . import ids

def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.H6("Minimum amount of targets"),
            dcc.Slider(0, 180, 20,
                        value=100,
                        id='targets_slider'
                ),
        ]
    )