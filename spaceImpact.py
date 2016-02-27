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

screen = pygame.display.set_mode(size)

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

#get background size
w,h = background.get_size()
x = 0
y = 0

x1 = -w
y1 = 0

while 1:
    for event in pygame.event.get():
        #Clicking exit will quit the game
        if event.type == pygame.QUIT: sys.exit()
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
    screen.blit(background, [0,0])
    #Scrolling background image
    x1 -= 1
    x -= 1
    screen.blit(background,(x,y))
    screen.blit(background,(x1,y1))
    if x > w:
        x = -w
    if x1 > w:
        x1 = -w
    #Puts player in screen
    screen.blit(player, [playerX, playerY])
    #Puts enemy in screen
    screen.blit(enemy, enemy_rect)











    pygame.display.update()
    pygame.display.flip()
