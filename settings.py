class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.speedup_scale = 3.2
        self.score_scale = 1.5
        self.ships_limit = 3
        self.initialize_dynamic_settings()

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        self.fleet_drop_speed = 10
        
    def initialize_dynamic_settings(self):
        self.ship_speed = 3
        self.bullet_speed = 5.0
        self.alien_speed = 2.5
        self.fleet_direction = 1                  # moving to the right, -1 for a left moving
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)