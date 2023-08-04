import pandas as pd
from dash import Dash, html, Input, Output
from . import epa_chart, season_dropdown, yac_chart, targets_slider
from . import ids

def create_layout(app: Dash, data:pd.DataFrame) -> html.Div:
    return html.Div(
        id=ids.APP_DIV,
        children=[
            html.H2(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[season_dropdown.render(app)]
            ),
            html.Div(
                className="chart-container",
                children=[epa_chart.render(app, data)]
            ),
            html.Hr(),
            html.Div(
                className="targets-slider-container",
                children=[targets_slider.render(app)]
            ),
            html.Div(
                className="chart-container",
                children=[yac_chart.render(app, data)]
            )
        ]
    )
