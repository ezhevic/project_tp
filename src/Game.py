import pygame
import sys
from Field import Field
from Hero import Hero

pygame.init()
size = width, height = 900, 500
screen = pygame.display.set_mode(size)
fieldposition = [startx, starty] = [200, 30]
horizontalcellcount = 15
verticalcellcount = 15
scale_factor = 3


class Game:
    def play():
        gameover = False
        field = Field(horizontalcellcount, verticalcellcount, fieldposition, scale_factor)
        field.selfgeneration()
        field.selfprint()
        mainhero = Hero(1, [11, 10], scale_factor, field)

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
                    mainhero.bufferredirect(direction)

            field.selfprint()
            mainhero.update()

            pygame.display.flip()
            pygame.time.wait(200)
        sys.exit()


    play()
