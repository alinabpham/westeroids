import sys,pygame
from pygame.locals import *
pygame.init()


size = width,height = 500,500
black = 0, 0, 0

screen = pygame.display.set_mode(size)

player = pygame.image.load("spaceship copy.png").convert()
player_rect = player.get_rect()

enemy = pygame.image.load("droid.png")
enemy_rect = enemy.get_rect()

background = pygame.image.load("galaxy1 copy.bmp")
background_rect = background.get_rect()

w,h = background.get_size()
x = 0
y = 0

x1 = 0
y1 = -h

while 1:
    screen.blit(background, background_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(player, player_rect)
    screen.blit(enemy, enemy_rect)

    y1 += 5
    y += 5
    screen.blit(background,(x,y))
    screen.blit(background,(x1,y1))
    if y > h:
        y = -h
    if y1 > h:
        y1 = -h


    pygame.display.update()
    pygame.display.flip()
