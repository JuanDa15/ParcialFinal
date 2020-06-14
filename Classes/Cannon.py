import pygame
from CRUD import Functions

class cannon(pygame.sprite.Sprite):
    def __init__(self,position,m,direccion):
        pygame.sprite.Sprite.__init__(self)
        self.image = m
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 0
        self.vely = 0
        self.timer = 50
        self.direccion = direccion
    

    def update(self):
       self.timer -= 1
    
    def returnPos(self):
        return self.rect.center
