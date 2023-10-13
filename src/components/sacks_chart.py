import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss
from sklearn.model_selection import StratifiedShuffleSplit
from xgboost import XGBClassifier
from dash import Dash, html, dcc, Input, Output
from . import ids
from ..data.loader import load_logos


def render(app: Dash, data: pd.DataFrame, year=2022) -> html.Div:
    data = data[(data['pass'] == 1) & (data['play_type'] != "no_play")]
    data['obvious_pass'] = np.where((data['down'] == 3) & (data['ydstogo'] >= 6), 1,0)   
    
    pre_df = data[['game_id', 'play_id', 'season', 'name', 'down', 'ydstogo', 'yardline_100', 'game_seconds_remaining', 'defenders_in_box', 'number_of_pass_rushers', 'xpass', 'obvious_pass', 'sack']]
    df = pre_df.dropna()
    df.isna().sum()

    df['down'] = df['down'].astype('category')
    df_no_ids = df.drop(columns = ['game_id', 'play_id', 'name', 'season'])
    df_no_ids = pd.get_dummies(df_no_ids, columns = ['down'])
    
    sss = StratifiedShuffleSplit(n_splits=1, test_size=0.25)
    for train_index, test_index in sss.split(df_no_ids, df_no_ids['sack']):
        strat_train_set = df_no_ids.iloc[train_index]
        strat_test_set = df_no_ids.iloc[test_index]

    X_train = strat_train_set.drop(columns = ['sack'])
    Y_train = strat_train_set['sack']
    X_test = strat_test_set.drop(columns = ['sack'])
    Y_test = strat_test_set['sack']
    
    XGB = XGBClassifier(objective="binary:logistic")
    XGB.fit(X_train, Y_train) 
    
    make_sacks_preds = df_no_ids.drop('sack', axis = 1)
    XGB_total_predictions = pd.DataFrame(XGB.predict_proba(make_sacks_preds), columns = ['no_sack', 'sack_pred'])[['sack_pred']]

    sacks_preds = df.reset_index().drop(columns = ['index'])
    sacks_preds['sack_pred'] = XGB_total_predictions
    # Sacks OE -> sacks over expected / sacks sobre los estimados 
    sacks_preds['sacks_oe'] = sacks_preds['sack'] - sacks_preds['sack_pred']
    sacks_preds = sacks_preds[(sacks_preds['season'] == year)].groupby('name').agg({'sack': 'sum', 'sack_pred': 'sum', 'sacks_oe': 'sum'}).reset_index().sort_values('sacks_oe', ascending = True)
    sacks_preds = sacks_preds[sacks_preds['sack_pred'] >= 15]

    sacks = sacks_preds['sack']
    
    fig = px.scatter(sacks_preds, y=sacks, x='sack_pred', text='name', width=1100, height=650, color='name', title=f'Actual vs. Predicted Sacks per QB, {year} season')
    fig.add_shape(type='line', x0=sacks.min(), y0=sacks.min(),
                x1=sacks.max(), y1=sacks.max(),
                line=dict(color='red', width=2, dash='dash'))
    fig.update_layout(
        xaxis_title="Predicted Sacks",
        yaxis_title="Actual Sacks",
        hovermode="closest",
        showlegend=False
    )
    fig.update_traces(textposition='top center')


    return html.Div(dcc.Graph(figure=fig), id=ids.SACKS_CHART)