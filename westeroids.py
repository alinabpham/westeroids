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

