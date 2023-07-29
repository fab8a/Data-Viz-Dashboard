from dash import Dash, html, dcc
from . import ids

def render(app: Dash) -> html.Div:
    seasons = range(2015, 2023)
    return html.Div(
        children=[
            html.H5("Temporada deseada"),
            dcc.Dropdown(
                id=ids.SEASON_DROPDOWN,
                multi=False,
                value=2022,
                options=[{"label": season, "value":season} for season in seasons],
            )
        ]
    )