import pygame

import random
from random import choice

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird




class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacles_classes = [Cactus, Cactus, Bird] ## Envolve as classes em uma lista para usar a função choice

    def update(self, game):
        if len(self.obstacles) == 0:
            self.class_choice = choice(self.obstacles_classes) ## escolhe aleatoriamente uma das classes a ser ativada
            if self.class_choice == Cactus:
                self.obstacles.append(Cactus(SMALL_CACTUS + LARGE_CACTUS)) ## Une as duas listas             
            elif self.class_choice == Bird:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    game.game_speed = 20 ## Reinicio da velocidade do jogo
                    break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []