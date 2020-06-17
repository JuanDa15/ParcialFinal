import pygame
from CRUD import Functions

class Bomber(pygame.sprite.Sprite):
    def __init__(self,position,m,direccion):
        pygame.sprite.Sprite.__init__(self)
        self.Sprites = (pygame.image.load('Assets\Images\Sprites\Bomber\Idle (26x26).png'), pygame.image.load('Assets\Images\Sprites\Bomber\Dead (34x28).png'), pygame.image.load('Assets\Images\Sprites\Bomber\Throwing Boom (26x26).png'))
        self.image = self.Sprites[0].subsurface(2,2,22,24)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 0
        self.vely = 0
        self.timer = 80
        self.player = None
        self.direccion = direccion
        self.Bloques = None

        #animacion
        self.accion = 0
        self.Muerte = 30
        self.frame = 0
        self.espera = 2
        self.animacion = ((2,2,22,24,28,2,22,24,54,2,23,24,80,2,22,24,106,2,23,24,132,2,22,24,158,2,22,24,184,2,22,24,210,2,22,24,236,2,22,24),(11,4,19,24,48,4,18,24,83,4,18,24,119,4,17,24),(2,2,23,24,28,2,24,24,54,2,24,24,79,2,17,24,104,2,20,24),(2,2,23,24,28,2,24,24,54,2,24,24,79,2,18,24,104,2,20,24))
    
    def update(self):
        self.timer -= 1
        if self.timer == 0:
            self.timer = 80
            self.frame = 0
            self.accion = 2
        #Posicion y velocidad en x

        if self.frame < len(self.animacion[self.accion]) - 1:
            if self.direccion == True:
                self.image = pygame.transform.flip(self.Sprites[self.accion].subsurface(self.animacion[self.accion][self.frame],self.animacion[self.accion][self.frame+1],self.animacion[self.accion][self.frame+2],self.animacion[self.accion][self.frame+3]),True,False)
            else:
                self.image = self.Sprites[self.accion].subsurface(self.animacion[self.accion][self.frame],self.animacion[self.accion][self.frame+1],self.animacion[self.accion][self.frame+2],self.animacion[self.accion][self.frame+3])
            if self.espera == 0: 
                self.frame += 4
                self.espera = 2
            else:
                self.espera -= 1
        else:
            if self.accion != 1:
                self.accion = 0
                self.frame = 0
            else:
                self.frame = 15
                self.velx = 0
        
        if self.player.rect.x < self.rect.x:
            self.direccion = False
        elif self.player.rect.x > self.rect.x:
            self.direccion = True
    
    def returnPos(self):
        return self.rect.center