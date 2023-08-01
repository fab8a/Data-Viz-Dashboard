import pandas as pd
from dash import Dash, html, dcc, Input, Output
from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:

    @app.callback(
            Output('season-container', 'children'),
            Input(ids.SEASON_DROPDOWN, 'value')
    )

    def update_season(value):
        return f"Season selected: {value}"
    

    seasons = range(2015, 2023)
    return html.Div(
        children=[
            html.H5("Temporada deseada"),
            dcc.Dropdown(
                id=ids.SEASON_DROPDOWN,
                multi=False,
                value=2022,
                options=[{"label": season, "value":season} for season in seasons],
            ),
            html.Div(id='season-container')
        ]
    )