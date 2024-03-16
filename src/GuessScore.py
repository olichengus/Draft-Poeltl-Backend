from enum import Enum
from src.Player import Player


class Direction(Enum):
    UP = 1
    DOWN = -1


class Status(Enum):
    GREY = -1
    YELLOW = 0
    GREEN = 1


class GuessScore:
    def __init__(self):
        self.year_dir = None
        self.year_score = None
        self.year_dir = None
        self.round_score = None
        self.pick_score = None
        self.pick_dir = None
        self.col_score = None
        self.pos_score = None
        self.team_score = None

    def get_scores(self, player1, player2):
        if player1 is not Player or player2 is not Player:
            raise Exception("a player is missing")
        if player1.id == player2.id:
            self.green_everything()
        else:
            self.calculate_year_scores(player1, player2)
            self.calculate_round_scores(player1, player2)
            self.calculate_pick_scores(player1, player2)
            self.calculate_col_scores(player1, player2)
            self.calculate_pos_scores(player1, player2)
            self.calculate_team_scores(player1, player2)

    def green_everything(self):
        self.year_score = Status.GREEN
        self.round_score = Status.GREEN
        self.pick_score = Status.GREEN
        self.col_score = Status.GREEN
        self.pos_score = Status.GREEN
        self.team_score = Status.GREEN

    def calculate_year_scores(self, player1, player2):
        if player1.d_year == player2.d_year:
            self.year_score = Status.GREEN
        else:
            if player1.d_year > player2.d_year:
                self.year_dir = Direction.UP
            elif player1.d_year < player2.d_year:
                self.year_dir = Direction.DOWN
            dif = abs(player1.d_year - player2.d_year)
            if dif <= 3:
                self.year_score = Status.YELLOW
            else:
                self.year_score = Status.GREY

    def calculate_round_scores(self, player1, player2):
        if player1 is not Player or player2 is not Player:
            raise Exception("a player is missing")
        if player1.d_round == player2.d_round:
            self.year_score = Status.GREEN
        else:
            self.year_score = Status.GREY

    def calculate_pick_scores(self, player1, player2):
        if player1 is not Player or player2 is not Player:
            raise Exception("a player is missing")
        p1 = player1.d_pick
        p2 = player2.d_pick
        if p1 == p2:
            self.pick_score = Status.GREEN
        else:
            if p1 > p2:
                self.pick_dir = Direction.UP
            elif p1 < p2:
                self.pick_dir = Direction.DOWN
            dif = abs(p1 - p2)
            if dif <= 10:
                self.pick_score = Status.YELLOW
            else:
                self.pick_score = Status.GREY
        return True

    def calculate_col_scores(self, player1, player2):
        if player1 is not Player or player2 is not Player:
            raise Exception("a player is missing")
        if player1.d_col == player2.d_col:
            self.col_score = Status.GREEN
        else:
            self.col_score = Status.GREY

    def calculate_pos_scores(self, player1, player2):
        if player1 is not Player or player2 is not Player:
            raise Exception("a player is missing")
        if player1.d_pos == player2.d_pos:
            self.pos_score = Status.GREEN
        else:
            self.pos_score = Status.GREY

    def calculate_team_scores(self, player1, player2):
        if player1 is not Player or player2 is not Player:
            raise Exception("a player is missing")
        if player1.d_team == player2.d_team:
            self.team_score = Status.GREEN
        else:
            self.team_score = Status.GREY
        return True



