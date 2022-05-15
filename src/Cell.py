import pygame

size = width, height = 900, 500
screen = pygame.display.set_mode(size)
scale_factor = 3
textures = [pygame.image.load('../animation/floor.jpeg'), pygame.image.load('../animation/wall.jpeg'), pygame.image.load(
    '../animation/wall3.png'), pygame.image.load('../animation/floor.jpeg')]


class Cell:
    def __init__(self, texture, x, y, scale_factor, id, dot_texture):
        self.id = id
        self.scale_factor = scale_factor
        self.start_texture = texture
        self.texture = pygame.transform.scale(self.start_texture, (
            texture.get_rect().width * scale_factor, texture.get_rect().height * scale_factor))
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.withGhost = False
        self.dot_texture = pygame.transform.scale(dot_texture, (
            dot_texture.get_rect().width * self.scale_factor, dot_texture.get_rect().width * self.scale_factor))
        if self.id == 0:
            self.withdot = True
        else:
            self.withdot = False

    def selfprint(self):
        screen.blit(self.texture, self.rect)
        if self.withdot:
            rect = self.dot_texture.get_rect()
            rect.x = self.rect.x + (self.rect.width / 2 - self.dot_texture.get_rect().width / 2)
            rect.y = self.rect.y + (self.rect.height / 2 - self.dot_texture.get_rect().height / 2)
            screen.blit(self.dot_texture, rect)
