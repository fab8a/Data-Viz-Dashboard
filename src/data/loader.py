import pandas as pd
import nfl_data_py as nfl

def load_data(year=2022) -> pd.DataFrame:
    pbp = nfl.import_pbp_data([year]) # pbp = pd.read_csv('./data/data_2022.csv', encoding='utf-8', engine='python')
    data = pbp[(pbp['pass'] == 1) | (pbp['rush'] == 1)]
    data = data.dropna(subset=['epa', 'posteam', 'defteam'])
    return data