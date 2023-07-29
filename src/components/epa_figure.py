from dash import Dash, html, dcc
import plotly.express as px
from . import ids

IRIS = px.data.iris()  # iris is a pandas DataFrame

def render(app: Dash) -> html.Div:
    fig = px.scatter(IRIS, x="sepal_width", y="sepal_length")
    return html.Div(dcc.Graph(figure=fig), id=ids.EPA_FIGURE)