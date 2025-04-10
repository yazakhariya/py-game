import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()                                                                     #time tracking
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)     #full screen
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")
                               
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _quit_game(self):
        sys.exit()
    
    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _handle_key_event(self, event):
        if event.type not in (pygame.KEYDOWN, pygame.KEYUP):
            return
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            self._quit_game()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self._fire_bullet()
        
        controls = {
            pygame.K_RIGHT: 'moving_right',
            pygame.K_LEFT: 'moving_left'
        }

        if event.key in controls:
            setattr(self.ship, controls[event.key], event.type == pygame.KEYDOWN)


    def _check_events(self):
        for event in pygame.event.get():
            self._handle_key_event(event)
                    

    def _update_screen(self):
        self.screen.fill(self.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()

        pygame.display.flip()                                  #updates the screen


    def run_game(self):

        while True:
            self._check_events()
            self.ship.update() 
            self._update_bullets()

            self._update_screen()           
            self.clock.tick(60)                                


if __name__ == '__main__':
    ai = AlienInvasion()                                       #instance of the class gets created
    ai.run_game()