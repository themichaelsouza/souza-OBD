# hud_module.py
# Created by Michael Souza
# 6/28/17

import pygame
from settings import *


class HudModule:
    def __init__(self, text="text", location=0):
        self.text = text
        self.text_font_size = 0
        self.info_font_size = 0
        self.module_location = location

        if self.module_location is 0:
            self.text_font_size = 48
            self.info_font_size = 150
        else:
            self.text_font_size = 24
            self.info_font_size = 75

    def draw_hud_modules(self, screen, info=0):
        if pygame.font:
            text_font = pygame.font.Font(FONT, self.text_font_size)
            info_font = pygame.font.Font(FONT, self.info_font_size)

            text = text_font.render(self.text, 1, (255, 255, 255))
            info = info_font.render(str(int(info)), 1, (255, 255, 255))

            text_pos = text.get_rect().move(self.get_text_location(1, text, info))
            info_pos = info.get_rect().move(self.get_text_location(2, text, info))

            screen.blit(text, text_pos)
            screen.blit(info, info_pos)

    def get_text_location(self, position, text, info):
        x = 0
        y = 0

        # location 0
        if self.module_location is 0 and position is 1:
            x = (WIDTH / 2) - (text.get_rect().width / 2)
            y = (HEIGHT / 2) - (info.get_rect().height / 2) - 5
        elif self.module_location is 0 and position is 2:
            x = (WIDTH / 2) - (info.get_rect().width / 2)
            y = (HEIGHT / 2) - (info.get_rect().height / 2)

        # location 1
        if self.module_location is 1 and position is 1:
            x = SIDE_BUFFER - (text.get_rect().width / 2)
            y = (SIDE_BUFFER - 20) - (info.get_rect().height / 2) - 5
        elif self.module_location is 1 and position is 2:
            x = SIDE_BUFFER - (info.get_rect().width / 2)
            y = (SIDE_BUFFER - 20) - (info.get_rect().height / 2)

        return x, y
