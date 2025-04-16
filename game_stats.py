class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0                               # does not get updated

    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
        self.score = 0                                    # gets updated when a new game's started
        self.level = 1