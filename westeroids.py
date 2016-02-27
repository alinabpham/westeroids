import math
from Processing import *

window(400,400)

img = loadImage("http://mvas.org/files/images/NGC%20253%20Sculptor%20Galaxy%20low%20res%20copy.preview.jpg")
image(img, 400, 400)

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
        
    background(0)
    triangle(shipX1,shipY1,shipX2,shipY2,shipX3,shipY3)
    
    #Bullet Code
    if bullet: 
        ellipse(bulletX, bulletY, 10, 10)
        bulletX += 10
        if bulletX > 410:
            bullet = False
        
        



   
frameRate(100)
onLoop += ship
loop()  
