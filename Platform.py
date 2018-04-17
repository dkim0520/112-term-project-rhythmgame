###Platform.py###
import pygame
import time
from GameObject import GameObject

class Platform(GameObject):
    @staticmethod
    def init():
        Platform.platformImage = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('images/bluesquare.svg').convert_alpha(),
                (50,25)), -90)

    def __init__(self, x, y):
        super(Platform, self).__init__(x, y, Platform.platformImage, 30)

    def update(self, keysDown, screenWidth, screenHeight):


        super(Platform, self).update(screenWidth, screenHeight)

