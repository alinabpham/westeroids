import sys,pygame
from pygame.locals import *
pygame.init()


size = width,height = 500,500
screen = pygame.display.set_mode(size)
black = 0,0,0
player = pygame.image.load("spaceship copy.png").convert()
player_rect = player.get_rect()
pygame.transform.scale(player, (10, 10))
background = pygame.image.load("galaxy1 copy.bmp").get_rect()



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #screen.fill(black)
    screen.blit(player, player_rect)

    pygame.display.flip()



# player = pygame.image.load("spaceship copy.bmp").convert()
# background = pygame.image.load("galaxy1 copy.bmp").convert()
# screen.blit(background, (0, 0))
