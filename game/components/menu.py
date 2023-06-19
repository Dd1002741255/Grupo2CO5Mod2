import os

import pygame

from game.utils.constants import (FONT_STYLE, GAME_OVER, IMG_DIR,
                                  SCREEN_HEIGHT, SCREEN_WIDTH)


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        self.font_large = pygame.font.Font(FONT_STYLE, 50)
        self.font_small = pygame.font.Font(FONT_STYLE, 20)
        self.font_medium = pygame.font.Font(FONT_STYLE, 35)
        self.title_text = self.font_large.render("SPACESHIPS WAR GAME", True, (0, 0, 255))
        self.title_text_rect = self.title_text.get_rect()
        icon = pygame.transform.scale(GAME_OVER, (400, 150))

        self.title_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 250)
        self.message_text = self.font_large.render(message, True, (255, 255, 255))
        self.message_text_rect = self.message_text.get_rect()
        self.message_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        self.credit_text = self.font_small.render("Hecho por Daniel Perez", True, (0, 0, 0))
        self.credit_text_rect = self.credit_text.get_rect()
        self.credit_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 280)


    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self,death_count, score_count, max_score, screen, selected_dificult, game):
        self.background_image = pygame.image.load(os.path.join(IMG_DIR, 'Other/background.png'))
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(self.background_image, (0, 0))

        # Renderizar sombra del título en blanco
        shadow_title_text = self.font_large.render("SPACESHIPS WAR GAME", True, (255, 255, 255))
        shadow_title_rect = shadow_title_text.get_rect()
        shadow_title_rect.center = (self.HALF_SCREEN_WIDTH + 3, self.HALF_SCREEN_HEIGHT - 247)
        screen.blit(shadow_title_text, shadow_title_rect)

        screen.blit(self.title_text, self.title_text_rect)

        button_text = self.font_medium.render("Presiona la tecla ARRIBA para difícil", True, (255, 255, 255))
        button_rect = button_text.get_rect()
        button_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT -80)
        screen.blit(button_text, button_rect)
        
        button_izi_text = self.font_medium.render("Presiona la tecla ABAJO para fácil", True, (255, 255, 255))
        button_izi_rect = button_izi_text.get_rect()
        button_izi_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 40)
        screen.blit(button_izi_text, button_izi_rect)
        game.selected_dificult = True

        # render game over:
        if death_count > 0:
            icon = pygame.transform.scale(GAME_OVER, (400, 150))
            icon_rect = icon.get_rect()
            icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 150)
            screen.blit(icon, icon_rect)

        # Renderizar sombra del texto "Presiona ENTER para jugar" en blanco
        screen.blit(self.message_text, self.message_text_rect)

        # Renderizar puntuaciones
        if death_count > 0:

            pun_text = self.font_medium.render("Puntuaciones", True, (0, 0, 0))
            pun_text_rect = pun_text.get_rect()
            pun_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 60)

            # Muertes:
            deaths_text = self.font_medium.render(f"Muertes: {death_count}", True, (0, 0, 0))
            deaths_text_rect = deaths_text.get_rect()
            deaths_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 90)
            # Puntuación:
            score_text = self.font_medium.render(f"Puntuacion: {score_count}", True, (0, 0, 0))
            score_text_rect = score_text.get_rect()
            score_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 120)
            # Maxima puntuación:
            max_score_text = self.font_medium.render(f"Maxima puntuacion: {max_score}", True, (0, 0, 0))
            max_score_text_rect = max_score_text.get_rect()
            max_score_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)
        
            # Blit the score texts
            screen.blit(score_text, score_text_rect)
            screen.blit(pun_text, pun_text_rect)
            screen.blit(deaths_text, deaths_text_rect)
            screen.blit(max_score_text, max_score_text_rect)

        # Renderizar sombra del texto "Hecho por Daniel Perez" en negro
        shadow_credit_text = self.font_small.render("Hecho por Daniel Perez", True, (255, 255, 255))
        shadow_credit_rect = shadow_credit_text.get_rect()
        shadow_credit_rect.center = (self.HALF_SCREEN_WIDTH + 1, self.HALF_SCREEN_HEIGHT + 281)
        screen.blit(shadow_credit_text, shadow_credit_rect)

        screen.blit(self.credit_text, self.credit_text_rect)



    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                game.limit = 6
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                game.limit = 3
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game.run()

    def reset_screen_color(self, screen): # here to change the background color
        screen.fill((0, 240, 255))

    def update_message(self, message):
        self.message_text = self.font_large.render(message, True, (255, 255, 255))
        self.message_text_rect = self.message_text.get_rect()
        self.message_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
