import pygame, sys
from pygame.locals import *

pygame.init()
soundObj = pygame.mixer.Sound('beep.wav')
soundObj.play()
import time
time.sleep(1)
soundObj.stop()