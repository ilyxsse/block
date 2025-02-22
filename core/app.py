import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from core.texturer import TextureManager
from core.renderer import Renderer
from core.controller import EventHandler
from core.utils import push_matrix

class BlockApp:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.display = (width, height)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        glViewport(0, 0, width, height)

        # Set up perspective projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / height, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

        self.texture_manager = TextureManager()
        self.renderer = Renderer(self.display, self.texture_manager)
        self.event_handler = EventHandler()

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            running = self.event_handler.handle_events()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.renderer.draw_background()
            
            glMatrixMode(GL_MODELVIEW)
            with push_matrix():
                glRotatef(self.event_handler.rotate_x, 1, 0, 0)
                glRotatef(self.event_handler.rotate_y, 0, 1, 0)
                self.renderer.draw_cube(self.event_handler.tex_rotate)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        sys.exit()