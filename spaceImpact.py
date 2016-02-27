import sys, pygame, time
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

size = width,height = 500,500
black = 0, 0, 0

#Keys
UP = 'up'
LEFT='left'
RIGHT='right'
DOWN='down'

screen = pygame.display.set_mode(size, 0, 32)

#load player spaceship
player = pygame.image.load("spaceship copy.png").convert()
player_rect = player.get_rect()
player_position = pygame.mouse.get_pos()
playerX = player_position[0]
playerY = player_position[1]

#Load droid enemy image
enemy = pygame.image.load("droid.png").convert()
enemy_rect = enemy.get_rect()

#Load background image
background = pygame.image.load("galaxy1 copy.bmp").convert()
background_rect = background.get_rect()
background2 = pygame.image.load("galaxy1 copy.bmp").convert()

#get background size
w,h = background.get_size()
x = 0

while True:
    for event in pygame.event.get():
        #Clicking exit will quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Reloads photo everytime player moves
        if event.type == KEYDOWN:
            if (event.key == K_LEFT):
                sprite=pygame.image.load('spaceship copy.png')
            elif (event.key == K_RIGHT):
                sprite=pygame.image.load('spaceship copy.png')
            elif (event.key == K_UP):
                sprite=pygame.image.load('spaceship copy.png')
            elif (event.key == K_DOWN):
                sprite=pygame.image.load('spaceship copy.png')

    keys_pressed = pygame.key.get_pressed()
    #Player Movements
    if keys_pressed[K_LEFT]:
        playerX -= 5
    if keys_pressed[K_RIGHT]:
        playerX += 5
    if keys_pressed[K_UP]:
        playerY -= 5
    if keys_pressed[K_DOWN]:
        playerY += 5

    screen.fill(black)
    #Puts background in screen
    #screen.blit(background, [0,0])

    #Scrolling background image
    screen.blit(background, (x,0))
    screen.blit(background2,(x+w,0))
    x = x - 5
    if x == (-w):
        x = 0
    msElapsed = fpsClock.tick(100)

    #Puts player in screen
    screen.blit(player, [playerX, playerY])
    #Puts enemy in screen
    screen.blit(enemy, enemy_rect)

    pygame.display.update()
    pygame.display.flip()
