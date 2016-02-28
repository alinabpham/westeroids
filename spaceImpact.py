import sys, pygame, time, pygame.mixer, random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

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
player = pygame.image.load("spaceship_copy.bmp").convert()
player = pygame.transform.scale(player,(65,50))
player_rect = player.get_rect()
player_position = pygame.mouse.get_pos()
playerX = 100
playerY = 225

#load lives/hearts
lives = 3
life1 = pygame.image.load("heartbit.bmp").convert()
lives_rect = life1.get_rect()
life2 = pygame.image.load("heartbit.bmp").convert()
lives_rect = life2.get_rect()
life3 = pygame.image.load("heartbit.bmp").convert()
lives_rect = life3.get_rect()

getHit = False
def livesfunction():
    global lives
    global getHit
    if getHit:
            lives -= 1
    if lives == 2:
            screen.blit(life3, [25, 5]) == False
    if lives == 1:
            screen.blit(life3, [25, 5]) == False
            screen.blit(life2, [15, 5]) == False
    if lives == 0:
            screen.blit(life3, [25, 5]) == False
            screen.blit(life2, [15, 5]) == False
            screen.blit(life1, [5, 5]) == False
            #Print "Game Over"
            #ont = pygame.font.Font(None, 36)
            #text = font.render("Game Over, Sucker!", 1, (10, 10, 10))
            #textpos = text.get_rect()
            #textpos.centerx = background.get_rect().centerx
            #background.blit(text, textpos)


#Sounds
soundtrack = pygame.mixer.Sound("soundtrack.wav")
pew = pygame.mixer.Sound("laser.wav")
explode_droid = pygame.mixer.Sound("explosion.wav")
gameover = pygame.mixer.Sound("game_over.wav")

#play soundtrack
soundtrack.play()

#Bullet
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super(Bullet, self).__init__()

        self.image = pygame.image.load("laser.bmp").convert()
        self.rect = self.image.get_rect()
        self.rect.x = playerX+50
        self.rect.y = playerY+22

    def update(self):
        """ Move the bullet. """
        self.rect.x += 10

#Load droid enemy image
class Enemy(pygame.sprite.Sprite):
    """ This class respresents the enemy """
    def __init__(self):
        super(Enemy, self).__init__()

        self.image = pygame.image.load("droid.bmp").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 250

    def update(self):
        """Move droid"""
        self.rect.x -= 2



#Load background image
background = pygame.image.load("galaxy1_copy_converted.bmp").convert()
background_rect = background.get_rect()
background2 = pygame.image.load("galaxy1_copy_converted.bmp").convert()

#get background size
w,h = background.get_size()
x = 0

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
# List of each bullet
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()



def newdroids1():
        space = random.randrange(50,450)
        enemy = Enemy()
        enemy.rect.x = 500
        enemy.rect.y = random.randrange(space)
        enemy_list.add(enemy)
        all_sprites_list.add(enemy)

global enemy_move
enemy_move = 20







while True:
    for event in pygame.event.get():
        #Clicking exit will quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Reloads photo everytime player moves
        if event.type == KEYDOWN:
            if (event.key == K_LEFT):
                sprite = pygame.image.load('spaceship_copy.bmp')
            elif (event.key == K_RIGHT):
                sprite = pygame.image.load('spaceship_copy.bmp')
            elif (event.key == K_UP):
                sprite = pygame.image.load('spaceship_copy.bmp')
            elif (event.key == K_DOWN):
                sprite = pygame.image.load('spaceship_copy.bmp')
            elif (event.key == K_SPACE):
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                pew.play()
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)



    # Call the update() method on all the sprites
    all_sprites_list.update()

    # Calculate mechanics for each bullet
    for bullet in bullet_list:
        # See if it hit a block
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
        # For each block hit, remove the bullet and add to the score
        for enemy in enemy_hit_list:
            explode_droid.play()
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
        # Remove the bullet if it flies up off the screen
        '''
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
        '''
    '''
    ship_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
    for enemy in enemy_hit_list:
        explode_droid.play()
    '''
    for enemy in enemy_list:
        if playerX == enemy.rect.x:
            gameover.play()
            playerX = 100
            playerY = 225
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            getHit = True
            livesfunction()

        #bullet_list.remove(bullet)
        #all_sprites_list.remove(bullet)

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
    #screen.blit(enemy, [enemyX, enemyY])
<<<<<<< Updated upstream
    
    #Puts lives on screen
    """
    #Waiting for getHit function
    if getHit:
        lives -= 1
        """
    if lives == 3:
        screen.blit(life3, [25, 5])
        screen.blit(life2, [15, 5])
        screen.blit(life1, [5, 5])
    elif lives == 2:
        screen.blit(life2, [15, 5])
        screen.blit(life1, [5, 5])
    elif lives == 1:
        screen.blit(life1, [5, 5])
    elif lives == 0:
        #Print "Game Over"
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over, Sucker!", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)

=======
    #puts lives on screen
    screen.blit(life1, [5, 5])
    screen.blit(life2, [15, 5])
    screen.blit(life3, [25, 5])
>>>>>>> Stashed changes
    # Draw all the sprites
    all_sprites_list.draw(screen)
    #draws enemies
    if enemy_move % 30== 0:
        newdroids1()
    enemy_move += 1
    pygame.display.update()
    pygame.display.flip()
