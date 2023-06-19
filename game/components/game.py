import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.menu import Menu
#agregado el importe
import time


from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, GAME_OVER, MUSIC_THEME, START_SOUND
from game.components.spaceship import Spaceship

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((0, 255, 255))
        self.limit = 3
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.death_count = 0
        self.score = 0
        self.selected = 0
        self.menu = Menu('PRESIONA ENTER PARA EMPEZAR...', self.screen)
        self.power_up_manager = PowerUpManager()
        self.max_score = 0
        self.start_sound = pygame.mixer.Sound(START_SOUND)
        self.last_score_increase = time.time()
        self.selected_difficulty = False


    def execute(self):
        pygame.mixer.music.load(MUSIC_THEME)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        self.running = True
        while self.running:
            if not self.playing:  # Pantalla del final
                self.show_finalscreen()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.score = 0
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.playing = True
        self.player.lifes_account = 1

        # Cargar y reproducir el sonido de inicio
        self.start_sound.play()

        # Cargar y reproducir la música de fondo
        pygame.mixer.music.load(MUSIC_THEME)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        current_time = time.time()
        # Comprueba si ha pasado al menos 4 segundos desde la última vez que se aumentó el score
        if current_time - self.last_score_increase >= 4:
            self.score += 5
            self.last_score_increase = current_time
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        self.enemy_manager.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((0, 255, 255))  # Change the background color to cyan (RGB: 0, 255, 255)
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_life()
        self.power_up_manager.draw(self.screen)

        self.draw_score()
        self.draw_power_up_time()

        pygame.display.update()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
            
        self.y_pos_bg += self.game_speed

    
    def show_finalscreen(self):
        self.check_max_score()
        self.menu.draw(self.death_count, self.score, self.max_score, self.screen, self.selected_difficulty,  self)
        self.menu.update(self)
    
    def check_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
    
    def update_score(self):
        self.score += 1
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000, 2)

            if time_to_show >=0:
                font = pygame.font.Font(FONT_STYLE, 30)
                text = font.render(f'{self.player.power_up_type.capitalize()} is enabled for {time_to_show} seconds', True, (255,255,255))
                #text_rect = text.get_rect()
                self.screen.blit(text,(540, 50))
            else:
                self.player_has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
    
    
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (100, 100)
        self.screen.blit(text, text_rect) 
        
        
        
    def draw_life(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Lives: {self.player.lifes_account}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (100, 50)
        self.screen.blit(text, text_rect) 
