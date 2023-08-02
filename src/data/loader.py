import pandas as pd
import nfl_data_py as nfl
import os, urllib

def load_data(year=2022) -> pd.DataFrame:
    pbp = nfl.import_pbp_data([year]) # pbp = pd.read_csv('./data/data_2022.csv', encoding='utf-8', engine='python')
    data = pbp[(pbp['pass'] == 1) | (pbp['rush'] == 1)]
    data = data.dropna(subset=['epa', 'posteam', 'defteam'])
    return data

def load_logos() -> pd.DataFrame:
    # Loading in the team logos
    if not os.path.exists("logos"):
        os.makedirs("logos")
    logos = nfl.import_team_desc()[['team_abbr', 'team_logo_espn']]
    logo_paths = []
    team_abbr = []

    for team in range(len(logos)):
        urllib.request.urlretrieve(logos['team_logo_espn'][team], f"logos/{logos['team_abbr'][team]}.tif")
        logo_paths.append(f"logos/{logos['team_abbr'][team]}.tif")
        team_abbr.append(logos['team_abbr'][team])

    data = {'team_abbr' : team_abbr, 'logo_path' : logo_paths}
    return pd.DataFrame(data)
