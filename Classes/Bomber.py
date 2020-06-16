import pygame
from CRUD import Functions

class Bomber(pygame.sprite.Sprite):
    def __init__(self,position,m,direccion):
        pygame.sprite.Sprite.__init__(self)
        self.image = m
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 0
        self.vely = 0
        self.timer = 30
        self.direccion = direccion
        self.Bloques = None
    

    def update(self):
       self.timer -= 1
    
    def returnPos(self):
        return self.rect.center