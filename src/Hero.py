import os
import sys

from Character import CharacterInterface
import pygame

size = width, height = 900, 500
screen = pygame.display.set_mode(size)
pacman_r = (
    pygame.image.load('../animation/RightMoveAnimation0.png'),
    pygame.image.load('../animation/RightMoveAnimation1.png'),
    pygame.image.load('../animation/RightMoveAnimation2.png'))
pacman_l = (
    pygame.image.load('../animation/LeftMoveAnimation0.png'), pygame.image.load('../animation/LeftMoveAnimation1.png'),
    pygame.image.load('../animation/LeftMoveAnimation2.png'))
pacman = (pacman_r, pacman_l)
delay = 5
hor_location = 8
vert_location = 5
loc_in_cell = 5
lives = 1


class Hero(CharacterInterface):
    def __init__(self, start_cell_address, field, pacman):
        self.field = field
        self.pacman = pacman
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
        self.animation_id = 0
        self.isstart = True
        self.score = 0
        self.animation = pygame.transform.scale(self.pacman[0][self.animation_id], (
            self.pacman[0][self.animation_id].get_rect().width,
            self.pacman[0][self.animation_id].get_rect().height))

    def move(self):
        if self.field.cells[self.current_cell_adr[0] + self.current_direction[1]][
            self.current_cell_adr[1] + self.current_direction[0]].id == 0:
            self.current_cell_adr = [self.current_cell_adr[0] + self.current_direction[1],
                                     self.current_cell_adr[1] + self.current_direction[0]]
            self.current_cell = self.field.cells[self.current_cell_adr[0]][self.current_cell_adr[1]]
            if self.current_cell.withdot:
                self.score += 1
                self.current_cell.withdot = False
            self.ismoving = True
            if self.buffer_direction != [0, 0]:
                if self.field.cells[self.current_cell_adr[0] + self.buffer_direction[1]][
                    self.current_cell_adr[1] + self.buffer_direction[0]].id != 1:
                    if self.buffer_direction[0] != -1 * self.current_direction[0] or self.buffer_direction[1] != -1 * \
                            self.current_direction[1]:
                        self.current_direction = self.buffer_direction
        else:
            self.current_direction = self.buffer_direction

        nick = 111
        f1 = pygame.font.Font(None, 30)
        Text = "Score:" + str(self.score)
        text1 = f1.render(Text, 1, (0, 0, 0))
        screen.blit(text1, (750, 400))
        Text = "Your nickname:" + str(nick)
        text2 = f1.render(Text, 1, (0, 0, 0))
        screen.blit(text2, (700, 300))
        Text = "Lives: " + str(lives)
        text3 = f1.render(Text, 1, (0, 0, 0))
        screen.blit(text3, (750, 350))
        pygame.time.wait(34)
        if self.score == 106:
            pygame.mixer.music.load('../animation/WinSound.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(2700)
            print("You won! Your score:", str(self.score))
            python = sys.executable
            os.execl(python, python, *sys.argv)

    def selfprint(self):
        pygame.draw.rect(screen, (255, 255, 0),
                         (self.current_cell.rect.x + loc_in_cell, self.current_cell.rect.y + loc_in_cell, self.width,
                          self.height))

    def bufferredirect(self, direction):
        self.buffer_direction = direction

    def update(self):
        if self.current_cell.withGhost:
            global isDead
            pygame.mixer.music.load('../animation/DeadSound.mp3')
            pygame.mixer.music.play()
            isDead = True
            print('DEAD')
            pygame.time.wait(1000)
            print("Your score:", str(self.score))
            sys.exit()

        self.move()
        self.selfprint()
