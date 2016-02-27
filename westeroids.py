import sys, pygame
pygame.init()

window(640,400)


screen = pygame.display.set_mode((640, 480))
player = pygame.image.load("spaceship copy.bmp").convert()
background = pygame.image.load("galaxy1 copy.bmp").convert()
screen.blit(background, (0, 0))
  
'''
img = loadImage("http://mvas.org/files/images/NGC%20253%20Sculptor%20Galaxy%20low%20res%20copy.preview.jpg")

bbg = image(img, 0, 0)
    

image(img, 0, 0)

'''

#LowerLeft
shipX1 = 190
shipY1 = 190
#Tip
shipX2 = 210
shipY2 = 200
#LowerRight
shipX3 = 190
shipY3 = 210

bulletX = shipX2
bulletY = shipY2

rotateRight = False
rotateLeft = False
bullet = False

#Time-Delta: To get time and multiply this with the rotation speed to make it consistent between frame rates
curtime = millis()
timeDelta = millis() - curtime
curtime = millis()

#Initial Rotation Angle
theta = 0 
rotationSpeed = 0.1

def ship():
    global shipX2, shipY2, shipX1, shipY1, shipX3, shipY3, rotateRight, rotateLeft, bullet, bulletX, bulletY
    
    #Movements
    if isKeyPressed():
        #Up
        if key() == "Up":
            shipY1 = shipY1 - 3
            shipY2 = shipY2 - 3
            shipY3 = shipY3 - 3
        #Back

        elif key() == "space" and bullet == False:
            bullet = True
            bulletX = shipX2
            bulletY = shipY2
        elif key() == "Left" and rotateLeft == False:
            rotateLeft = True
        elif key() == "Right" and rotateRight == False:
            rotateRight = True
      
        #Temporary Movements while figuring out how to use rotate
        #MoveLeft
        elif key() == "Left":
            shipX1 = shipX1 - 3
            shipX2 = shipX2 - 3
            shipX3 = shipX3 - 3
        #Forward
        elif key() == "Right":
            shipX1 = shipX1 + 3
            shipX2 = shipX2 + 3
            shipX3 = shipX3 + 3
        #Down
        elif key() == "Down":
            shipY1 = shipY1 + 3
            shipY2 = shipY2 + 3
            shipY3 = shipY3 + 3

       

        #Shooting Function
        elif key() == "space" and bullet == False:
            bullet = True
            bulletX = shipX2
            bulletY = shipY2

        
        
    #background(0)
    triangle(shipX1,shipY1,shipX2,shipY2,shipX3,shipY3)
    
    #Bullet Code
    if bullet:
        ellipse(bulletX, bulletY, 10, 10)
        bulletX += 10
        if bulletX > 410:

        ellipse(bulletX, bulletY, 5, 5)
        bulletY -= 10
        if bulletY < 10:
            bullet = False
          

frameRate(100)
onLoop += ship
loop()  
