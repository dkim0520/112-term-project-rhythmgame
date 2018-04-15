###Character.py###
import pygame
from GameObject import GameObject

class Character(GameObject):
    @staticmethod
    def init():
        Character.characterImage = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('images/character.png').convert_alpha(),
                (50,50)), -90)

    def __init__(self, x, y):
        super(Character, self).__init__(x, y, Character.characterImage, 30)
        self.isAlive = True
        self.angle = 0
        self.isJump = False
        self.velocity = 0

    def update(self, keysDown, screenWidth, screenHeight):
        if keysDown(pygame.K_UP) and self.isJump == False:
            self.isJump = True
            self.velocity = 100

        super(Character, self).update(screenWidth, screenHeight)



