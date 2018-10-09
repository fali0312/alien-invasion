class GameStats:
    def __init__(self, ai_settings):
        self.game_active = True
        self.ai_settings = ai_settings

        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.high_score = 0
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
