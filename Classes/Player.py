import pygame
from CRUD import Functions

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25,25])
        self.image.fill(Functions.SelectColor('White'))
        self.rect = self.image.get_rect()
        self.position = [100,100]
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.velx = 0
        self.vely = 0
        
    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely