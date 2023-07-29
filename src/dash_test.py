from dash import Dash, dcc, Output, Input, html
import dash_bootstrap_components as dbc
from components.layout import create_layout

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
mytext = dcc.Markdown(children='')  
myinput = dcc.Input(value='# Hello World')

# Layout
app.title = "NFL Stats Analyzer"
app.layout = create_layout(app)#dbc.Container([mytext, myinput])

# Callbacks
@app.callback( 
    Output(mytext, component_property='children'),
    Input(myinput, component_property='value')
)

def update_tittle(user_input):
    return user_input


if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
