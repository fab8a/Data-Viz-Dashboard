from dash import Dash, html, Input, Output
from . import epa_chart, season_dropdown, yac_chart, targets_slider
from . import ids
from ..data.loader import load_data

def create_layout(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.APP_DIV, 'children'),
        Input(ids.SEASON_DROPDOWN, 'value')
    )

    def update_graph(year) -> html.Div:
        data = load_data(year)
        return html.Div(id=ids.APP_DIV, children=[
            html.H2(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[season_dropdown.render(app, year)]
            ),
            html.Div(
                className="chart-container",
                children=[epa_chart.render(app, data)]
            ),
            html.Div(
                className="targets-slider-container",
                children=[targets_slider.render(app)]
            ),
            html.Div(
                className="chart-container",
                children=[yac_chart.render(app, data)]
            )
        ])

    data = load_data()
    return html.Div(
        id=ids.APP_DIV,
        children=[
            html.H2(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[season_dropdown.render(app)]
            ),
            html.Div(
                className="chart-container",
                children=[epa_chart.render(app, data)]
            ),
            html.Div(
                className="targets-slider-container",
                children=[targets_slider.render(app)]
            ),
            html.Div(
                className="chart-container",
                children=[yac_chart.render(app, data)]
            )
        ]
    )
