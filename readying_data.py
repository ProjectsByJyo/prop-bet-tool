"""
THIS IS THE FILE FOR READYING DATA
"""
import random

random.seed(10)


def ready_data(variables):
    for index, row in variables.data.iterrows():
        # ignore row where player did not play
        if str(row['Minutes Played']) in variables.dnp:
            variables.delete.append(index)
            continue

        variables = alter_row(variables=variables, index=index, row=row)

    # Delete rows where players haven't played
    variables.data.drop(index=variables.delete)
    # Make sure the data types are numerical for easier machine learning
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
    variables.data = variables.data.astype(convert_dict)

    # Return finalized data and also update reverse map variables while we are at it
    # reverse_map will return original variables
    return reverse_map(variables)


def reverse_map(variables):
    # reverse mapping ids
    variables.id_team = {value: key for key, value in variables.team_id.items()}
    variables.id_player = {value: key for key, value in variables.player_id.items()}

    # return reverse mapped
    return variables


def alter_row(variables, index, row):
    # Convert player names to player IDs
    if row['Name'] not in variables.player_id:
        variables.player_id.update({row['Name']: random.randint(0, 100000)})
    variables.data.at[index, 'Name'] = variables.player_id[row['Name']]

    # Convert team names to team IDs
    variables.data.at[index, 'Team'] = variables.team_id[row['Team']]

    # Convert opponent names to team IDs
    # opponents are the same as team names, so we need to use the team_id dictionary and map to the opponent names
    variables.data.at[index, 'Opp'] = variables.team_id[row['Opp']]

    # Convert Position to respective number
    # (PG:1, SG:2, SF:3, PF:4, C:5)
    variables.data.at[index, 'Position'] = variables.position_num[row['Position']]

    # Convert Minutes played to total seconds
    variables.data.at[index, 'Minutes Played'] = (int(variables.data.at[index, 'Minutes Played'].split(':')[0]) * 60) + (int(variables.data.at[index, 'Minutes Played'].split(':')[1]) * 60)

    # Convert Date to Month, Day, and Year
    temp = variables.data.at[index, 'Date'].split("/")
    variables.data.at[index, 'Month'] = temp[0]
    variables.data.at[index, 'Date'] = temp[1]
    variables.data.at[index, 'Year'] = temp[2]

    return variables
