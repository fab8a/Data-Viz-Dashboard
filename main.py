import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash
import nfl_data_py as nfl

from src.components.layout import create_layout
# from src.data.loader import load_data

def main() -> None:
    # data = load_data()
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "NFL Stats Analyzer"
    app.layout = create_layout(app)#, data)
    app.run(port=8051, debug=True)

if __name__ == '__main__':
    main()      