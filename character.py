###Character.py###
import pygame
import time
from GameObject import GameObject

class Character(GameObject):
    @staticmethod
    def init():
        Character.characterImage = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('images/character.png').convert_alpha(),
                (25,25)), -90)

    def __init__(self, x, y):
        super(Character, self).__init__(x, y, Character.characterImage, 30)
        self.isAlive = True
        self.angle = 0
        self.isJump = False
        self.velocity = 0
        self.dy = 1
        self.gF = 0

    def update(self, keysDown, screenWidth, screenHeight):
        if self.isJump:
            self.gF = 0.5 * self.velocity**2
            self.velocity -= self.dy
            self.y -= self.height/3
            if self.y < screenHeight/2 - 10: 
                self.y += self.gF
                self.angle -= 4.1
            elif self.y > screenHeight//2:
                self.velocity = 0
                self.y = screenHeight//2
                self.isJump = False
                self.angle = 90
            self.updateRect()

        if keysDown(pygame.K_UP) and self.isJump == False:
            self.isJump = True
            self.velocity = 5

        if keysDown(pygame.K_LEFT):
            self.x -= 20

        if keysDown(pygame.K_RIGHT):
            self.x += 20

        super(Character, self).update(screenWidth, screenHeight)




