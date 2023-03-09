"""
THIS IS THE FILE FOR READYING DATA
"""
import pandas as pd
import random

random.seed(10)

def ready_data():
    data = pd.read_csv("cleaned_data.csv")
    dnp = ["Inactive", "Did Not Dress", "Did Not Play", "Suspended", "Not With Team", "Player Suspended"]

    player_id = {}
    team_id = {
                "ATL":1,
                "BOS": 2,
                "BRK": 3,
                "CHO": 4,
                "CHI": 5,
                "CLE": 6,
                "DAL": 7,
                "DEN": 8,
                "DET": 9,
                "GSW": 10,
                "HOU": 11,
                "IND": 12,
                "LAC": 13,
                "LAL": 14,
                "MEM": 15,
                "MIA": 16,
                "MIL": 17,
                "MIN": 18,
                "NOP": 19,
                "NYK": 20,
                "OKC": 21,
                "ORL": 22,
                "PHI": 23,
                "PHO": 24,
                "POR": 25,
                "SAC": 26,
                "SAS": 27,
                "TOR": 28,
                "UTA": 29,
                "WAS": 30
               }
    delete = []
    for index, row in data.iterrows():
        # ignore row where player did not play
        if str(row['Minutes Played']) in dnp:
            delete.append(index)
            continue

        # Convert player names to player IDs
        if row['Name'] == "":
            break
        elif row['Name'] not in player_id:
            player_id.update({row['Name']: random.randint(0, 100000)})
        data.at[index, 'Name'] = player_id[row['Name']]

        # Convert team names to team IDs
        data.at[index, 'Team'] = team_id[row['Team']]

        # Convert opponent names to team IDs
        # opponents are the same as team names, so we need to use the team_id dictionary and map to the opponent names
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
        if row['Position'] == "":
            break
        data.at[index, 'Position'] = position_num[row['Position']]

        # Convert Minutes played to total seconds
        if row['Minutes Played'] == "":
            break
        elif row['Minutes Played'] in dnp:
            pass
        else:
            data.at[index, 'Minutes Played'] = (int(data.at[index, 'Minutes Played'].split(':')[0]) * 60) + (int(data.at[index, 'Minutes Played'].split(':')[1]) * 60)

        # Convert Date to Month, Day, and Year
        if row['Date'] == "":
            break
        temp = data.at[index, 'Date'].split("/")
        data.at[index, 'Month'] = temp[0]
        data.at[index, 'Date'] = temp[1]
        data.at[index, 'Year'] = temp[2]

    # Delete rows where players haven't played
    data.drop(index=delete)
    # Return finalized data
    convert_dict = {
        'Name': int,
        'Position': int,
        'Month': int,
        'Date': int,
        'Year': int,
        'Team': int,
        'Location': int,
        'Opp': int,
        'Minutes Played': int,
        'FGM': float,
        'FGA': float,
        '3PM': float,
        '3PA': float,
        'FTM': float,
        'FTA': float,
        'ORB': float,
        'DRB': float,
        'TRB': float,
        'AST': float,
        'STL': float,
        'BLK': float,
        'TOV': float,
        'PTS': float
    }
    data = data.astype(convert_dict)
    return data
print(ready_data())