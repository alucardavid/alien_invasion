class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
        
        # Ship settings
        self.ship_speed = 3

        # Bullet settings
        self.bullet_speed = 20
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0