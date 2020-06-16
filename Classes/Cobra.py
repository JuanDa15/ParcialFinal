import pygame
from CRUD import Functions

class Cobra(pygame.sprite.Sprite):
    def __init__(self,position,player):
        pygame.sprite.Sprite.__init__(self)
        self.Sprites = (pygame.image.load('Assets\Images\Sprites\Snake\Run.png'),pygame.image.load('Assets\Images\Sprites\Snake\Dead.png'))
        self.image = self.Sprites[0].subsurface(4,5,16,16)
        #self.image.fill(Functions.SelectColor('White'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 0
        self.vely = 0
        self.player = player
        self.Bloques = None

        #animacion
        self.frame = 0
        self.direccion = True
        self.Muerte = 30
        self.direccion = True
        self.accion = 0
        self.espera = 2
        self.animacion = ((4,5,16,16,37,5,14,16,70,5,14,16,101,5,14,16,132,5,16,16,163,5,19,16,194,5,22,16,227,5,19,16),(4,5,16,16,36,2,15,19,68,2,15,19,99,6,23,15,130,11,29,10,161,15,31,6))
        
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

        if self.player.rect.x < self.rect.x:
            self.velx = -2
            self.direccion = False
        elif self.player.rect.x > self.rect.x:
            self.velx = 2
            self.direccion = True


        if self.frame < len(self.animacion[self.accion]) - 1:
            if self.direccion == False:
                self.image = pygame.transform.flip(self.Sprites[self.accion].subsurface(self.animacion[self.accion][self.frame],self.animacion[self.accion][self.frame+1],self.animacion[self.accion][self.frame+2],self.animacion[self.accion][self.frame+3]),True,False)
            else:
                self.image = self.Sprites[self.accion].subsurface(self.animacion[self.accion][self.frame],self.animacion[self.accion][self.frame+1],self.animacion[self.accion][self.frame+2],self.animacion[self.accion][self.frame+3])
            if self.espera == 0: 
                self.frame += 4
                self.espera = 4
            else:
                self.espera -= 1 
        else:
            if self.accion != 1:
                self.frame = 0
            else:
                self.frame = len(self.animacion[self.accion])-1
                self.velx = 0

