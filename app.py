import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash
import nfl_data_py as nfl

from src.components.layout import create_layout
from src.data.loader import load_data
from src.components import ids

seasons = ids.SEASONS
data = load_data(seasons)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.title = "NFL Stats Analyzer"
app.layout = create_layout(app, data)


if __name__ == '__main__':
    app.run(debug=True)