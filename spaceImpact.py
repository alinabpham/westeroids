import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 500, 240
speed = [2, 2]
BLACK = 0, 0, 0

screen = pygame.display.set_mode(size)

screen.fill(BLACK)

spaceship = pygame.image.load("deathstar.jpg")
