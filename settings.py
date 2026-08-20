import pygame
import sys

def settings(screen : pygame.Surface | None = None, **kwargs):
    run = True
    while run:

        mouse_pos = pygame.mouse.get_pos()

        screen.fill((0,0,0)) if screen else kwargs["screen"].fill((0, 0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()