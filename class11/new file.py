import pygame
import sys
import random

pygame.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()

bg_x = 500
bg_y = 400
screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("打地鼠")

sur = pygame.Surface([bg_x, bg_y])

pos6 = [[200, 200], [300, 200], [400, 200], [200, 300], [300, 300], [400, 300]]

tick = 0
max_tick = 10
pos = pos6[0]


def gophers_update(win):
    global tick, pos
    if tick > max_tick:
        new_pos = random.randint(0, 5)
        pos = pos6[new_pos]
        tick = 0
    else:
        tick += 1
    pygame.draw.circle(sur, BLUE, pos, 50)


def screen_update(win):
    win.blit(sur, (0, 0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys, exit()
    sur.fill(BLACK)
    gophers_update(screen)
    screen_update(screen)

    clock.tick(30)
    pygame.display.update()
