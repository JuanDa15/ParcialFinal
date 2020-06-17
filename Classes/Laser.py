import pygame
from CRUD import Functions
from CRUD import Constants

class Laser(pygame.sprite.Sprite):
    def __init__(self,position,player,direction):
        pygame.sprite.Sprite.__init__(self)
        self.Sprites = (pygame.image.load('Assets\Images\Sprites\Laser\Idle.png'),pygame.image.load('Assets\Images\Sprites\Bomb\spin right.png'))
        self.image = self.Sprites[0].subsurface(0,0,35,5)
        #self.image.fill(Functions.SelectColor('Yellow'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.direccion = direction
        if self.direccion == 0:
            self.velx = -10
            self.vely = 0
        elif self.direccion == 1:
            self.velx = -10
            self.vely = -10
        elif self.direccion == 2:
            self.velx = 0
            self.vely = -10
        elif self.direccion == 3:
            self.velx = 10
            self.vely = -10
        elif self.direccion == 4:
            self.velx = 10
            self.vely = 0
        self.time = 60
        self.player = player

        #animacion
        self.frame = 0
        self.espera = 1
        self.animacion=((0,1,13,16,15,1,16,16,33,1,13,16,48,2,16,15),(0,1,13,16,15,1,16,16,33,1,13,16,48,2,16,15))
        
    def update(self):
        listaColision=pygame.sprite.spritecollide(self,self.player,False)
        if listaColision:
            Constants.LifeManager.hitPlayer(10)
            Constants.LasersJefe2.remove(self)
        #Posicion y velocidad en x
        self.rect.x += self.velx
        
        if self.time > 0:
            self.time -= 1

        self.rect.y+=self.vely