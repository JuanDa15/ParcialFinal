import pygame
from CRUD import Functions

class cannonball(pygame.sprite.Sprite):
    def __init__(self,position,direccion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('Assets\Sprites\Cannon\Cannon Ball.png'),(18,18))
        #self.image.fill(Functions.SelectColor('Yellow'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = direccion
        self.vely = 0
    
    def update(self):
        #Posicion y velocidad en x
        self.rect.x+=self.velx      
        
        #Posicion y velocidad en y
        self.rect.y+=self.vely

        
