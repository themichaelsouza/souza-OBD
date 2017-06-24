# souza-OBD
# Created by Michael Souza
# 6/22/17

import obd
import pygame
import random
from settings import *
from sprites import *


class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.mph = 0

    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        self.mph += 1
        if self.mph >= 150:
            self.mph = 0

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)

        if pygame.font:
            mph_text_font = pygame.font.Font("Dancing Juice & Salabat.ttf", 24)
            mph_font = pygame.font.Font("Dancing Juice & Salabat.ttf", 72)

            mph_text = mph_text_font.render('MPH', 1, (255, 255, 255))
            mph = mph_font.render(str(int(self.mph)), 1, (255, 255, 255))

            mph_text_pos = mph_text.get_rect().move((WIDTH / 2) - (mph_text.get_rect().width / 2), (HEIGHT / 2) - (mph.get_rect().height / 2) - 5)
            mph_pos = mph.get_rect().move((WIDTH / 2) - (mph.get_rect().width / 2), (HEIGHT / 2) - (mph.get_rect().height / 2))

            self.screen.blit(mph_text, mph_text_pos)
            self.screen.blit(mph, mph_pos)

        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()


    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
