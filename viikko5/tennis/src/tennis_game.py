class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.is_deuce():
            return self.get_deuce_score()
        elif self.is_advantage():
            return self.get_advantage_score()
        elif self.is_win():
            return self.get_win_score()
        else:
            return self.get_normal_score()

    def is_deuce(self):
        return self.player1_score == self.player2_score and self.player1_score >= 3

    def is_advantage(self):
        return abs(self.player1_score - self.player2_score) == 1 and self.player1_score >= 3 and self.player2_score >= 3

    def is_win(self):
        return abs(self.player1_score - self.player2_score) >= 2 and self.player1_score >= 4 or self.player2_score >= 4

    def get_deuce_score(self):
        return "Deuce"

    def get_advantage_score(self):
        if self.player1_score > self.player2_score:
            return "Advantage player1"
        else:
            return "Advantage player2"

    def get_win_score(self):
        if self.player1_score > self.player2_score:
            return "Win for player1"
        else:
            return "Win for player2"

    def get_normal_score(self):
        scores = ["Love", "Fifteen", "Thirty", "Forty"]
        if self.player1_score == self.player2_score:
            return f"{scores[self.player1_score]}-All"
        else:
            return f"{scores[self.player1_score]}-{scores[self.player2_score]}"
