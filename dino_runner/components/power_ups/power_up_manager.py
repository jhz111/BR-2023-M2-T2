import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart, HEART
from dino_runner.components.dinossaur import SHIELD_TYPE, HAMMER_TYPE, HEART_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        self.power_ups_list = [
            Shield(),
            Hammer(), 
            Heart()
        ]

        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_ups.append(self.power_ups_list[random.randint(0, 2)])

    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
                    
                if power_up.type == HAMMER_TYPE:
                    player.hammer = True
                    player.shield = False
                if power_up.type == SHIELD_TYPE:
                    player.shield = True
                    player.hammer = False
                if power_up.type ==  HEART_TYPE:
                    player.hearts += 1

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300) ## parte 2 da logica de aparição