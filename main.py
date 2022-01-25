import pygame
import numpy
import math

DISPLAY_HEIGHT = 800
DISPLAY_WIDTH = DISPLAY_HEIGHT
BLOCKS = 15
MARGIN = 2

block_size = int((DISPLAY_HEIGHT - BLOCKS * MARGIN) / BLOCKS)

SPEED = 10

BLACK = (0, 0, 0)
GREY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = y = 0
neighbours = 0

x_dim = int(DISPLAY_HEIGHT / block_size)
y_dim = int(DISPLAY_WIDTH / block_size)

# initialize two array filled with zeros
block = numpy.zeros((x_dim, y_dim))
block_new = numpy.zeros((x_dim, y_dim))

pygame.init()

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH + MARGIN, DISPLAY_HEIGHT + MARGIN))
pygame.display.set_caption('Game of Life')
clock = pygame.time.Clock()

gameDisplay.fill(GREY)


def draw_rect():
    for y in range(0, y_dim):
        for x in range(0, x_dim):
            if block[y][x] == 1:
                pygame.draw.rect(gameDisplay, RED, (
                    x * block_size + x * MARGIN + MARGIN, y * block_size + y * MARGIN + MARGIN, block_size, block_size))
            if block[y][x] == 0:
                pygame.draw.rect(gameDisplay, BLACK, (
                    x * block_size + x * MARGIN + MARGIN, y * block_size + y * MARGIN + MARGIN, block_size, block_size))

    return 1


def check_life():
    for y in range(0, y_dim):
        for x in range(0, x_dim):
            neighbours = 0
            for count_y in range(-1, 2):
                for count_x in range(-1, 2):
                    if y + count_y < 0: continue
                    if x + count_x < 0: continue
                    if y + count_y == y_dim: continue
                    if x + count_x == x_dim: continue
                    if block[y + count_y][x + count_x] == 1:
                        neighbours += 1
            if block[y][x] == 0 and neighbours == 3:
                block_new[y][x] = 1
            if block[y][x] == 1 and neighbours == 1:
                block_new[y][x] = 0
            if block[y][x] == 1 and neighbours == 3:
                block_new[y][x] = 1
            if block[y][x] == 1 and neighbours == 4:
                block_new[y][x] = 1
            if block[y][x] == 1 and neighbours == 5:
                block_new[x][y] = 0
            if block[y][x] == 1 and neighbours == 2:
                block_new[y][x] = 0
    return 1


def manual_draw():
    pos = pygame.mouse.get_pos()
    create_x = math.ceil((pos[0] / (block_size + MARGIN)) - 1)
    create_y = math.ceil((pos[1] / (block_size + MARGIN)) - 1)
    if block[create_y][create_x] == 1:
        block[create_y][create_x] = 0
    else:
        block[create_y][create_x] = 1
    draw_rect()
    return


crashed = False
start = False
draw_rect()

pygame.display.update()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                gameDisplay.fill(GREY)
                block = numpy.random.randint(2, size=(x_dim, y_dim))
        if event.type == pygame.MOUSEBUTTONUP:
            manual_draw()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            start = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            start = False

    if start:
        check_life()
        block = block_new
        block_new = numpy.zeros((x_dim, y_dim))
        draw_rect()

    pygame.display.update()
    clock.tick(SPEED)

pygame.quit()
quit()
