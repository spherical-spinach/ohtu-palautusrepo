import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.statistics_service = StatisticsService(PlayerReaderStub())

    def test_name_in_players_list_is_found(self):
        player = self.statistics_service.search("Semenko")
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)

    def test_fake_name_in_players_list_is_not_found(self):
        self.assertEqual(self.statistics_service.search("asdf"), None)

    def test_team_search_returns_correct_players(self):
        players = self.statistics_service.team("EDM")
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_top_player_is_correct_without_sortby(self):
        topPlayerList = self.statistics_service.top(1)
        self.assertEqual(topPlayerList[0].name, "Gretzky")

    def test_sorting_top_by_goals_works(self):
        topPlayerList = self.statistics_service.top(1, SortBy.GOALS)
        self.assertEqual(topPlayerList[0].name, "Lemieux")

    def test_sorting_top_by_assists_works(self):
        topPlayerList = self.statistics_service.top(1, SortBy.ASSISTS)
        self.assertEqual(topPlayerList[0].name, "Gretzky")

    def test_sorting_top_by_invalid_value_returns_error(self):
        with self.assertRaises(ValueError):
            self.statistics_service.top(10, 999)
        