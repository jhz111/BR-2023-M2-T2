import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart
from dino_runner.components.dinossaur import SHIELD_TYPE, HAMMER_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.power_ups_list = [Shield, Hammer, Heart]

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.chosen_power_up = random.choice(self.power_ups_list)
            if self.chosen_power_up == Shield:
                self.when_appears += random.randint(200, 300) ## parte 1 da lógica de aparição
                self.power_ups.append(Shield())
            elif self.chosen_power_up == Hammer:
                self.when_appears += random.randint(200, 300)
                self.power_ups.append(Hammer()) ######
            elif self.chosen_power_up == Heart:
                self.when_appears += random.randint(200, 300)
                self.power_ups.append(Heart()) ######

    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                    power_up.start_time = pygame.time.get_ticks()
                    #player.shield = True
                    #player.hammer = True
                    player.has_power_up = True
                    player.type = power_up.type
                    player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                    self.power_ups.remove(power_up)
                    
                    if self.chosen_power_up == Hammer:
                        player.hammer = True
                        player.shield = False
                        player.heart = False
                    if self.chosen_power_up == Shield:
                        player.shield = True
                        player.hammer = False
                        player.heart = False
                    if self.chosen_power_up == Heart:
                        player.shield = False
                        player.hammer = False
                        player.heart = True


        

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300) ## parte 2 da logica de aparição