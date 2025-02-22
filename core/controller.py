import pygame
from pygame.locals import *

class EventHandler:
    def __init__(self):
        self.rotate_x = 0
        self.rotate_y = 0
        self.tex_rotate = 0
        self.mouse_pos = {1: None, 3: None}

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button in self.mouse_pos:
                    self.mouse_pos[event.button] = event.pos
            elif event.type == MOUSEBUTTONUP:
                if event.button in self.mouse_pos:
                    self.mouse_pos[event.button] = None
            elif event.type == MOUSEMOTION:
                if self.mouse_pos[1]:
                    dx = event.pos[0] - self.mouse_pos[1][0]
                    dy = event.pos[1] - self.mouse_pos[1][1]
                    self.rotate_y += dx
                    self.rotate_x += dy
                    self.mouse_pos[1] = event.pos
                if self.mouse_pos[3]:
                    dx = event.pos[0] - self.mouse_pos[3][0]
                    self.tex_rotate += dx
                    self.mouse_pos[3] = event.pos
        return True