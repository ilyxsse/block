from OpenGL.GL import *
from core.utils import push_matrix

class Renderer:
    def __init__(self, display, texture_manager):
        self.display = display
        self.textures = texture_manager.textures

    def draw_background(self):
        width, height = self.display
        with push_matrix(GL_PROJECTION):
            glLoadIdentity()
            glOrtho(0, width, 0, height, -1, 1)
            with push_matrix(GL_MODELVIEW):
                glLoadIdentity()
                glDisable(GL_DEPTH_TEST)
                glBindTexture(GL_TEXTURE_2D, self.textures["background"])
                glBegin(GL_QUADS)
                glTexCoord2f(0, 0); glVertex2f(0, 0)
                glTexCoord2f(1, 0); glVertex2f(width, 0)
                glTexCoord2f(1, 1); glVertex2f(width, height)
                glTexCoord2f(0, 1); glVertex2f(0, height)
                glEnd()
                glEnable(GL_DEPTH_TEST)

    def draw_cube(self, tex_rotate):
        vertices = [
            (-1, -1, -1), (1, -1, -1), (1,  1, -1), (-1,  1, -1),
            (-1, -1,  1), (1, -1,  1), (1,  1,  1), (-1,  1,  1)
        ]

        faces = [
            ([4, 5, 6, 7], "side"),
            ([1, 0, 3, 2], "side"),
            ([0, 4, 7, 3], "side"),
            ([5, 1, 2, 6], "side"),
            ([3, 7, 6, 2], "top"),
            ([0, 1, 5, 4], "bottom")
        ]

        tex_coords = ((0, 0), (1, 0), (1, 1), (0, 1))

        for indices, tex_key in faces:
            glBindTexture(GL_TEXTURE_2D, self.textures[tex_key])
            with push_matrix(GL_TEXTURE):
                glLoadIdentity()
                glTranslatef(0.5, 0.5, 0)
                glRotatef(tex_rotate, 0, 0, 1)
                glTranslatef(-0.5, -0.5, 0)
                glBegin(GL_QUADS)
                for i, vi in enumerate(indices):
                    glTexCoord2f(*tex_coords[i])
                    glVertex3fv(vertices[vi])
                glEnd()