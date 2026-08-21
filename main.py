import pygame
import pygame.font as font
import pygame.mixer as mixer
import sys
from button import Button
import Levels
import settings

pygame.init()
font.init()
mixer.init()


WIDTH = 1000
HEIGHT = 1000

large_font = pygame.font.SysFont("Arial", 50, bold=True)
main_font = font.Font("assets/fonts/franklin-gothic/FranklinGothic.ttf", 30)
title_font = font.Font("assets/fonts/franklin-gothic/Franklin Gothic Bold.ttf", 72)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Match 3")
# icon = pygame.image.load("icon.png")
# pygame.display.set_icon(icon)

clock = pygame.time.Clock()
fps = 60

# Buttons
settings_btn = Button(body='assets/buttons/settings.png', body2='assets/buttons/settings_hover.png', body3='assets/buttons/settings_pressed.png', function=settings.settings_screen, args=(screen,))
exit_btn = Button(body="assets/buttons/exit_small.png", body2="assets/buttons/exit_small_hover.png", body3="assets/buttons/exit_small_pressed.png")
level1 = Button(text='Level 1', font=main_font, function=Levels.level1, args=(screen, clock))


def menu():
    run = True
    while run:
        full_width, full_height = screen.get_size()
        mouse_pos = pygame.mouse.get_pos()

        clock.tick(fps)

        screen.fill((123,0,0))
        text = title_font.render("Main Menu", True, (255, 255, 255))
        text_rect = text.get_rect(center=(full_width/2,100))
        screen.blit(text, text_rect)

        # Draw the buttons to the screen
        level1.draw(mouse_pos, screen, (full_width // 2, full_height // 3))
        settings_btn.draw(mouse_pos, screen, (75, full_height - 50))
        exit_btn.draw(mouse_pos, screen, (full_width - 100, full_height - 50))


        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            level1.clicked(event)
            settings_btn.clicked(event)
            exit_btn.clicked(event)
        pygame.display.update()

        # checked after the update so the pressed face reaches the screen first
        settings_btn.finished()
        level1.finished()
        if exit_btn.finished():
            run = False

    pygame.quit()
    sys.exit()

menu()