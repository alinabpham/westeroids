import sys,pygame
from pygame.locals import *
pygame.init()


size = width,height = 500,500
black = 0, 0, 0

screen = pygame.display.set_mode(size)
<<<<<<< Updated upstream
black = 0,0,0
player = pygame.image.load("spaceship copy.png").convert()
=======

player = pygame.image.load("spaceship copy.bmp").convert()
pygame.transform.scale(player, (10, 10))
>>>>>>> Stashed changes
player_rect = player.get_rect()
background = pygame.image.load("galaxy1 copy.bmp").convert().get_rect()



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(player, player_rect)

    pygame.display.flip()



# player = pygame.image.load("spaceship copy.bmp").convert()
# background = pygame.image.load("galaxy1 copy.bmp").convert()
# screen.blit(background, (0, 0))
