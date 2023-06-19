import random
import pygame
import pygame.mixer

from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self, game):
        self.add_enemy(game.limit)
        for enemy in self.enemies:
            if enemy.rect.colliderect(game.player.rect) and game.player.power_up_type != 'shield':
                game.player.add_lifes(-1)
                self.enemies.remove(enemy)
                if game.player.lifes_account <= 0:
                    game.bullet_manager.dead_sound.play()
                    game.playing = False
                if game.player.lifes_account > 0:
                    game.player.sound_collision.play()
            enemy.update(self.enemies, game)

    def draw (self, screen):
        for enemy in self.enemies:
            enemy.draw(screen, exploding=False)

    def add_enemy(self, limit):
        enemy_type = random.randint(1,4)
        if enemy_type ==1:
            enemy = Enemy()
        else:
            x_speed = 5
            y_speed = 2
            move_x_for = [50, 120]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)

        if len(self.enemies) < limit:
            self.enemies.append(enemy)
    
    def reset(self):
        self.enemies = []