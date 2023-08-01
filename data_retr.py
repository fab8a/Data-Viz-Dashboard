import nfl_data_py as nfl
import time
import pandas as pd

def extract_data_to_csv():
    for year in range(2015,2023):    
        start_time = time.time()
        pbp = nfl.import_pbp_data([year])

    #### Cleaning the Datase
        pbp_rp = pbp[(pbp['pass'] == 1) | (pbp['rush'] == 1)]
        pbp_rp = pbp_rp.dropna(subset=['epa', 'posteam', 'defteam'])

        pbp_rp.to_csv(f'./data/data_{year}.csv', index=False)
        elapsed_time = time.time() - start_time
        print(f"Lap execution time: {elapsed_time:.6f} seconds")


start_time_total = time.time()
# extract_data_to_csv()
df = pd.read_csv('./data/data_2022.csv')
elapsed_time = time.time() - start_time_total
print(f"Execution time: {elapsed_time:.6f} seconds")

