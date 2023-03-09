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

