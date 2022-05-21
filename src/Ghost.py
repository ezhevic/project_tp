from Character import CharacterInterface
import pygame
import random

ghost_texture = pygame.image.load('../animation/Red_Ghost.png')
size = width, height = 900, 500
screen = pygame.display.set_mode(size)
ghost_scale = 2


class Ghost(CharacterInterface):
    def __init__(self, texture, field):
        self.direction = self.logic()
        self.field = field
        self.texture = pygame.transform.scale(texture, (
            texture.get_rect().width * ghost_scale, texture.get_rect().width * ghost_scale))
        self.rect = self.texture.get_rect()
        self.current_cell_adr = [7, 7]
        self.current_cell = field.cells[self.current_cell_adr[0]][self.current_cell_adr[1]]
        self.current_cell.withGhost = True
        self.moving_counter = 0
        self.current_cell.id = 0
        self.x = self.current_cell.rect.x
        self.y = self.current_cell.rect.y

    def logic(self):
        direction = random.randint(0, 1)
        if direction == 0:
            return [random.randint(-1, 1), 0]
        else:
            return [0, random.randint(-1, 1)]

    def move(self):
        global delay
        delay = 1
        if self.moving_counter == delay:
            direction = self.logic()
            if self.field.cells[(self.current_cell_adr[0] + direction[0]) % 15][
                (self.current_cell_adr[1] + direction[1]) % 15].id != 1:
                self.current_cell_adr = (
                    self.current_cell_adr[0] + direction[0], self.current_cell_adr[1] + direction[1])
                self.current_cell.withGhost = False
                self.current_cell = self.field.cells[(self.current_cell_adr[0]) % 15][(self.current_cell_adr[1]) % 15]
                self.current_cell.withGhost = True
                self.x = self.current_cell.rect.x
                self.y = self.current_cell.rect.y
                self.moving_counter = 0
        if self.moving_counter < delay:
            self.moving_counter += 1

    def selfprint(self):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.texture, self.rect)