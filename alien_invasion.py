import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()                                                                     #time tracking
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)                                   #full screen
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")
                               
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()


    def run_game(self):
        while True:
            self._check_events()
            self.ship.update() 
            self._update_bullets()
            self._update_aliens()
            self._update_screen()           
            self.clock.tick(60)  


    def _quit_game(self):
        sys.exit()


    def _check_events(self):
        for event in pygame.event.get():
            self._handle_key_event(event) 


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


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        
    
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if not self.aliens:                                     # if the fleet is destroyed
            self.bullets.empty()                                # clear the bullets
            self._create_fleet()                                # create a new fleet

    
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _check_fleet_edges(self):                             # check position on the screen
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1                        # changing direction to the opposite (from right to left in this case)

    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Shit happens ;)")

                    
    def _update_screen(self):
        self.screen.fill(self.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()                                                                       #updates the screen                             
q

if __name__ == '__main__':
    ai = AlienInvasion()                                                                            #instance of the class gets created
    ai.run_game()