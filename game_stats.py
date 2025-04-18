import json

class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        filename = 'high_score.json'
        try:
            with open(filename) as f:
                contents = f.read()
                if contents.strip():  # Check if file is not empty
                    return json.loads(contents)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0
        return 0 
    
    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
        self.score = 0                                    # gets updated when a new game's started
        self.level = 1