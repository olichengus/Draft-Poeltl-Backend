from nba_api.stats.endpoints import playerindex
from nba_api.stats.endpoints import drafthistory
from src.Player import Player


class MyException(Exception):
    pass


# given draft year, draft round and draft pick returns the team that made that pick
def get_draft_team(y, r, p):
    draft = drafthistory.DraftHistory(league_id="00", season_year_nullable=y, round_num_nullable=r,
                                      overall_pick_nullable=p).get_data_frames()
    draft_dataFrames = draft[0]

    print("Organization:" + draft["ORGANIZATION"][0])
    print("Organization type: " + draft["ORGANIZATION_TYPE"][1])
    return draft["TEAM_NAME"][0]


class GameAPI:
    def __init__(self):
        self.players = playerindex.PlayerIndex(league_id="00", season="2023").get_data_frames()[0]

    # returns a random player from specific draft class
    def get_player_from_draft_year(self, draft_year):
        years_df = self.players[self.players["DRAFT_YEAR"] == draft_year]
        player_selection = years_df.sample()
        p_id = player_selection["PERSON_ID"].values[0]
        p_round = int(player_selection["DRAFT_ROUND"].values[0])
        p_pick = int(player_selection["DRAFT_NUMBER"].values[0])
        p_pos = player_selection["POSITION"].values[0]
        return Player(p_id, draft_year, p_round, p_pick, p_pos)

    # returns player given player_id
    def make_player(self, player_id):
        player_df = self.players[self.players["PERSON_ID"] == player_id]
        if len(player_df) > 0:
            try:
                p_draft_year = int(player_df["DRAFT_YEAR"].values[0])
                p_round = int(player_df["DRAFT_ROUND"].values[0])
                p_pick = int(player_df["DRAFT_NUMBER"].values[0])
            except ValueError:
                print("This player was undrafted")
                raise MyException("This player was undrafted")
            p_pos = player_df["POSITION"].values[0]
            return Player(player_id, p_draft_year, p_round, p_pick, p_pos)
        else:
            print(f"No player found with ID {player_id}.")
            raise MyException("This player was not active in the 2023/24 season")
