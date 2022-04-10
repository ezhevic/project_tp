from Character import CharacterInterface
import pygame

scale_factor = 3
size = width, height = 900, 500
screen = pygame.display.set_mode(size)


class Hero(CharacterInterface):
    def __init__(self, texture, start_cell_address, scale_factor, field):
        self.field = field
        self.texture = texture
        self.scale_factor = scale_factor
        self.currentcelladr = start_cell_address
        self.currentcell = field.cells[start_cell_address[0]][start_cell_address[1]]
        self.x = self.currentcell.rect.x + 10 * scale_factor
        self.y = self.currentcell.rect.y + 2.5 * scale_factor
        self.height = 6 * scale_factor
        self.width = 6 * scale_factor
        self.current_direction = [0, 0]
        self.buffer_direction = [0, 0]
        self.ismoving = False
        self.movingcounter = 0
        print(self.currentcelladr)


    def move(self):
        if self.field.cells[self.currentcelladr[0] + self.current_direction[1]][
            self.currentcelladr[1] + self.current_direction[0]].id != 1:
            self.currentcelladr = [self.currentcelladr[0] + self.current_direction[1],
                                   self.currentcelladr[1] + self.current_direction[0]]
            print(self.currentcelladr)
            self.currentcell = self.field.cells[self.currentcelladr[0]][self.currentcelladr[1]]
            self.ismoving = True
            if self.buffer_direction != [0, 0]:
                if self.field.cells[self.currentcelladr[0] + self.buffer_direction[1]][
                    self.currentcelladr[1] + self.buffer_direction[0]].id != 1:
                    if self.buffer_direction[0] != -1 * self.current_direction[0] or self.buffer_direction[1] != -1 * \
                            self.current_direction[1]:
                        self.current_direction = self.buffer_direction

        else:
            self.current_direction = self.buffer_direction

    def selfprint(self):
        pygame.draw.rect(screen, (255, 255, 0), (
            self.currentcell.rect.x + 2 * scale_factor, self.currentcell.rect.y + 2 * scale_factor, self.width,
            self.height))

    def bufferredirect(self, direction):
        self.buffer_direction = direction

    def update(self):
        self.move()
        self.selfprint()
