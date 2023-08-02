from dash import Dash, html, dcc
from . import ids

def render(app: Dash, year=(2022)) -> html.Div:
    seasons = range(2013, 2023)
    return html.Div(
        children=[
            html.H5("Temporada deseada"),
            dcc.Dropdown(
                id=ids.SEASON_DROPDOWN,
                multi=False,
                value=year,
                options=[{"label": season, "value":season} for season in seasons],
            ),
        ]
    )