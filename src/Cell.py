import pygame

size = width, height = 900, 500
screen = pygame.display.set_mode(size)


class Cell:
    def __init__(self, texture, x, y, scale_factor, id):
        self.containment = None
        self.id = id
        self.scale_factor = scale_factor
        self.start_texture = texture
        self.texture = pygame.transform.scale(self.start_texture, (
            texture.get_rect().width * scale_factor, texture.get_rect().height * scale_factor))
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y

    def addcontainment(self, containment):
        self.containment += [containment]

    def move(self, x, y):
        self.rect.x += x * self.scale_factor
        self.rect.y += y * self.scale_factor

        for i in self.containment:
            i.Move(x, y)

    def selfprint(self):
        screen.blit(self.texture, self.rect)
