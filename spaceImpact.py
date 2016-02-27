import sys,pygame
from pygame.locals import *
pygame.init()


size = width,height = 500,500
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#Player Spaceship
player = pygame.image.load("spaceship copy.png")
pygame.transform.scale(player, (10, 10))
player_rect = player.get_rect()

#Droid Enemy
enemy = pygame.image.load("droid.png")
enemy_rect = enemy.get_rect()

#Background
background = pygame.image.load("galaxy1 copy.bmp").convert()



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(background, [0,0])
    screen.blit(player, player_rect)
    screen.blit(enemy, enemy_rect)

    pygame.display.flip()
