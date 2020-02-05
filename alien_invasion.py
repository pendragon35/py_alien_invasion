import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_function as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "play")
    stats = GameStats(ai_settings)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:
        gf.check_events(ai_settings, screen, ship, stats, play_button, bullets, aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, bullets, ship, ai_settings)
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)
            print(len(bullets))

        gf.update_screen(
            ai_settings, screen, ship,
            bullets, aliens, stats, play_button)

run_game()