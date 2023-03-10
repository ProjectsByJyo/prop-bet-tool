from tool import setup
from learning import rf
from readying_data import ready_data
from pathlib import Path
import pickle

def run():
    # first we need to set up the variables we are going to be working with in this code which all live in tool.py
    variables = setup()
    variables = ready_data(variables)

    info = [[]]
    info[0].append(variables.player_id[str(input("What's the player's name?\n->"))])
    info[0].append(variables.position_num[str(input("What's the player's position?\n->"))])
    date = str(input("What's the date of the game?\n *input in MM/DD/YYYY format*\n->"))
    temp = date.split("/")
    info[0].append(temp[2])
    info[0].append(temp[1])
    info[0].append(temp[0])
    info[0].append(variables.team_id[str(input("What's the player's team?\n->"))])
    info[0].append(int(input("What's the location of the game?\n *Home:0, Away:1*\n->")))
    info[0].append(variables.team_id[str(input("Who's the player's opponent?\n->"))])

    path = Path('./rf_model.sav')
    if path.is_file():
        rf_model = pickle.load(open('rf_model.sav', 'rb'))
        predictions = rf_model.predict(info)[0]
    else:
        predictions = rf(variables, info)[0]
    formatted_prediction = f"Points: {predictions[14]:.1f}\n Rebounds: {predictions[9]:.1f}\n Assists: {predictions[10]:.1f}\n Points+Rebounds+Assists: {predictions[14] + predictions[9] + predictions[10]:.1f}\n Steals: {predictions[11]:.1f}\n Blocks: {predictions[12]:.1f}\n Turnovers: {predictions[13]:.1f}"
    print(
        f"Your Predictions for {variables.id_player[info[0][0]]} against {variables.id_team[info[0][7]]} at {variables.location[info[0][6]]} on {date} are:\n {formatted_prediction}")

run()
