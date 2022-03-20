import pygame
import sys

size = width, height = 900, 500
pygame.init()
screen = pygame.display.set_mode(size)
FieldPosition = StartX, StartY = 200, 30
HorizontalCellCount = 15
VerticalCellCount = 15
scale_factor = 3

textures = (pygame.image.load('floor.jpg'), pygame.image.load('wall.jpg'))


class field():
    def __init__(self, HorizontalCellCount, VerticalCellCount, start_pos, scale_factor):
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.cells = []
        self.scale_factor = scale_factor
        self.HorizontalCellCount = HorizontalCellCount
        self.VerticalCellCount = VerticalCellCount

    def SelfGeneration(self):
        TempY = self.y
        TextureSplit = 0
        counter = 0
        map = []
        with open('map.txt', 'r') as f:
            for line in f:
                map.append([])
                print('')
                for letter in line:
                    if letter != '\n':
                        map[counter].append(int(letter))
                counter += 1
        for i in range(0, self.VerticalCellCount):
            self.cells.append([])
            TempX = self.x
            for j in range(0, self.HorizontalCellCount):
                temp_cell = Cell(textures[0], TempX, TempY, self.scale_factor, 0)
                if map[i][j] == 1:
                    temp_cell = Cell(textures[1], TempX, TempY, self.scale_factor, 1)
                self.cells[i].append(temp_cell)
                TempX = TempX + 10 * self.scale_factor + TextureSplit
            TempY = TempY + 10 * self.scale_factor + TextureSplit

    def SelfPrint(self):
        for x in range(0, len(self.cells)):
            for y in range(0, len(self.cells)):
                self.cells[x][y].SelfPrint()


class Cell():
    def __init__(self, texture, x, y, scale_factor, id):
        self.contaiment = None
        self.id = id
        self.scale_factor = scale_factor
        self.start_texture = texture
        self.texture = pygame.transform.scale(self.start_texture, (
            texture.get_rect().width * scale_factor, texture.get_rect().height * scale_factor))
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y
        try:
            self.contaiment = self.contaiment
        except:
            self.contaiment = []

    def AddContament(self, contaiment):
        self.contaiment += [contaiment]

    def Move(self, x, y):
        self.rect.x += x * self.scale_factor
        self.rect.y += y * self.scale_factor
        for i in self.contaiment:
            i.Move(x, y)

    def SelfPrint(self):
        screen.blit(self.texture, self.rect)


class Hero:
    def __init__(self, texture, start_cell_adress, scale_factor, field):
        self.field = field
        self.texture = texture
        self.scale_factor = scale_factor
        self.currentCellAdr = start_cell_adress
        self.currentCell = field.cells[start_cell_adress[0]][start_cell_adress[1]]
        self.x = self.currentCell.rect.x + 10 * scale_factor
        self.y = self.currentCell.rect.y + 2.5 * scale_factor
        self.height = 6 * scale_factor
        self.width = 6 * scale_factor
        self.current_direction = [0, 0]
        self.buffer_direction = [0, 0]
        self.isMoving = False
        self.MovingCounter = 0
        print(self.currentCellAdr)

    def Move(self):
        if self.field.cells[self.currentCellAdr[0] + self.current_direction[1]][
            self.currentCellAdr[1] + self.current_direction[0]].id != 1:
            self.currentCellAdr = [self.currentCellAdr[0] + self.current_direction[1],
                                   self.currentCellAdr[1] + self.current_direction[0]]
            print(self.currentCellAdr)
            self.currentCell = self.field.cells[self.currentCellAdr[0]][self.currentCellAdr[1]]
            self.isMoving = True
            if self.buffer_direction != [0, 0]:
                if self.field.cells[self.currentCellAdr[0] + self.buffer_direction[1]][
                    self.currentCellAdr[1] + self.buffer_direction[0]].id != 1:
                    if self.buffer_direction[0] != -1 * self.current_direction[0] or self.buffer_direction[1] != -1 * \
                            self.current_direction[1]:
                        self.current_direction = self.buffer_direction

        else:
            self.current_direction = self.buffer_direction

    def SelfPrint(self):
        pygame.draw.rect(screen, (255, 255, 0), (
            self.currentCell.rect.x + 2 * scale_factor, self.currentCell.rect.y + 2 * scale_factor, self.width,
            self.height))

    def BufferRedirect(self, direction):
        self.buffer_direction = direction

    def Update(self):
        self.Move()
        self.SelfPrint()


def main():
    gameover = False
    Field = field(HorizontalCellCount, VerticalCellCount, FieldPosition, scale_factor)
    Field.SelfGeneration()
    MainHero = Hero(1, [11, 10], scale_factor, Field)

    while not gameover:
        screen.fill((220, 200, 240))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                direction = [0, 0]
                if event.key == pygame.K_UP:
                    direction = [0, -1]
                if event.key == pygame.K_DOWN:
                    direction = [0, 1]
                if event.key == pygame.K_LEFT:
                    direction = [-1, 0]
                if event.key == pygame.K_RIGHT:
                    direction = [1, 0]
                MainHero.BufferRedirect(direction)

        # MainHero.Update()
        Field.SelfPrint()
        MainHero.Update()

        pygame.display.flip()
        pygame.time.wait(200)
    sys.exit()


main()