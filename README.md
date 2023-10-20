# Data-Viz-Dashboard
NFL players statistics dashboard for DevF's Data Visualization module

## Expected Points Added per team comparision
- Combination of offensive EPA from rushing plus passing plays for each team.
- Visual representation of each team cummulative's EPA using their corresponding logos.
- Selector of the last 10 seasons to analyze evolution of offenses throught the years. 

## Yards after the catch leaders 
- Total YAC acummuladed (sum) for the entire season per top performing players.
- Minimum amount of targets sliding filter.
- Charted said total amount vs the total targets received by each ball catcher.

## Expected vs actual sacks per QB
- Comparison chart of situationally probabilistic sacks against plays resulting in actual sacks.
- Feature engineered 'obvious pass' situation, utilizing 'down' and 'yards to go'.
- Created a model with 'sack' as target variable and using relevant features for sack plays as the independent variables.
- Used the 'XGBClassifier', which is a gradient boosting algorithn machine learning algorithm to train the model. 
- Did EDA to both determine the relevancy of the 'features' as well as to choose the ML algorithm.
- Made predictions that based on the league's average sack, how many of such situations each QB faced during the entire season


![](https://github.com/fab8a/Data-Viz-Dashboard/blob/main/assets/sample.gif)
---

# Extras
### [Data wrangling Colab](https://colab.research.google.com/drive/1Fi001xmwjThMcLuw4FgTefySJMSjFurU?usp=sharing)

- Used ['nfl_data_py'](https://pypi.org/project/nfl-data-py/) which uses ['nflverse-pbp'](https://github.com/nflverse/nflverse-pbp) to retreive the play by play data for all games from an NFL season.
- Used ['dash'](https://dash.plotly.com/) and ['plotly.express'](https://plotly.com/python-api-reference/index.html) to build a basic dashboard for visualization.
