import sys, pygame, time, pygame.mixer
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

'''
bulletUsed = False
bullet = pygame.image.load("laser.png").convert()
bullet_rect = bullet.get_rect()

bulletX = 0
bulletY = 0
# List of each bullet
bullet_list = []
#Bullet sound
bullet_sound = pygame.mixer.Sound("")
#bullet_sound.play() <- command to play comes later on
'''
#Bullet try
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super(Bullet, self).__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.rect = self.image.get_rect()
    def update(self):
        """ Move the bullet. """
        self.rect.x +=5

# List of each bullet
bullet_list = pygame.sprite.Group()

#Load droid enemy image
enemy = pygame.image.load("droid.png").convert()
enemy_rect = enemy.get_rect()
enemyX = 500
enemyY = 200

#Load background image
background = pygame.image.load("galaxy1 copy.bmp").convert()
background_rect = background.get_rect()
background2 = pygame.image.load("galaxy1 copy.bmp").convert()

#get background size
w,h = background.get_size()
x = 0

# List of each bullet
bullet_list = pygame.sprite.Group()



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
            elif (event.key == K_SPACE):
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = player_rect.x
                bullet.rect.y = player_rect.y
                # Add the bullet to the lists
                #all_sprites_list.add(bullet)
                bullet_list.add(bullet)

        '''
        #Does event when key is lifted up
        if event.type == KEYUP:
            if (event.key == K_SPACE):
                # Set the bullet so it is where the player is
                shoot_rect.x = player_rect.x
                shoot_rect.y = player_rect.y
                bullets.append([shoot_rect.x,shoot_rect.y])


                #bullet+sound.play() plays bullet sound
                #bulletX = (playerX+100)
                #bulletY = (playerY+50)
                #pew = pygame.draw.circle(screen, yellow, (bulletX,bulletY),10, 5)
        '''
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
    #if keys_pressed[K_SPACE]:
        #shoot_rect.y -= 3

    #Prevents ship from going out of frame

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
    screen.blit(enemy, [enemyX, enemyY])



    pygame.display.update()
    pygame.display.flip()
