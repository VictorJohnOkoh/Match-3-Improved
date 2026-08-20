import pygame
import pygame.font as font
import pygame.mixer as mixer
import sys
from button import Button

pygame.init()
font.init()
mixer.init()


WIDTH = 1000
HEIGHT = 1000

large_font = pygame.font.SysFont("Arial", 50, bold=True)
main_font = font.SysFont("bahnschrift,franklin gothic medium,arial", 15, bold=True)
F_A_TITLE = font.SysFont("bahnschrift,franklin gothic medium,arial", 46, bold=True)
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Main Menu")
# icon = pygame.image.load("icon.png")
# pygame.display.set_icon(icon)
clock = pygame.time.Clock()
fps = 60

# Buttons
settings = Button((200, 200), body='assets/buttons/settings.png', body2='assets/buttons/settings_hover.png', body3='assets/buttons/settings_pressed.png')

def menu():
    run = True
    while run:
        full_width, full_height = screen.get_size()
        mouse_pos = pygame.mouse.get_pos()

        clock.tick(fps)

        screen.fill((123,0,0))
        text = F_A_TITLE.render("Main Menu", True, (255,255,255))
        text_rect = text.get_rect(center=(WIDTH/2,150))
        screen.blit(text, text_rect)


        settings.draw(mouse_pos, screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()
    sys.exit()

menu()