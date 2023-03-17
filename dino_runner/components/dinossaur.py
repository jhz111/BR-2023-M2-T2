import pygame
from dino_runner.utils.constants import RUNNING, JUMPING

X_POS = 80 ## constante de posição horizontal
Y_POS = 310 ## constante de posição vertical
JUMP_VEL = 8.5 ## constatnte de velocidade de pulo que entrará em cálculo para progressão do jogo 
## criação de constantes para simplificar o código

class Dinossaur:
    def __init__(self):
        self.image = RUNNING[0] ## Lista iniciando a imagem do dino correndo, partido da primeira imagem
        self.dino_rect = self.image.get_rect() ## seleção do quadrado de ocorrencia do dino, usando da função get_rect()
        self.dino_rect.x = X_POS ## posição horizontal do dino
        self.dino_rect.y = Y_POS ## posição vertical do dino
        self.step_index = 0 ## contagem de passos do dino que dá uma impressão de distancia percorrida
        self.dino_jump = False ## Evento de pulo
        self.dino_run = True ## Evento de corrida do dino(sempre está correndo atté o jogo acabar)
        self.jump_vel = JUMP_VEL ## evento de cálculo da velocidade do pulo ao pular

    def update(self, user_input): ## metódo presente em todos os objetos (<<< assim como o método draw) atualiza o estado do objetp, no caso o dino.
        if user_input[pygame.K_SPACE] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True

        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        
        if self.step_index >= 10: ## completa a logica criando alternancia entre as imagens do array
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1] ##  atualiza a imagem do dino alternando entre as imagens da array que contem o dino correndo, dando a impressão de corrida ao dino
        self.dino_rect = self.image.get_rect() ## atualiza a imagem de acordo com a condição
        self.dino_rect.x = X_POS ## posição horizontal do dino
        self.dino_rect.y = Y_POS ## posição vertical do dino
        self.step_index += 1 ## adiciona uma pontuação ao final do ciclo 

    def jump(self): ## acrescenta o método de pulo do dino
        self.image = JUMPING ## o dino mantem a mesma imagem enquanto pula
        if self.dino_jump: ## eveto de pulo do dino =  True
            self.dino_rect.y -= self.jump_vel * 4 ## calculo baseado na logica dos frames 
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL: ## evento de término do pulo do dino
            self.dino_rect.y = Y_POS ## retornando a posição inicial do eixo vertical
            self.jump_vel = JUMP_VEL ## retora a velociade de pulo
            self.dino_jump = False # retorna False a não ocorrencia do eveto de pulo

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y)) ##desenha na tela o enfileiramento das imagens