import pygame
from CRUD import Functions

class bomb(pygame.sprite.Sprite):
    def __init__(self,position,direction):
        pygame.sprite.Sprite.__init__(self)
        self.Sprites = (pygame.image.load('Assets\Images\Sprites\Bomb\spin left.png'),pygame.image.load('Assets\Images\Sprites\Bomb\spin right.png'))
        self.image = self.Sprites[0].subsurface(0,1,13,16)
        #self.image.fill(Functions.SelectColor('Yellow'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.direccion = direction
        if self.direccion:
            self.velx = 3
        else:
            self.velx = -3
        self.vely = 0
        self.Bloques = None
        self.time = 60

        #animacion
        self.frame = 0
        self.espera = 1
        self.animacion=((0,1,13,16,15,1,16,16,33,1,13,16,48,2,16,15),(0,1,13,16,15,1,16,16,33,1,13,16,48,2,16,15))
        
    def update(self):
        #Posicion y velocidad en x
        self.rect.x += self.velx
        
        if self.time > 0:
            self.time -= 1

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

        #Gravedad-------------------------------------------------------------------------------------
        self.vely += 0.7

        if self.direccion == True:
            self.accion = 0
        else:
            self.accion = 1

        if self.frame < len(self.animacion[self.accion]) - 1:
            self.image = pygame.transform.flip(self.Sprites[self.accion].subsurface(self.animacion[self.accion][self.frame],self.animacion[self.accion][self.frame+1],self.animacion[self.accion][self.frame+2],self.animacion[self.accion][self.frame+3]),True,False)
            if self.espera == 0: 
                self.frame += 4
                self.espera = 2
            else:
                self.espera -= 1
        else:
            self.frame = 0