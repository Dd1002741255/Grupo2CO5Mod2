import pygame
import os


pygame.init()
pygame.mixer.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 36
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
HEART_TYPE  = 'heart'
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

#Only the path to the music is needed
MUSIC_THEME = os.path.join(IMG_DIR, 'sounds/Theme.mp3')
START_SOUND = os.path.join(IMG_DIR, 'sounds/Start.mp3')
SHOOT_SOUND = os.path.join(IMG_DIR, 'sounds/Shoot_player.mp3')
DEAD_SOUND = os.path.join(IMG_DIR, 'sounds/dead_sound.mp3')

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
EXPLOSION1 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/ex1.png"))
EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, "Explosion/explotion.png"))
EXPLOSION3 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/ex3.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png"))

FONT_STYLE = 'freesansbold.ttf'

MENU_BACKGROUND = pygame.image.load(os.path.join(IMG_DIR, 'Other/background.png'))

COLLISSION_SOUND = os.path.join(IMG_DIR, 'sounds/collision.mp3')