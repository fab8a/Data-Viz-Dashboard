from dash import Dash, html
import dash_bootstrap_components as dbc
from . import epa_chart, season_dropdown, yac_chart, targets_slider
import pandas as pd

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
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