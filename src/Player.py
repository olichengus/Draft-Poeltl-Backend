class Player:
    def __init__(self, name, d_year, d_round, d_pick, d_team, d_college, d_pos):
        self.name = name
        self.d_year = d_year
        self.d_round = d_round
        self.d_pick = d_pick
        self.d_team = d_team
        self.d_college = d_college
        self.pos = d_pos

    def get_name(self):
        return self.name

    def get_d_year(self):
        return self.d_year

    def get_d_round(self):
        return self.d_round

    def get_d_pick(self):
        return self.d_pick

    def get_d_team(self):
        return self.d_team

    def draftMatch(self, year, round, pick, team):
        return year == self.d_year and round == self.d_round and pick == self.d_pick and team == self.d_team
