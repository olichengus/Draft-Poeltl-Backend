from nba_api.stats.endpoints import playerindex
from nba_api.stats.endpoints import drafthistory
import random


class GamePlatform:
    def __init__(self):
        self.players = playerindex.PlayerIndex(league_id="00", season="2023").get_data_frames()[0]
        self.availableYears = [2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
        self.poeltlPlayer = None
        self.round = 0
        self.answerPlayer = None

# finds new player for new iteration of the game
    def setNewPlayer(self):
        draft_Year = random.choice(self.availableYears)
        years_df = self.players[self.players["DRAFT_YEAR"] == draft_Year]
        player_selection = years_df.sample()
        p_round = player_selection[0]["DRAFT_ROUND"]
        p_pick = player_selection[0]["DRAFT_NUMBER"]
        p_college = player_selection[0]["COLLEGE"]
        p_pos = player_selection[0]["POSITION"]
        p_team = self.getDraftTeam(draft_Year,p_round,p_pick)

    # returns the team name that made p overall pick in the r round of the y draft
    def getDraftTeam(self,y,r,p):
        draft = drafthistory.DraftHistory(league_id="00",season_year_nullable=y,round_num_nullable=r,
                                          overall_pick_nullable=p).get_data_frames()[0]
        return draft["TEAM_NAME"]

    # used for Testing purposes
    def setNewPlayerNotRandom(self):
        return True


    def submit(self, year, round, pick, team):
        return False