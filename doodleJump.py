import sys, pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 900))
pygame.display.set_caption("Jumper")
clock = pygame.time.Clock()
white = (0,0,0)
background_surface = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background_surface, (600, 900))

jumper_surface = pygame.image.load('jumper.png').convert_alpha()
jumper = pygame.transform.scale(jumper_surface, (50, 50))

platform_surface = pygame.image.load('platform.png').convert()
platform = pygame.transform.scale(platform_surface, (80, 10))

class Player():
    def __init__(self, x, y):
        self.image = jumper
        self.width = 30
        self.height = 40
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = (x, y)
        self.flip = False

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 7, self.rect.y - 5))
        pygame.draw.rect(screen, white, self.rect, 2)

    def key_handler(self):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            dx = -10
            self.flip = True
        if key[pygame.K_d]:
            dx = 10
            self.flip = False

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > 600:
            dx = 600 - self.rect.right

        self.rect.x += dx
        self.rect.x += dy



jumper = Player(600 // 2, 900 - 150)

game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    jumper.key_handler()
    screen.blit(background, (0,0))  
    jumper.draw()
    clock.tick(60)
    pygame.display.update()