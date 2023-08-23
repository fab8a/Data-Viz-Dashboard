import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash

from src.components.layout import create_layout

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "NFL Stats Analyzer"
app.layout = create_layout(app)#, data)
app.run(port=8050)
