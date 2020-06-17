import pygame
from CRUD import Constants
from CRUD import Functions

class King(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        #Orden = (Idle, Correr, Hit)
        self.image =  pygame.surface.Surface([24,28])
        self.image.fill(Functions.SelectColor('White'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

        self.Animacion = pygame.sprite.Sprite()
        self.AnimacionSprites = pygame.image.load('Assets\Images\Sprites\King Pig\Idle (38x28).png')
        self.Animacion.image = self.AnimacionSprites.subsurface(11,8,18,20)
        self.Animacion.rect = self.Animacion.image.get_rect()
        self.Animacion.rect.x = position[0]+20
        self.Animacion.rect.y = position[1]

        self.velx = 0
        self.vely = 0
        self.Bloques = None
        self.gravity = 0.5

        #Animaciones
        self.accion = 0
        self.direccion = True
        self.espera = 2
        self.frame = 0
        self.animacion = (11,6,18,22,49,6,18,22,87,6,18,22,125,6,18,22,163,6,18,22,201,6,18,22,239,6,18,22,277,6,18,22,315,6,18,22,352,6,18,22,390,6,19,22,429,6,18,22)
                        

    def update(self):
        #Posicion y velocidad en x
        #colision x--------------------------------------------------------------------------------------
        listaColision=pygame.sprite.spritecollide(self,self.Bloques,False)
        for b in listaColision:
            if ((self.rect.right >= b.rect.left) and (self.rect.right <= b.rect.right)):
                self.rect.right = b.rect.left
            elif ((self.rect.left <= b.rect.right) and (self.rect.left >= b.rect.left)):
                self.rect.left = b.rect.right

        #Posicion y velocidad en x
        self.rect.y+=self.vely
        #colision y--------------------------------------------------------------------------------------
        listaColision=pygame.sprite.spritecollide(self,self.Bloques,False)
        for b in listaColision:
            if ((self.rect.bottom >= b.rect.top) and (self.rect.bottom <= b.rect.bottom)):
                self.vely = 0
                self.rect.bottom = b.rect.top
                Constants.PlataformaMovil = False
            elif ((self.rect.top <= b.rect.bottom) and (self.rect.top >= b.rect.top)):
                self.vely = 0
                self.rect.top = b.rect.bottom
                self.vely += 0.5

        if self.frame < 44:
            if self.direccion == True:
                self.Animacion.image = self.AnimacionSprites.subsurface(self.animacion[self.frame],self.animacion[self.frame+1],self.animacion[self.frame+2],self.animacion[self.frame+3])
            else:
                self.Animacion.image = pygame.transform.flip(self.AnimacionSprites.subsurface(self.animacion[self.frame],self.animacion[self.frame+1],self.animacion[self.frame+2],self.animacion[self.frame+3]), True, False)
            if self.espera == 0: 
                self.frame += 4
                self.espera = 2
            else:
                self.espera -= 1 
        else:
            self.frame = 0


        self.vely += self.gravity
        self.Animacion.rect.x = self.rect.x
        self.Animacion.rect.y = self.rect.y

