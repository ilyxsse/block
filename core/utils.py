from OpenGL.GL import *
from contextlib import contextmanager

@contextmanager
def push_matrix(mode=GL_MODELVIEW):
    previous_mode = glGetIntegerv(GL_MATRIX_MODE)
    glMatrixMode(mode)
    glPushMatrix()
    try:
        yield
    finally:
        glPopMatrix()
        glMatrixMode(previous_mode)