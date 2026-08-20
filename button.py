import pygame

class Button:
    def __init__(self, coords : tuple[float, float], *, body : str = '', body2 : str  = '', body3 : str = '', font : pygame.font.Font | None = None, text : str = ''):
        self.font = font
        self.text = text
        if text != '':
            self.image = self.font.render(self.text, True, (255,255,255))
            self.image_hover = self.font.render(self.text, True, (255, 0, 0))
            self.image_clicked = self.font.render(self.text, True, (255, 255, 0))
        else:
            self.image = pygame.image.load(body)
            self.image_hover = pygame.image.load(body2)
            self.image_clicked = pygame.image.load(body3)

        self.coords = coords
        self.rect = self.image.get_rect(center=self.coords)

        # draws the button to the screen as well as the hover
    def draw(self, mouse_pos : tuple[float, float], screen):
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.image_hover, self.rect)
            if pygame.mouse.get_pressed()[0]:
                screen.blit(self.image_clicked, self.rect)
        else:
            screen.blit(self.image, self.rect)
