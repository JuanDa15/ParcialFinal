import pygame
from CRUD import Functions

class cañon(pygame.sprite.Sprite):
    def __init__(self,position,widht,height):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.transform.scale(pygame.image.load('MapsTiledSet\Level1\Sprites\Cannon\Idle.png'),(38,32))
        #self.image.fill(Functions.SelectColor('Blue'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 0
        self.vely = 0
        self.Disparo = 30
        self.Direccion = False
        self.Bloques = None
        
    def update(self):
        #Posicion y velocidad en x
        self.rect.x += self.velx

        #colision x--------------------------------------------------------------------------------------
        listaColision=pygame.sprite.spritecollide(self,self.Bloques,False)
        for b in listaColision:
            if ((self.rect.right >= b.rect.left) and (self.rect.right <= b.rect.right)):
                self.velx=0
                self.rect.right = b.rect.left
            elif ((self.rect.left <= b.rect.right) and (self.rect.left >= b.rect.left)):
                self.velx=0
                self.rect.left = b.rect.right


        #Posicion y velocidad en x
        self.rect.y+=self.vely

        #colision y--------------------------------------------------------------------------------------
        listaColision=pygame.sprite.spritecollide(self,self.Bloques,False)
        for b in listaColision:
            self.EnAire = False
            if ((self.rect.bottom >= b.rect.top) and (self.rect.bottom <= b.rect.bottom)):
                self.vely = 0
                self.rect.bottom = b.rect.top       
            elif ((self.rect.top <= b.rect.bottom) and (self.rect.top >= b.rect.top)):
                self.vely = 0
                self.rect.top = b.rect.bottom
        

        
 