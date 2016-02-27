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



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    #Puts background in screen
    screen.blit(background, [0,0])
    #Puts player in screen
    screen.blit(player, player_rect)
    #Puts enemy in screen
    screen.blit(enemy, enemy_rect)

    pygame.display.flip()
