from dash import Dash, html
import dash_bootstrap_components as dbc
from . import season_dropdown, epa_figure
import pandas as pd

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H2(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[season_dropdown.render(app, data)]
            ),
            html.Div(
                className="figure-one-container",
                children=[epa_figure.render(app, data)]
            ),
        ]
    )