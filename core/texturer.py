import pygame
from OpenGL.GL import *

class TextureManager:
    def __init__(self):
        glEnable(GL_TEXTURE_2D)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

        self.textures = self.init_textures()

    def load_texture(self, image_path, darken=False, brightness_factor=1.0):
        surface = pygame.image.load(image_path).convert_alpha()
        
        if darken:
            arr = pygame.surfarray.pixels3d(surface)
            arr[:] = (arr * brightness_factor).clip(0, 255)
            del arr

        image_data = pygame.image.tostring(surface, "RGB", True)
        width, height = surface.get_size()

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0,
                     GL_RGB, GL_UNSIGNED_BYTE, image_data)
        return texture_id

    def init_textures(self):
        return {
            "top": self.load_texture("assets/top.png"),
            "side": self.load_texture("assets/side.png"),
            "bottom": self.load_texture("assets/bottom.png"),
            "background": self.load_texture("assets/background.png", darken=True, brightness_factor=0.5),
        }