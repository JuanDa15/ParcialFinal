import pygame
from CRUD import Functions

class cannonball(pygame.sprite.Sprite):
    def __init__(self,position,direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets\Images\Sprites\Cannon\Cannon Ball.png')
        #self.image.fill(Functions.SelectColor('Yellow'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.distance = 0
        self.velx = direction
        self.bloques = None
    
    def update(self):
        #Posicion y velocidad en x
        self.rect.x+=self.velx 
        self.distance += 1

    def getDistance(self):
        return self.distance
        
