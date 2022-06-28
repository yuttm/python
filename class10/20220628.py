import pygame
import sys
import math

pygame.init()  #啟動pygame
screen = pygame.display.set_mode((1000, 800))
width, heigh = screen.get_size()
bg = pygame.Surface(screen.get_size())
bg.fill((227, 158, 93))
pygame.display.set_caption("my game")
sw = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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

    #pygame.draw.arc(bg, (255, 10, 0), [100, 100, 100, 50], math.radians(180),math.radians(0), 2)
    pygame.display.update()
