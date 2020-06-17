import pygame
import random
from CRUD import Functions
from CRUD import Constants

class Roca(pygame.sprite.Sprite):
    def __init__(self,position,player,direction):
        pygame.sprite.Sprite.__init__(self)
        #self.Sprites = pygame.Surface.Surface([50,50])
        self.image = pygame.surface.Surface([50,50])
        self.image.fill(Functions.SelectColor('Yellow'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.direccion = direction
        if self.direccion:
            self.velx = 10
        else:
            self.velx = -10
        
        self.possibleVel = [-10,-15,-20]

        self.vely = self.possibleVel[random.randint(0,2)]
        self.player = player
        self.time = 100

        #animacion
        self.frame = 0
        self.espera = 1
        self.animacion=((0,1,13,16,15,1,16,16,33,1,13,16,48,2,16,15),(0,1,13,16,15,1,16,16,33,1,13,16,48,2,16,15))
        
    def update(self):
        listaColision=pygame.sprite.spritecollide(self,self.player,False)
        if listaColision:
            Constants.LifeManager.hitPlayer(40)
            Constants.LasersJefe2.remove(self)
        #Posicion y velocidad en x
        self.rect.x += self.velx
        
        if self.time > 0:
            self.time -= 1

        self.rect.y+=self.vely

        self.vely += 0.5