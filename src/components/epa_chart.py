import plotly.express as px
import pandas as pd
from PIL import Image
from dash import Dash, html, dcc, Input, Output
from . import ids
from ..data.loader import load_logos

def render(app: Dash, data: pd.DataFrame, year=2022) -> html.Div:
    # Filtering and getting usefull data
    # EPA = Expected Points Added == Puntos Esperados Anadidos -> Metrica de eexito que estima los puntos que un equipo deberia anotar conforme al contexto y/o situacion actual. 
    pass_epa = data[(data['pass'] == 1)].groupby('posteam')['epa'].mean().reset_index().rename(columns = {'epa' : 'pass_epa'})
    pass_epa.sort_values('pass_epa', ascending = False)
    # Combining passing plays EEPA + rushing plays EPA / Obtenemos el EPA total combinando el EPA de jugadas de pase + el de jugadas de corrida
    rush_epa = data[(data['rush'] == 1)].groupby('posteam')['epa'].mean().reset_index().rename(columns = {'epa' : 'rush_epa'})
    epa = pd.merge(pass_epa, rush_epa, on = 'posteam')

    logo_data = load_logos()
    epa_with_logos = pd.merge(epa, logo_data, left_on = 'posteam', right_on = 'team_abbr')

    x = epa_with_logos['pass_epa']
    y = epa_with_logos['rush_epa']
    paths = epa_with_logos['logo_path']

    fig = px.scatter(x=x, y=y, width=1100, height=600)

    # Add the logos as annotations
    for x0, y0, path in zip(x, y, paths):
        # https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html?highlight=add_layout_image#plotly.graph_objects.Figure.add_layout_image
        fig.add_layout_image( 
            dict(
                source=Image.open(path),
                xref='x',
                yref='y',
                x=x0,
                y=y0,
                sizex=0.06, # As fraction of total plot space  
                sizey=0.06,
                xanchor='center',
                yanchor='middle',
                opacity=0.85,
                layer='above'
            )
        )
    fig.update_layout(
        title=f"Rush and Pass EPA, {year} season",
        xaxis_title="EPA/Pass",
        yaxis_title="EPA/Rush"
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    return html.Div(dcc.Graph(figure=fig), id=ids.EPA_CHART)