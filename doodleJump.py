import sys, pygame
from pygame.locals import *
import random   

pygame.init()
WIDTH = 400 
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumper")
clock = pygame.time.Clock()
white = (0,0,0)
GRAV = 1
PLATFORMS = 10

background_surface = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background_surface, (WIDTH, HEIGHT))

jumper_surface = pygame.image.load('jumper.png').convert_alpha()
jumper = pygame.transform.scale(jumper_surface, (50, 50))

platform_surface = pygame.image.load('platform.png').convert_alpha()


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_surface, (width, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player():
    def __init__(self, x, y):
        self.image = jumper
        self.width = 30
        self.height = 40
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.velY = 0
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
        if self.rect.right + dx > WIDTH:
            dx = WIDTH - self.rect.right

        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.rect.bottom < platform.rect.centery:
                    print(self.velY)
                    if self.velY > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.velY = -20

        self.velY += GRAV
        dy += self.velY
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom + dy > HEIGHT:
            dy = 0
            self.velY = -20

jumper = Player(WIDTH // 2, HEIGHT - 150)

platform_group = pygame.sprite.Group()

for i in range(PLATFORMS):
    plat_w = 60
    plat_x = random.randint(10, HEIGHT - plat_w)
    plat_y = i * random.randint(80, 120)
    platform = Platform(plat_x, plat_y, plat_w)
    platform_group.add(platform)


game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    jumper.key_handler()
    screen.blit(background, (0,0))  
    platform_group.draw(screen)
    jumper.draw()
    clock.tick(60)
    print(jumper.velY)
    pygame.display.update()