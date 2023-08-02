import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, Input, Output
from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.YAC_CHART, 'children'),
        Input(ids.TARGETS_SLIDER, 'value')
    )

    def update_graph(min_targets) -> html.Div:
        receiver_yac = data[(data['pass'] == 1)].groupby('receiver_player_name').agg({'pass': 'count','yards_after_catch': 'sum', 'posteam':'min'}).reset_index().rename(columns = {'pass' : 'targets', 'yards_after_catch' : 'yac', 'posteam':'team'})
        receiver_yac = receiver_yac[(receiver_yac['targets'] >= min_targets)]

        name = receiver_yac['receiver_player_name']
        team = receiver_yac['team']

        fig = px.scatter(receiver_yac, x='yac', y='targets', text=name, width=1200, height=650, color=team)
        fig.update_traces(textposition='top center')

        return html.Div(dcc.Graph(figure=fig), id=ids.YAC_CHART)
    return html.Div(id=ids.YAC_CHART)