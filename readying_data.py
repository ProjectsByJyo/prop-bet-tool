"""
THIS IS THE FILE FOR READYING DATA
"""
import pandas as pd
import random

random.seed(10)
data = pd.read_csv("cleaned_data.csv")


def ready_data():
    # Convert player names to player IDs
    player_id = {}

    for index, row in data.iterrows():
        if row['Name'] == "":
            break
        elif row['Name'] not in player_id:
            player_id.update({row['Name']: random.randint(0, 100000)})
        data.at[index, 'Name'] = player_id[row['Name']]

    # Convert team names to team IDs
    team_id = {}

    for index, row in data.iterrows():
        if row['Team'] == "":
            break
        elif row['Team'] not in team_id:
            team_id.update({row['Team']: random.randint(0, 20000)})
        data.at[index, 'Team'] = team_id[row['Team']]

    # Convert opponent names to team IDs
    # opponents are the same as team names, so we need to use the team_id dictionary and map to the opponent names
    for index, row in data.iterrows():
        if row['Opp'] == "":
            break
        data.at[index, 'Opp'] = team_id[row['Opp']]

    # Convert Position to respective number
    # (PG:1, SG:2, SF:3, PF:4, C:5)
    position_num = {
                    'PG': 1,
                    'SG': 2,
                    'SF': 3,
                    'PF': 4,
                    'C': 5
                            }
    for index, row in data.iterrows():
        if row['Position'] == "":
            break
        data.at[index, 'Position'] = position_num[row['Position']]

    # Return finalized data
    return data
print(ready_data())