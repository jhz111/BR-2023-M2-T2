import pygame
import os

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE, SKULL, HEART, DINO_METEOR, DINO_DEAD, GAME_OVER, RESET, HEART_TYPE
from dino_runner.components.dinossaur import Dinossaur ## instancia internamente o objeto dinossauro para dentro do game
from dino_runner.components.obstacles.obstacleManager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False ## executando aplicacao
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0


        self.player = Dinossaur() ## criação do player como uma instancia do dino
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self): 
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.score = 0 ## Retorna o score a 0
        self.game_speed = 20
        self.player.hearts += 1
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed() ## percdebe interação do usuário
        self.player.update(user_input) ## pega o método do objeto dino para atualizar o game com a entrada do usuário
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen) ## método do bjeto dinossauro que desenha para o usuario o dino
        self.obstacle_manager.draw(self.screen)
        self.draw_info()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_text(self, text_choiced, font_size, xpos, ypos):  ## Método para criar texto usando o texto, tamanho e posições
            font = pygame.font.Font(FONT_STYLE, int(font_size))
            text = font.render(text_choiced, True, (72, 77, 80))
            text_rect = text.get_rect()
            text_rect.center = (xpos, ypos)
            self.screen.blit(text, text_rect)

    def draw_info(self):
        self.draw_text(f'SCORE: {self.score}', 15, 900, 50) ## Cria um texto no canto da tela com as informações de score
        self.draw_text(f'HEARTS: {self.player.hearts}', 15, 900, 100)   
        self.screen.blit(HEART, (785, 90))
        self.draw_text(f'LOSSES: {self.death_count}', 15, 900, 150)
        self.screen.blit(SKULL, (780, 130)) 
          
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                if self.player.type == HEART_TYPE:
                    pass
                else:               
                    self.draw_text(f'{self.player.type.capitalize()} enabled for {time_to_show} seconds', 14, 550, 40)

            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        self.half_screen_height = SCREEN_HEIGHT // 2
        self.half_screen_width = SCREEN_WIDTH // 2
        if self.death_count == 0:
            self.draw_text('press any key to start', 40, self.half_screen_width, self.half_screen_height)
        else:
            self.screen.blit(DINO_METEOR, (500, 220))
            self.screen.blit(GAME_OVER, (375, 100))
            self.draw_text(f'SCORE: {self.score}', 18, self.half_screen_width, 150) ## contador de score
            self.draw_text(f'LOSSES: {self.death_count}', 18, self.half_screen_width, 450) ## contador de mortes
            self.draw_text('PRESS ANY KEY TO RESTART', 28, self.half_screen_width, 500)            

        pygame.display.flip()

        self.handle_events_on_menu()