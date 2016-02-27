import math
from Processing import *

window(400,400)

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
        elif key() == "Left" and rotateLeft == False:
            rotateLeft = True
        elif key() == "Right" and rotateRight == False:
            rotateRight = True
        '''
        
        
    background(0)
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
        ellipse(bulletX, bulletY, 20, 20)
        bulletY -= 10
        if bulletY < 10:
            bullet = False
        
        



   
frameRate(100)
onLoop += ship
loop()  