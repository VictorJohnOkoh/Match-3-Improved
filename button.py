import pygame


class Button:
    """ A button class that can use either an image or text to create an instance of a button"""

    def __init__(self, *, body: str = '', body2: str = '', body3: str = '', font: pygame.font.Font | None = None, text : str = '', function = None, args : tuple = (), kwargs : dict | None = None):
        self.font = font
        self.text = text
        if text != '':
            self.image = self.font.render(self.text, True, (0,0,0))
            self.image_hover = self.font.render(self.text, True, (255, 0, 0))
            self.image_clicked = self.font.render(self.text, True, (255, 255, 0))
        else:
            self.image = pygame.image.load(body)
            self.image_hover = pygame.image.load(body2)
            self.image_clicked = pygame.image.load(body3)
        self.rect = self.image.get_rect()
        self.pressed_until = None
        self.function = function
        self.args = args
        self.kwargs = kwargs or {}

        # starts the click animation
    def press(self, hold : int = 120):
        self.pressed_until = pygame.time.get_ticks() + hold

        # feed every event to this, it starts the animation on a left click
    def clicked(self, event, hold : int = 120):
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
                and self.pressed_until is None
                and self.rect.collidepoint(event.pos)):
            self.press(hold)

        # true on the one frame the animation ends, runs the button's function
    def finished(self) -> bool:
        if self.pressed_until is not None and pygame.time.get_ticks() >= self.pressed_until:
            self.pressed_until = None
            if self.function is not None:
                self.function(*self.args, **self.kwargs)
            return True
        return False

        # draws the button to the screen as well as the hover and clicked states
    def draw(self, mouse_pos : tuple[float, float], screen, coords : tuple[int, int] = None):
        if coords:
            self.rect.center = coords

        # Manages the hover, clicked and idle states of the button
        if self.pressed_until is not None:
            image = self.image_clicked
        elif self.rect.collidepoint(mouse_pos):
            image = self.image_clicked if pygame.mouse.get_pressed()[0] else self.image_hover
        else:
            image = self.image
        screen.blit(image, self.rect)
