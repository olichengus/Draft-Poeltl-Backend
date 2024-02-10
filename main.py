# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
from nba_api.stats.endpoints import leagueleaders
from nba_api.stats.endpoints import drafthistory
from nba_api.stats.endpoints import playercareerstats

# Anthony Davis


def print_hi(name):
    try:
        draft_2023 = drafthistory.DraftHistory(league_id="00")
        #      # Pull data for the top 500 scorers
        #     top_500 = leagueleaders.LeagueLeaders(
        #         season='2023-24',
        #         season_type_all_star='Regular Season',
        #         stat_category_abbreviation='PTS'
        #     ).get_data_frames()[0][:500]
        #
        #     # Correct column names for grouping
        #     avg_stats_columns = ['MIN', 'FGM', 'FGA', 'FTM', 'FTA', 'PTS', 'FG3M', 'FG3A']
        #     top_500_avg = top_500.groupby(['PLAYER', 'PLAYER_ID'])[avg_stats_columns].mean()
        #
        #     # Inspect the first few rows of the averaged stats
        #     print(top_500_avg.head())
        print(draft_2023.get_data_frames()[0])
        print("bruh")
    except Exception as e:
        print(f"An error occurred: {e}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
