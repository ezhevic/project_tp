import pygame
import sys
from Field import Field
from Hero import Hero
from Ghost import Ghost

pygame.init()
size = width, height = 900, 500
screen = pygame.display.set_mode(size)
fieldposition = [startx, starty] = [200, 30]
horizontalcellcount = 15
verticalcellcount = 15
scale_factor = 3
clock = pygame.time.Clock()
FPS = 30
isDead = False
ghost_texture = pygame.image.load('../animation/Red_Ghost.png')
pacman_r = (pygame.image.load('../animation/RightMoveAnimation0.png'), pygame.image.load('../animation/RightMoveAnimation1.png'), pygame.image.load('../animation/RightMoveAnimation2.png'))
pacman_l = (pygame.image.load('../animation/LeftMoveAnimation0.png'), pygame.image.load('../animation/LeftMoveAnimation1.png'), pygame.image.load('../animation/LeftMoveAnimation2.png'))
animation_list = (pacman_r, pacman_l)

class Game:
    def play():
        pygame.mixer.music.load('../animation/pacman_theme.mp3')
        pygame.mixer.music.play()
        gameover = False
        field = Field(horizontalcellcount, verticalcellcount, fieldposition, scale_factor)
        field.selfgeneration()
        mainhero = Hero([9, 10], field, animation_list)
        ghost = (Ghost(ghost_texture, field), Ghost(ghost_texture, field))

        while not gameover:
            screen.fill((220, 200, 240))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True
                if isDead:
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

            if not isDead:
                field.selfprint()
                mainhero.update()
                for i in ghost:
                    i.move()
                for i in ghost:
                    i.selfprint()

            pygame.display.flip()
            pygame.time.wait(20)
        sys.exit()

    play()