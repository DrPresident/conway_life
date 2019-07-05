import pygame
from random import randint, seed
from time import time

pygame.init()

size = (300, 300)
tile_size = 4
grid_size = (size[0] // tile_size, size[1] // tile_size)
tick_rate = 3

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Conway')

DEAD  = 0
ALIVE = 1

COLORS = [ (0, 0, 0), (0, 150, 0) ]

grid = [ [ [DEAD, DEAD] for x in range(grid_size[0]) ] for y in range(grid_size[1]) ]

# will determine the current and nxt
current = 0
nxt = 1

seed(time())

# STARTUP
for x in range(grid_size[0]):
    for y in range(grid_size[1]):
        if x and y and x < size[0] and y < size[1]:
            grid[x][y][current] = randint(DEAD, ALIVE)


def tick(x, y):
    life = 0

    for a in range(x - 1, x + 2):
        for b in range(y - 1, y + 2):
            if a == x and b == y:
                continue
            if grid[a][b][current] == ALIVE:
                life += 1

    if life < 2 or life > 3:
        grid[x][y][nxt] = DEAD

    elif grid[x][y][current] == ALIVE and (life == 2 or life == 3):
        grid[x][y][nxt] = ALIVE

    elif grid[x][y][current] == DEAD and life == 3:
        grid[x][y][nxt] = ALIVE

    pygame.draw.rect(screen, COLORS[grid[x][y][nxt]],
                     (x * tile_size, y * tile_size, tile_size, tile_size))

clock = pygame.time.Clock()
done = False

# iterate
while not done:

    clock.tick(tick_rate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # tick loop
    for x in range(1, grid_size[0] - 1):
        for y in range(1, grid_size[1] - 1):
            tick(x, y)

    """
    # apply nxt stage and draw
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            grid[x][y][0] = grid[x][y][1]
            pygame.draw.rect(screen, COLORS[grid[x][y][0]],
                             (x * tile_size, y * tile_size, tile_size, tile_size))
    """
    current, nxt = nxt, current
    pygame.display.flip()


