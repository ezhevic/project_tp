from Cell import Cell
import pygame

textures = [pygame.image.load('../animation/floor.jpeg'), pygame.image.load('../animation/wall.jpeg'), pygame.image.load(
    '../animation/wall3.png'), pygame.image.load('../animation/floor.jpeg')]
Dot_Texture = pygame.image.load('../animation/coin.png')


class Field:
    def __init__(self, horizontalcellcount, verticalcellcount, start_pos, scale_factor):
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.cells = []
        self.scale_factor = scale_factor
        self.horizontalcellcount = horizontalcellcount
        self.verticalcellcount = verticalcellcount

    def selfgeneration(self):
        tempy = self.y
        field_scale = 30
        counter = 0
        map = []
        with open('../map.txt', 'r') as f:
            for line in f:
                map.append([])
                for letter in line:
                    if letter != '\n':
                        map[counter].append(int(letter))
                counter += 1

        for i in range(0, self.verticalcellcount):
            self.cells.append([])
            tempx = self.x
            for j in range(0, self.horizontalcellcount):
                temp_cell = Cell(textures[0], tempx, tempy, self.scale_factor, 0, Dot_Texture)
                if map[i][j] == 1:
                    temp_cell = Cell(textures[1], tempx, tempy, self.scale_factor, 1, Dot_Texture)
                if map[i][j] == 2:
                    temp_cell = Cell(textures[2], tempx, tempy, self.scale_factor, 2, Dot_Texture)
                if map[i][j] == 3:
                    temp_cell = Cell(textures[3], tempx, tempy, self.scale_factor, 3, Dot_Texture)
                self.cells[i].append(temp_cell)
                tempx = tempx + field_scale
            tempy = tempy + field_scale

    def selfprint(self):
        for x in range(0, len(self.cells)):
            for y in range(0, len(self.cells)):
                self.cells[x][y].selfprint()
