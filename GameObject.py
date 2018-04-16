###GameObject Class###
#Framework inspired by Lukas Peraza#

import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, radius):
        super(GameObject, self).__init__()
        self.x, self.y, self.image, self.radius = x, y, image, radius
        self.baseImage = image.copy()
        w, h = image.get_size()
        self.updateRect()
        self.scroll = (-10, 0)
        self.velocity = 0
        self.angle = 0

    def updateRect(self):
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)

    def update(self, screenWidth, screenHeight):
        self.image = pygame.transform.rotate(self.baseImage, self.angle)
        dx , dy = self.scroll
        self.x += dx
        self.updateRect()

