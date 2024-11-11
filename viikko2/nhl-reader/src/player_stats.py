class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players(nationality)
        players.sort(key=lambda player: player.goals + player.assists, reverse=True)
        return players
    
    def __str__(self):
        return "hello stats"
