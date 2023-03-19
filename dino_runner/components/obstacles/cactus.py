import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 5) ## Aumentado de 0-2 para 0-5 para englobar a nova lista
        super().__init__(image, self.type)
        self.rect.y = 325 if self.type < 3 else 300 #3 ajusta a posição dos cactos segundo a ordem na lista definida em obstacleManager
