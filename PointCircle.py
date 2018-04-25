###Point Circles
import pygame
from GameObject import GameObject

class PointCircle(GameObject):
    @staticmethod
    def init():
        PointCircle.pointCircleImage = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('images/pointcircle.png').convert_alpha(),
                (25,25)), -90)

    def __init__(self, x, y):
        PointCircle.pointCircleImage = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('images/pointcircle.png').convert_alpha(),
                (25,25)), -90)
        super(PointCircle, self).__init__(x, y, PointCircle.pointCircleImage, 25)

    def update(self, keysDown, screenWidth, screenHeight):

        super(PointCircle, self).update(screenWidth, screenHeight)
