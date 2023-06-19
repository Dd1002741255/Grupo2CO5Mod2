


import random

import pygame
from game.components.power_ups.shield import Shield
from game.components.power_ups.lifes import lifes

from game.utils.constants import SPACESHIP_SHIELD, HEART


class PowerUpManager:
    def __init__(self):
        self.shield_power_ups = []
        self.heart_power_ups = []
        self.shield_duration = random.randint(3, 5)
        self.shield_when_appears = random.randint(5000, 10000)
        self.heart_when_appears = random.randint(5000, 10000)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.shield_power_ups) == 0 and current_time >= self.shield_when_appears:
            self.generate_power_up_shield(game)

        if len(self.heart_power_ups) == 0 and current_time >= self.heart_when_appears:
            self.generate_power_up_heart(game)
        
        for power_up in self.shield_power_ups:
            power_up.update(game.game_speed, self.shield_power_ups)

            if game.player.rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.shield_duration * 1000)
                game.player.set_image((65, 75), SPACESHIP_SHIELD)
                self.shield_power_ups.remove(power_up)

        for power_up in self.heart_power_ups:
            power_up.update(game.game_speed, self.heart_power_ups)

            if game.player.rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.add_lifes(1)
                self.heart_power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.shield_power_ups:
            power_up.draw(screen)

        for power_up in self.heart_power_ups:
            power_up.draw(screen)

    def generate_power_up_shield(self, game):
        power_up = Shield()
        self.shield_when_appears += random.randint(5000, 10000)
        self.shield_power_ups.append(power_up)
        
    def generate_power_up_heart(self, game):
        power_up = lifes()
        self.heart_when_appears += random.randint(5000, 10000)
        self.heart_power_ups.append(power_up)
