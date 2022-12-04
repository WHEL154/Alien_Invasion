class Settings():
    """A Class to store all settings for Alient Invasion"""

    def __init__(self):
        """Initilize the game's settings"""

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1       

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 102, 0)

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50
    
    def update(self):
        """Move the alien right."""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)