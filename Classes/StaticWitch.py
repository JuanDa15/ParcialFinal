import pygame
from CRUD import Functions

class StaticWitch(pygame.sprite.Sprite):
    def __init__(self,position, pixeles):
        pygame.sprite.Sprite.__init__(self)
        self.Correr = pygame.image.load('Assets\Sprites\Pork\Run (34x28).png')
        self.image = self.Correr.subsurface(10,0,19,15)
        #self.image.fill(Functions.SelectColor('White'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1] 
        self.velx = 2
        self.vely = 0
        self.Pixeles = pixeles
        self.Movidos = self.Pixeles
        self.Bloques = None

        #animacion
        #self.frame = 0
        #self.direccion = True
        #self.espera = 4
        #self.animacion = (10,0,19,22,44,0,19,22,79,0,18,22,113,0,18,22,147,0,18,22,181,0,18,22)
        
    def update(self):
        #Posicion y velocidad en x
        self.rect.x += self.velx
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
            if self.rect.colliderect(b.rect):
                self.EnAire = False
            else:
                self.EnAire = True
            if ((self.rect.bottom >= b.rect.top) and (self.rect.bottom <= b.rect.bottom)):
                self.vely = 0
                self.rect.bottom = b.rect.top       
            elif ((self.rect.top <= b.rect.bottom) and (self.rect.top >= b.rect.top)):
                self.vely = 0
                self.rect.top = b.rect.bottom
        
        self.vely += 0.5

        if self.Movidos > 0:
            self.Movidos -= 2
        else:
            if self.direccion == True:
                self.direccion = False
            else:
                self.direccion = True
            self.Movidos = self.Pixeles
            self.velx = self.velx * -1

        """
        if self.frame < len(self.animacion) - 1:
            if self.direccion == True:
                self.image = pygame.transform.flip(self.Correr.subsurface(self.animacion[self.frame],self.animacion[self.frame+1],self.animacion[self.frame+2],self.animacion[self.frame+3]),True,False)
            else:
                self.image = self.Correr.subsurface(self.animacion[self.frame],self.animacion[self.frame+1],self.animacion[self.frame+2],self.animacion[self.frame+3])
            if self.espera == 0: 
                self.frame += 4
                self.espera = 4
            else:
                self.espera -= 1 
        else:
            self.frame = 0 
            """