import sys, pygame
from pygame.locals import *

pygame.init()

WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.flip()

game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()