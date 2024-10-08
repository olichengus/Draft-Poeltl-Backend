import unittest
from src.GuessScore import Status, Direction, GuessScore
from src.Player import Player
from src.GamePlatform import GamePlatform
from src.GamePlatform import find_lists_of_players_full_name
from src.Game_API.GameAPI import get_draft_team
from nba_api.stats.endpoints import drafthistory


class TestGuessScore(unittest.TestCase):
    def setUp(self):
        self.playerPoeltl = Player(2544,2003,1,1,"SF")
        self.game = GuessScore()

    def test_green_everything(self):
        test_player = Player(2544,2003,1,1,"Lakers")
        res = self.game.get_scores(test_player, self.playerPoetl)
        self.assertEqual(res["year_score"], Status.GREEN)
        self.assertEqual(res['round_score'], Status.GREEN)
        self.assertEqual(res['pick_score'], Status.GREEN)
        self.assertEqual(res['col_score'], Status.GREEN)
        self.assertEqual(res['pos_score'], Status.GREEN)
        self.assertEqual(res['team_score'], Status.GREEN)

    def test_submit_answer(self):
        game = GamePlatform()
        game.set_new_player()
        test_player = "Victor Wembanyama"
        res = game.submit_answer(test_player, "Chris Duarte")
        college = res["d_col"].name
        team = res["d_team"].name
        self.assertIsNotNone(res)

    def test_incorrect_guess(self):
        test_player = Player(2541, 2002,1,6,"SF")
        res = self.game.get_scores(self.playerPoeltl, test_player)
        self.assertEqual(self.game.year_score, Status.YELLOW)
        self.assertEqual(self.game.round_score, Status.GREEN)
        self.assertEqual(self.game.pick_score, Status.YELLOW)
        self.assertEqual(self.game.team_score, Status.GREEN)
        self.assertEqual(self.game.col_score, Status.GREY)
        self.assertEqual(self.game.pos_score, Status.GREY)
        self.assertEqual(self.game.year_dir, Direction.UP)
        self.assertEqual(self.game.pick_dir, Direction.DOWN)

    def test_set_poetl_player(self):
        gamePlatform = GamePlatform()
        gamePlatform.set_new_player()
        self.assertIsNotNone(gamePlatform.poeltlPlayer)

    def test_list_players(self):
        player_full_name = "vic"
        res = find_lists_of_players_full_name(player_full_name)
        res_active = [x for x in res if x["is_active"]]
        res_full_names = [active_player['full_name'] for active_player in res_active]
        print(res_full_names)

    def test_draft_team(self):
        gamePlatform = GamePlatform()
        gamePlatform.set_new_player()





if __name__ == '__main__':
    unittest.main()
