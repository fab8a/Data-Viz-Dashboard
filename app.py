import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash

from src.components.layout import create_layout

def main() -> None:
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "NFL Stats Analyzer"
    app.layout = create_layout(app)#, data)
    server = app.server()
    app.run(debug=True)

if __name__ == '__main__':
    main()  
