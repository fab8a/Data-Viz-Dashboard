from dash import Dash, html, dcc
from . import ids

def render(app: Dash, year=(2022)) -> html.Div:
    seasons = ids.SEASONS
    return html.Div(
        children=[
            html.H5("Season selected"),
            dcc.Dropdown(
                id=ids.SEASON_DROPDOWN,
                multi=False,
                value=year,
                options=[{"label": season, "value":season} for season in seasons],
            ),
        ]
    )