import pygame
from CRUD import Functions

class Escoba(pygame.sprite.Sprite):
    def __init__(self,position, pixeles):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([26,32])
        self.image.fill(Functions.SelectColor('White'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 2
        self.vely = 0
        self.Pixeles = pixeles
        self.Movidos = self.Pixeles
        self.Bloques = None
        
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
        #self.rect.y+=self.vely
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
        
        #self.vely += 0.5

        if self.Movidos > 0:
            self.Movidos -= 2
        else:
            self.Movidos = self.Pixeles
            self.velx = self.velx * -1
    
class Escoba(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([26,32])
        self.image.fill(Functions.SelectColor('White'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 2
        self.vely = 0
        self.Pixeles = pixeles
        self.Movidos = self.Pixeles
        self.Bloques = None
        
    def update(self):
        pass