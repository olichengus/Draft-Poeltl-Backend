from src.GuessScore import GuessScore


class Player:
    def __init__(self, ids, d_year, d_round, d_pick, d_team, d_college, d_pos):
        self.id = ids
        self.d_year = d_year
        self.d_round = d_round
        self.d_pick = d_pick
        self.d_team = d_team
        self.d_college = d_college
        self.pos = d_pos

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

    # compares players and returns a guess score
    def draft_match(self, player):
        gs = GuessScore()
        gs.get_scores(self,player)
        return gs
