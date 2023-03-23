import pygame

import random
from random import choice

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, HAMMER_TYPE, DEFAULT_TYPE, HEART_TYPE, SHIELD_TYPE
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird




class ObstacleManager:
    def __init__(self):
        self.obstacles = []
         ## Envolve as classes em uma lista para usar a função choice

    def update(self, game):
        self.obstacles_classes = [
            Cactus(SMALL_CACTUS + LARGE_CACTUS),
            Bird(BIRD)
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(self.obstacles_classes[random.randint(0, 1)]) ## escolhe aleatoriamente uma das classes a ser ativada

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.has_power_up:
                    if game.player.type == HAMMER_TYPE:
                        self.obstacles.remove(obstacle)
                    elif game.player.type == SHIELD_TYPE:
                        continue
                    elif game.player.type == HEART_TYPE:
                        continue
                elif not game.player.has_power_up:
                    if game.player.hearts > 0:
                        game.player.hearts -= 1
                        game.game_speed = 20
                        self.obstacles.remove(obstacle)
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break
                


                elif not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
    

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []