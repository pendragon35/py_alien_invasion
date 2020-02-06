import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        self.stats = stats
