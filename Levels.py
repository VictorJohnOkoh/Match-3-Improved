import sys
import pygame

from button import Button




exit_button = Button(body ='assets/buttons/exit.png', body2 ='assets/buttons/exit_hover.png', body3 ='assets/buttons/exit_pressed.png')

def level1(screen, clock):
    run = True
    while run:
        clock.tick(60)

        mouse_pos = pygame.mouse.get_pos()
        screen.fill((0,0,0))

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            exit_button.clicked(event)

        exit_button.draw(mouse_pos, screen, (75, 75))
        pygame.display.update()

        # checked after the update so the pressed face reaches the screen first
        if exit_button.finished():
            run = False
