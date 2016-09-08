# Project taken and adapted from "Python Crash Course" by Eric Matthes

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion - By Ben")
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main game loop
    while True:
        # Watch for keyboard and mouse events:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        # Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
