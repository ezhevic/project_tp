from Character import CharacterInterface
import pygame

size = width, height = 900, 500
screen = pygame.display.set_mode(size)
loc_in_cell = 5


class Hero(CharacterInterface):
    def __init__(self, texture, start_cell_address, scale_factor, field):
        self.field = field
        self.texture = texture
        self.scale_factor = scale_factor
        self.current_cell_adr = start_cell_address
        self.current_cell = field.cells[start_cell_address[0]][start_cell_address[1]]
        self.x = self.current_cell.rect.x
        self.y = self.current_cell.rect.y
        self.height = 20
        self.width = 20
        self.current_direction = [0, 0]
        self.buffer_direction = [0, 0]
        self.ismoving = False
        self.movingcounter = 0
        self.isstart = True

    def move(self):
        if self.field.cells[self.current_cell_adr[0] + self.current_direction[1]][
            self.current_cell_adr[1] + self.current_direction[0]].id != 1:
            self.current_cell_adr = [self.current_cell_adr[0] + self.current_direction[1],
                                     self.current_cell_adr[1] + self.current_direction[0]]
            self.current_cell = self.field.cells[self.current_cell_adr[0]][self.current_cell_adr[1]]
            self.ismoving = True
            if self.buffer_direction != [0, 0]:
                if self.field.cells[self.current_cell_adr[0] + self.buffer_direction[1]][
                    self.current_cell_adr[1] + self.buffer_direction[0]].id != 1:
                    if self.buffer_direction[0] != -1 * self.current_direction[0] or self.buffer_direction[1] != -1 * \
                            self.current_direction[1]:
                        self.current_direction = self.buffer_direction
        else:
            self.current_direction = self.buffer_direction

    def selfprint(self):
        pygame.draw.rect(screen, (255, 255, 0),
                         (self.current_cell.rect.x + loc_in_cell, self.current_cell.rect.y + loc_in_cell, self.width, self.height))

    def bufferredirect(self, direction):
        self.buffer_direction = direction

    def update(self):
        self.move()
        self.selfprint()
