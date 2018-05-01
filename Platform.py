###Platform.py###
import pygame
from GameObject import GameObject

class Platform(GameObject):
    @staticmethod
    def init():
        Platform.platformImage = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('images/bluesquare.png').convert_alpha(),
                (20,50)), -90)

    def __init__(self, x, y, length, final = False):
        self.length = length
        self.final = final
        Platform.platformImage = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load('images/bluesquare.png').convert_alpha(),
            (25, length)), -90)

        if self.final == True:
            Platform.platformImage = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load('images/finalplatform.png').convert_alpha(),
            (25, length)), -90)
            self.final = final
        super(Platform, self).__init__(x, y, Platform.platformImage, 30)

    def update(self, keysDown, screenWidth, screenHeight):

        super(Platform, self).update(screenWidth, screenHeight)

