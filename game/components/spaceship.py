import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
import pygame.mixer
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP, SHOOT_SOUND, DEFAULT_TYPE, COLLISSION_SOUND

class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10

    def __init__(self):
        self.image = SPACESHIP
        self.sound_collision = pygame.mixer.Sound(COLLISSION_SOUND)
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0

        self.shoot_sound = pygame.mixer.Sound(SHOOT_SOUND)
        self.shoot_sound.set_volume(0.3)
        self.lifes_account = 1

    def update(self, user_input, game):
        movement_actions = {
            pygame.K_LEFT: self.move_left,
            pygame.K_RIGHT: self.move_right,
            pygame.K_UP: self.move_up,
            pygame.K_DOWN: self.move_down
        }

        for key, action in movement_actions.items():
            if user_input[key]:
                action()

        if user_input[pygame.K_SPACE]:
            self.shoot(game)

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.right >= SCREEN_WIDTH - self.SHIP_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SHIP_SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet)
        self.shoot_sound.play()
        
    def set_image(self, size = (SHIP_WIDTH, SHIP_HEIGHT), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)
        
    def add_lifes(self,new_life):
        if self.lifes_account + new_life <= 3:
            self.lifes_account += new_life
        else:
            self.lifes_account = 3
