import dash_bootstrap_components as dbc
from dash import Dash
from src.components.layout import create_layout
from src.data.loader import load_data

def main():
    data = load_data()
    app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "NFL Stats Analyzer"
    app.layout = create_layout(app, data)#dbc.Container([mytext, myinput])
    app.run(port=8051, debug=True)

if __name__ == '__main__':
    main()