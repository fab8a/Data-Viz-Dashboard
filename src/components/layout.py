import pandas as pd
from dash import Dash, html, Input, Output
from . import epa_chart, season_dropdown, yac_chart, sacks_chart, targets_slider, ids
from src.data.loader import load_data

def create_layout(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.APP_DIV, 'children'),
        Input(ids.SEASON_DROPDOWN, 'value'),
    )

    def update_graph(year) -> html.Div:
        data = load_data(year)
        return html.Div(
            id=ids.APP_DIV,
            className='app-div',
            children=[
                html.Div(
                    children=[
                        html.H2(app.title, className="banner-text"),
                        html.Img(src=app.get_asset_url('banner.png'), style={'width':'100%'})], #className='banner-image')],
                    className='title-div'),
                html.Div(
                    children=[
                        html.Div(
                            className="dropdown-container",
                            children=[season_dropdown.render(app, year)]
                        ),
                        html.Div(
                            className="chart-container",
                            children=[epa_chart.render(app, data, year)]
                        ),
                        html.Hr(),
                        html.Div(
                            className="targets-slider-container",
                            children=[targets_slider.render(app)]
                        ),
                        html.Div(
                            className="chart-container",
                            children=[yac_chart.render(app, data, year),
                                      sacks_chart.render(app, data, year)]
                    )],
                    className="body-div"
                )
            ]
        )
    data = load_data()
    return html.Div(
        id=ids.APP_DIV,
        className='app-div',
        children=[
            html.Div(
                html.H2(app.title),
                className='title-div'),
                html.Img(src=r'assets/banner.jpg', alt='app banner'),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[season_dropdown.render(app)]
            ),
            html.Div(
                className="chart-container",
                children=[epa_chart.render(app, data)]
            ),
            html.Hr(),  
            html.Div(
                className="chart-container",
                children=[yac_chart.render(app, data),
                          sacks_chart.render(app, data)]
                ),
            html.Div(
                className="targets-slider-container",
                children=[targets_slider.render(app)]
            )],         
    )
