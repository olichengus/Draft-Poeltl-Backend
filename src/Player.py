from src.College import College
from src.Team import Team
from nba_api.stats.endpoints import drafthistory

def set_draft_team_info(y, r, p, player):
    draft = drafthistory.DraftHistory(league_id="00", season_year_nullable=y, round_num_nullable=r,
                                      overall_pick_nullable=p).get_data_frames()
    draft_dataFrames = draft[0]
    team_name = draft_dataFrames["TEAM_NAME"][0]
    college_name = draft_dataFrames["ORGANIZATION"][0]
    college_type = draft_dataFrames["ORGANIZATION_TYPE"][0]
    player.d_team.set_team(team_name)
    player.d_col.set_name(college_name)
    player.d_col.set_type(college_type)
    return

class Player:
    def __init__(self, ids, d_year, d_round, d_pick, d_pos):
        self.id = ids  # Int: unique player id
        self.d_year = d_year  # Int: draft year
        self.d_round = d_round  # Int: draft round
        self.d_pick = d_pick  # Int: draft pick
        self.pos = d_pos  # String: Position the player plays
        self.d_team = Team(None)
        self.d_col = College(None, None)
        set_draft_team_info(d_year, d_round, d_pick, self)

    def get_id(self):
        return self.id

    def get_d_year(self):
        return self.d_year

    def get_d_round(self):
        return self.d_round

    def get_d_pick(self):
        return self.d_pick

    def get_d_team(self):
        return self.d_team

    def get_player_dict(self):
        return {key: value for key, value in self.__dict__.items() if not key.startswith("__")}

    # compares players and returns a guess score

