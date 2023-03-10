# NBA Betting Tool
*This project is intended for users **(primarily me)** to make better decisions when betting money on NBA props.*

*(Raw NBA data from @basketball-reference.com to be used purely for research/educational purposes on how historical data can influence future outcomes. **ONLY**)*

### Data Collection
1. Manually collected raw data from @basket-reference.com and saved into csv `data.csv`
2. **Features**: Name, Position, Month, Day, Year, Team, Location (Home: 0, At: 1), Opponent, Minutes Played
3. **Attributes**: FGA, FGM, 3PA, 3PM, FTA, FTM, Rebounds, Assists, Steal, Block, Turnovers, Points

### Machine Learning Model Setup
1. `readying_data.py` takes `cleaned_data.csv` and performs a variety of operations:
   1. map *team* to a respective *team_id*
   2. delete rows where players did not play
   3. convert *name* to a respective *player_id*
   4. map *opp* to a respective *team_id*
   5. convert *position* to their respective number (PG:1, SG:2, SF:3, PF:4, C:5)
   6. convert *minutes played* to total seconds on field
   7. convert date to Month, Day, and Year columns

2. Added files `readying_data.py`, `learning.py`, `tool.py`, `main.py`
   1. `main.py` is the driver of the program. **As of right now, you have to enter player stats one by one**
   2. `tool.py` is the file that holds all the variables needed for the program
   3. `readying_data.py` is the file that transforms the data to what is comfortable for machine learning
   4. `learning.py` is the file that contains the random forest model.

3. Updated dataset to include games between 03/07-03/09

4. A load ml model file functionality was added to avoid training after every input
   1. `rf_model.sav' is the file for the model, if the program detects that it is present then it will skip training and use current file
   2. If it is not present then it will train a new instance of the model and save it into `rf_model.sav` for next time
   3. *General Housekeeping* delete `rf_model.sav` if you add more data to the dataset since we have not added online learning to this model.
      1. Will consider this in the future.

5. Next feature to be added is bulk upload.

