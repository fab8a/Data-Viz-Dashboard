from dash import Dash, html
from . import season_dropdown, epa_figure

def create_layout(app: Dash) -> html.Div:
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
                className="figure-one-container",
                #children=[epa_figure.render(app)]
            ),
            epa_figure.render(app)
        ]
    )