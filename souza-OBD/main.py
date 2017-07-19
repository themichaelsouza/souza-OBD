# souza-OBD
# Created by Michael Souza
# 6/22/17

import obd
import pygame
from hud_module import *
from settings import *
from sprites import *


class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.connection = obd.OBD()
        self.command = obd.commands.RPM
        self.response = self.connection.query(self.command)

        self.mph = 0
        self.rpm = self.response.value
        self.throttle_position = 0
        self.temp = 0
        self.fuel = 100
        self.oil_pressure = 0
        self.fuel_pressure = 0

        self.test_module_1 = HudModule("MPH", 0)
        self.test_module_2 = HudModule("RPM", 1)
        self.test_module_3 = HudModule("THROTTLE POS", 2)
        self.test_module_4 = HudModule("TEMP", 3)
        self.test_module_5 = HudModule("FUEL", 4)
        self.test_module_6 = HudModule("OIL PRESSURE", 5)
        self.test_module_7 = HudModule("FUEL PRESSURE", 6)

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
        pygame.mouse.set_visible(False)
        #self.mph += 1
        #self.rpm += 33
        #self.throttle_position += 1
        #self.temp += 3
        #self.fuel -= 1
        #self.oil_pressure += 3
        #self.fuel_pressure +=2

        if self.mph >= 150:
            self.mph = 0
        if self.rpm >= 5000:
            self.rpm = 0
        if self.throttle_position >= 100:
            self.throttle_position = 0
        if self.temp >= 350:
            self.temp = 0
        if self.fuel <= 0:
            self.fuel = 100
        if self.oil_pressure >= 140:
            self.oil_pressure = 0
        if self.fuel_pressure >= 200:
            self.fuel_pressure = 0

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)

        self.test_module_1.draw_hud_modules(self.screen, self.mph)
        self.test_module_2.draw_hud_modules(self.screen, self.rpm)
        self.test_module_3.draw_hud_modules(self.screen, self.throttle_position)
        self.test_module_4.draw_hud_modules(self.screen, self.temp)
        self.test_module_5.draw_hud_modules(self.screen, self.fuel)
        self.test_module_6.draw_hud_modules(self.screen, self.oil_pressure)
        self.test_module_7.draw_hud_modules(self.screen, self.fuel_pressure)

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
