####################################################################################################
# Import
####################################################################################################

import modules.settings
import OpenGL.GL
import pygame

####################################################################################################
# Class
####################################################################################################

class Engine():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(modules.settings.CAPTION)
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((modules.settings.DISPLAY_WIDTH, modules.settings.DISPLAY_HEIGHT), pygame.DOUBLEBUF | pygame.OPENGL)

    def run(self):
        # Infinite Loop
        while True:
            # Check For Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Update
            OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT | OpenGL.GL.GL_DEPTH_BUFFER_BIT)
            pygame.display.flip()

            # Clock
            self.clock.tick(modules.settings.FPS)
