import sys, pygame, time
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

size = width,height = 500,483
black = 0, 0, 0
yellow = 255,255,0

#Creats a 500 by 483 screen
screen = pygame.display.set_mode(size, 0, 32)

#Names the window "Nokia Wesleyan"
pygame.display.set_caption('WeSteroids')

#load player spaceship
player = pygame.image.load("spaceship copy.png").convert()
player = pygame.transform.scale(player,(65,50))
player_rect = player.get_rect()
player_position = pygame.mouse.get_pos()
playerX = 100
playerY = 225

#Bullet
bullet = False
bulletX = 0
bulletY = 0
#Bullet sound
bullet_sound = pygame.mixer.Sound("")
#bullet_sound.play() <- command to play comes later on

#Load droid enemy image
enemy = pygame.image.load("droid.png").convert()
enemyX = 500
enemyY = 200

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
                sprite = pygame.image.load('spaceship copy.png')
            elif (event.key == K_RIGHT):
                sprite = pygame.image.load('spaceship copy.png')
            elif (event.key == K_UP):
                sprite = pygame.image.load('spaceship copy.png')
            elif (event.key == K_DOWN):
                sprite = pygame.image.load('spaceship copy.png')
            elif (event.key == K_SPACE) and bullet == False:
                #bullet+sound.play() plays bullet sound
                bulletX = (playerX+100)
                bulletY = (playerY+50)
                pew = pygame.draw.circle(screen, yellow, (bulletX,bulletY),10, 5)
    #Bullet still not working!!!
    '''
    if bullet:
        pew = pygame.image.load('spaceship copy.png')
        bulletX += 15
        if bulletX > 500:
            bullet = False
    '''
    screen.fill(black)

    keys_pressed = pygame.key.get_pressed()
    #Player Movements and Boundaries
    if keys_pressed[K_LEFT] and playerX > 0:
        playerX -= 10
    if keys_pressed[K_RIGHT] and playerX < 350:
        playerX += 10
    if keys_pressed[K_UP] and playerY > 0:
        playerY -= 10
    if keys_pressed[K_DOWN] and playerY < 430:
        playerY += 10

    #Prevents ship from going out of frame

    #Scrolling background image
    bbg = screen.blit(background, (x,0))
    bbg = screen.blit(background2,(x+w,0))
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
