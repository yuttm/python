import pygame
import sys
import math


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


BLACK = (0, 0, 0)
pygame.init()  #啟動pygame
screen = pygame.display.set_mode((1000, 800))
width, heigh = screen.get_size()
bg = pygame.Surface(screen.get_size())
bg.fill((227, 158, 93))
pygame.display.set_caption("my game")
sw = True

typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render('Start', True, BLACK)
tit_w = title.get_width()
tit_h = title.get_height()


def display_font(win):
    win.blit(title, (0, 0))


while True:
    mouse_pose = pygame.mouse.get_pos()
    print(mouse_pose)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if check_click(mouse_pose, 0, 0, tit_w, tit_h):
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            sw = not (sw)
    if sw:
        screen.blit(bg, (0, 0))
        pygame.draw.polygon(bg, (100, 200, 45),
                            [[100, 100], [0, 200], [200, 200]], 0)
        pygame.draw.circle(bg, (20, 20, 200), (100, 130), 10, 0)
        pygame.draw.rect(bg, (100, 0, 177), [150, 70, 80, 40], 2)
        pygame.draw.ellipse(bg, (100, 0, 177), [100, 115, 60, 40], 2)
        pygame.draw.line(bg, (20, 20, 200), (200, 100), (310, 220), 5)
    else:
        bg.fill((227, 158, 93))
        screen.blit(bg, (0, 0))
        display_font(screen)

    #pygame.draw.arc(bg, (255, 10, 0), [100, 100, 100, 50], math.radians(180),math.radians(0), 2)
    pygame.display.update()
