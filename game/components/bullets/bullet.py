from pygame.sprite import _Group, Sprite 
import pygame
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT, SCREEN_WIDTH

class Bullet(Sprite):
    BULLET_SIZE = pygame.tansform.scale(BULLET, (10, 10))
    BULLET_ENEMY_SIZE = pygame.tansform.scale(BULLET_ENEMY, (10, 10))
    BULLETS = {'player': BULLET_SIZE, 'enemy': BULLET_ENEMY_SIZE}
    SPEED = 20

    #para gestionar que se hace con la bala
    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type

    def update(self, bullets):
        self.rect.y -= self.SPEED
        if self.rect.y >= SCREEN_HEIGHT:
            bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
