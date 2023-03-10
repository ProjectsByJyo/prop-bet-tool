import pandas as pd


class setup:
    data = pd.DataFrame()
    delete = []
    player_id = {}
    team_id = {}
    id_team = {}
    id_player = {}
    dnp = []
    position_num = {}
    location = {}
    def __init__(self):
        self.data = pd.read_csv("cleaned_data.csv")
        self.team_id = {
            "ATL": 1, "BOS": 2, "BRK": 3, "CHO": 4, "CHI": 5,
            "CLE": 6, "DAL": 7, "DEN": 8, "DET": 9, "GSW": 10,
            "HOU": 11, "IND": 12, "LAC": 13, "LAL": 14, "MEM": 15,
            "MIA": 16, "MIL": 17, "MIN": 18, "NOP": 19, "NYK": 20,
            "OKC": 21, "ORL": 22, "PHI": 23, "PHO": 24, "POR": 25,
            "SAC": 26, "SAS": 27, "TOR": 28, "UTA": 29, "WAS": 30
        }
        self.dnp = [
            "Inactive",
            "Did Not Dress",
            "Did Not Play",
            "Suspended",
            "Not With Team",
            "Player Suspended"
        ]
        self.position_num = {
            'PG': 1,
            'SG': 2,
            'SF': 3,
            'PF': 4,
            'C': 5
        }
        self.location = {0:'Home', 1:'Away'}
