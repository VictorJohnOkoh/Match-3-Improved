import pygame
import sys
from button import Button


back_button = Button(body ='assets/buttons/back.png', body2 ='assets/buttons/back_hover.png', body3 ='assets/buttons/back_pressed.png')


def settings_srcn(screen : pygame.Surface):
    run = True
    while run:

        mouse_pos = pygame.mouse.get_pos()

        screen.fill((0,0,0))

        back_button.draw(mouse_pos, screen, (75, 75))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            back_button.clicked(event)
        pygame.display.update()

        if back_button.finished():
            run = False