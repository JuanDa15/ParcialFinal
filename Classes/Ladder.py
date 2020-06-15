import pygame
from CRUD import Functions

class Ladder(pygame.sprite.Sprite):
    def __init__(self, position,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
