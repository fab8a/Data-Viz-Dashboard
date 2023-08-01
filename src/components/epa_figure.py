import os, urllib, PIL
import plotly.express as px
import pandas as pd
import nfl_data_py as nfl
from dash import Dash, html, dcc, Input, Output
from . import ids
from ..data.loader import load_data

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.EPA_CHART, 'children'),
        Input(ids.SEASON_DROPDOWN, 'value')
    )

    def update_graph(year) -> html.Div:
        data = load_data(year)
        # Filtering and getting usefull data
        # EPA = Expected Points Added == Puntos Esperados Anadidos -> Metrica de eexito que estima los puntos que un equipo deberia anotar conforme al contexto y/o situacion actual. 
        pass_epa = data[(data['pass'] == 1)].groupby('posteam')['epa'].mean().reset_index().rename(columns = {'epa' : 'pass_epa'})
        pass_epa.sort_values('pass_epa', ascending = False)
        # Combining passing plays EEPA + rushing plays EPA / Obtenemos el EPA total combinando el EPA de jugadas de pase + el de jugadas de corrida
        rush_epa = data[(data['rush'] == 1)].groupby('posteam')['epa'].mean().reset_index().rename(columns = {'epa' : 'rush_epa'})
        epa = pd.merge(pass_epa, rush_epa, on = 'posteam')

        # Loading in the team logos
        logos = nfl.import_team_desc()[['team_abbr', 'team_logo_espn']]
        logo_paths = []
        team_abbr = []
        if not os.path.exists("logos"):
            os.makedirs("logos")

        for team in range(len(logos)):
            urllib.request.urlretrieve(logos['team_logo_espn'][team], f"logos/{logos['team_abbr'][team]}.tif")
            logo_paths.append(f"logos/{logos['team_abbr'][team]}.tif")
            team_abbr.append(logos['team_abbr'][team])

        data = {'team_abbr' : team_abbr, 'logo_path' : logo_paths}
        logo_data = pd.DataFrame(data)
        epa_with_logos = pd.merge(epa, logo_data, left_on = 'posteam', right_on = 'team_abbr')

        x = epa_with_logos['pass_epa']
        y = epa_with_logos['rush_epa']
        paths = epa_with_logos['logo_path']

        fig = px.scatter(x=x, y=y, width=1200, height=650)

        # Add the logos as annotations
        for x0, y0, path in zip(x, y, paths):
            # https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html?highlight=add_layout_image#plotly.graph_objects.Figure.add_layout_image
            fig.add_layout_image( 
                dict(
                    source=PIL.Image.open(path),
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
        # Update the layout with axis limits, title, and axis labels
        fig.update_layout(
            title=f"Rush and Pass EPA, {year} season",
            xaxis=dict(range=[-0.2, 0.3]),
            yaxis=dict(range=[-0.25, 0.15]),
            xaxis_title="EPA/Pass",
            yaxis_title="EPA/Rush"
        )
        
        return html.Div(dcc.Graph(figure=fig), id=ids.EPA_CHART, style={
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
        },)
    return html.Div(id=ids.EPA_CHART)