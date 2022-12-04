import sys
import pygame
from pygame.sprite import Group
from setting import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200,800))

    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    bg_color = (0, 102, 0)

    # Make an Alien

    aliens = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, aliens)

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # mian loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        screen.fill(bg_color)

        screen.fill(ai_settings.bg_color)
        
        ship.blitme()

        pygame.display.flip()
        
run_game()

