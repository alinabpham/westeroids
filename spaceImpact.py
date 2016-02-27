import sys,pygame
from pygame.locals import *
pygame.init()


size = width,height = 500,500
black = 0, 0, 0

screen = pygame.display.set_mode(size)
black = 0,0,0

player = pygame.image.load("spaceship copy.png")
pygame.transform.scale(player, (10, 10))
player_rect = player.get_rect()

enemy = pygame.image.load("droid.png")
enemy_rect = enemy.get_rect()
background = pygame.image.load("galaxy1 copy.bmp").get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(player, player_rect)
    screen.blit(enemy, enemy_rect)

    pygame.display.flip()
