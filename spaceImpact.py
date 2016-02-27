import sys,pygame
from pygame.locals import *
pygame.init()


size = width,height = 500,500
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#load player spaceship
player = pygame.image.load("spaceship copy.png")
pygame.transform.scale(player, (10, 10))
player_rect = player.get_rect()

#Load droid enemy image
enemy = pygame.image.load("droid.png")
enemy_rect = enemy.get_rect()

#Load background image
background = pygame.image.load("galaxy1 copy.bmp").convert()
background_rect = background.get_rect()

w,h = background.get_size()
x = 0
y = 0

x1 = 0
y1 = -h

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    #Puts background in screen
    screen.blit(background, [0,0])
    y1 += 1
    y += 1
    screen.blit(background,(x,y))
    screen.blit(background,(x1,y1))
    if y > h:
        y = -h
    if y1 > h:
        y1 = -h
    #Puts player in screen
    screen.blit(player, player_rect)
    #Puts enemy in screen
    screen.blit(enemy, enemy_rect)

    pygame.display.update()
    screen.blit(player, player_rect)
    screen.blit(enemy, enemy_rect)

    pygame.display.flip()
