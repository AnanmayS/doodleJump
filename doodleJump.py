import sys, pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 900))
pygame.display.set_caption("Jumper")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')

background_surface = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background_surface, (600, 900))

jumper_surface = pygame.image.load('jumper.png').convert_alpha()
jumper = pygame.transform.scale(jumper_surface, (50, 50))
jumper_rect = jumper.get_rect(midbottom = (300, 200))


platform_surface = pygame.image.load('platform.png').convert()
platform = pygame.transform.scale(platform_surface, (80, 10))
platform_rect = platform.get_rect(midtop = (300, 800))


game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(test_surface, (200,100))
    screen.blit(background, (0,0))  
    jumper_rect.y += 5
    screen.blit(jumper, jumper_rect)
    screen.blit(platform, platform_rect)
    ## Testing if Collsion Works (Currently Working)
    if platform_rect.colliderect(jumper_rect) == True:
        sys.exit()
    clock.tick(60)
    pygame.display.update()