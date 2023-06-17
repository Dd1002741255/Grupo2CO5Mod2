import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
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
        self.menu = Menu('Press Any Key to start...', self.screen)
        self.max_score = 0
        self.start_sound = pygame.mixer.Sound(START_SOUND)
        self.last_score_increase = time.time()


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
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((0, 255, 255))  # Change the background color to cyan (RGB: 0, 255, 255)
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        #pygame.display.flip()

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
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        self.menu.reset_screen_color(self.screen)
        self.check_max_score()
        if self.played_alredy():
            
            message = "Puntuaciones\n" \
                    f"Muertes: {self.death_count}\n" \
                    f"Puntuación: {self.score}\n" \
                    f"Maxima puntuación: {self.max_score}\n"
            font = pygame.font.Font(FONT_STYLE, 30)
            text_surface = self.render_multiline_text(font, message, (0, 0, 0), 400)

            pygame.display.set_caption(message)

            icon = pygame.transform.scale(GAME_OVER, (400, 150))
            self.screen.blit(icon, (half_screen_width - 200, half_screen_height - 200))
            self.screen.blit(text_surface, ((SCREEN_WIDTH - text_surface.get_width()) // 2, half_screen_height + 50))

        self.menu.draw(self.screen)
        self.menu.update(self)
    
    #if we haze played alredy we will show the score
    def played_alredy(self):
        return self.death_count > 0
    
    def check_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
    
    def render_multiline_text(self, font, text, color, max_line_width):
        lines = text.split('\n')
        rendered_lines = []

        for line in lines:
            rendered_line = font.render(line, True, color)
            rendered_lines.append(rendered_line)

        max_line_height = max(rendered_line.get_height() for rendered_line in rendered_lines)
        text_surface = pygame.Surface((max_line_width, max_line_height * len(rendered_lines)), pygame.SRCALPHA)

        current_y = 0
        for rendered_line in rendered_lines:
            text_surface.blit(rendered_line, ((max_line_width - rendered_line.get_width()) // 2, current_y))
            current_y += max_line_height

        return text_surface
    
    
    def update_score(self):
        self.score += 1
    
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (100, 100)
        self.screen.blit(text, text_rect)