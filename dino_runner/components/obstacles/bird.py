import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
   def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randrange(200, 310, 50)
        self.wing_index = 0

   def draw(self, screen):
        screen.blit(self.image[int(self.wing_index / 5)], (self.rect.x, self.rect.y)) ## enfileira a imagem e o posicionamento, imagem definida pela divisão inteira por 5 para atrasar o bater das asas
        self.wing_index += 1
        #print(int(self.wing_index/5))
        if self.wing_index >= 10:
            self.wing_index = 0
         