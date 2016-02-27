import math
from Processing import *

window(625,400)

img = loadImage("http://mvas.org/files/images/NGC%20253%20Sculptor%20Galaxy%20low%20res%20copy.preview.jpg")
image(img, 0, 0)

'''
xAstLoc = 0
xAstSpeed = 1
yAstLoc = 25
yAstSpeed = 5
def asteroids():
    global xAstLoc
    global xAstSpeed
    global yAstLoc
    global yAstSpeed
    fill(0, 255, 150)
    ellipse(xAstLoc, yAstLoc, 25, 25)
    
    xAstLoc = xAstLoc + xAstSpeed
    yAstLoc = yAstLoc + yAstSpeed
   
    if xAstLoc < 0:
        xAstSpeed = 1
    elif xAstLoc > 387.5:
        xAstSpeed = -1
    if yAstLoc > 0:
        yAstSpeed = -yAstSpeed
    elif (yAstLoc > 350) and (xAstLoc < mouseX()-75 or 
    xAstLoc > (mouseX()+75)):
        xAstSpeed = xAstSpeed
        yAstSpeed = yAstSpeed
        if yAstLoc > 425:
            endGame()
    else: 
        xAstSpeed = -xAstSpeed
        yAstSpeed = -yAstSpeed
        
frameRate(100)
onLoop += asteroids
loop()
'''

#LowerLeft
shipX1 = 210
shipY1 = 215
#Tip
shipX2 = 200
shipY2 = 185
#LowerRight
shipX3 = 190
shipY3 = 215

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
    global shipX1, shipY1, shipX2, shipY2, shipX3, shipY3, rotateRight, rotateLeft, bullet, bulletX, bulletY
    
    #Movements
    if isKeyPressed():
        #MoveForward
        if key() == "Up":
            shipY1 = shipY1 - 3
            shipY2 = shipY2 - 3
            shipY3 = shipY3 - 3
        elif key() == "space" and bullet == False:
            bullet = True
            bulletX = shipX2
            bulletY = shipY2
        elif key() == "Left" and rotateLeft == False:
            rotateLeft = True
        elif key() == "Right" and rotateRight == False:
            rotateRight = True
        '''
        #Temporary Movements while figuring out how to use rotate
        #MoveLeft
        elif key() == "Left":
            shipX1 = shipX1 - 3
            shipX2 = shipX2 - 3
            shipX3 = shipX3 - 3
        #MoveRight
        elif key() == "Right":
            shipX1 = shipX1 + 3
            shipX2 = shipX2 + 3
            shipX3 = shipX3 + 3
        #MoveBack
        elif key() == "Down":
            shipY1 = shipY1 + 3
            shipY2 = shipY2 + 3
            shipY3 = shipY3 + 3
        '''
        
        
    #background(0)
    triangle(shipX1,shipY1,shipX2,shipY2,shipX3,shipY3)
    
    #RotateLeft     
    if rotateLeft:
        '''
        popMatrix()
        background(0)
        rotate(radians(theta + (rotationSpeed * timeDelta)))
        translate(200,207.5)
        triangle(-10, 7.5, 0, -7.5, 10, 7.5)
        pushMatrix()
        rotateLeft = False
        '''
    if rotateRight:
        '''
        popMatrix()
        background(0)
        rotate(radians(theta + (rotationSpeed * timeDelta)))
        translate(200,207.5)
        triangle(-10, 7.5, 0, -7.5, 10, 7.5)
        pushMatrix()
        rotateRight = False
        '''
    if bullet: 
        ellipse(bulletX, bulletY, 5, 5)
        bulletY -= 10
        if bulletY < 10:
            bullet = False
        
        



   
frameRate(100)
onLoop += ship
loop()  
