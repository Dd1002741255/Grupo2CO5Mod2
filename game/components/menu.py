import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        self.font_large = pygame.font.Font(FONT_STYLE, 50)
        self.font_small = pygame.font.Font(FONT_STYLE, 20)
        self.title_text = self.font_large.render("Spaceship game", True, (255, 0, 0))
        self.title_text_rect = self.title_text.get_rect()
        self.title_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 250)
        self.message_text = self.font_large.render(message, True, (0, 0, 0))
        self.message_text_rect = self.message_text.get_rect()
        self.message_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        self.credit_text = self.font_small.render("Hecho por Daniel Perez", True, (0, 0, 0))
        self.credit_text_rect = self.credit_text.get_rect()
        self.credit_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 280)
        screen.fill((0, 255, 255)) # cyan background

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.title_text, self.title_text_rect)
        screen.blit(self.message_text, self.message_text_rect)
        screen.blit(self.credit_text, self.credit_text_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen): # here to change the background color
        screen.fill((0, 240, 255))

    def update_message(self, message):
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)