import pygame
from CRUD import Functions

class Escoba(pygame.sprite.Sprite):
    def __init__(self,position, pixeles):
        pygame.sprite.Sprite.__init__(self)
        self.Sprites = (pygame.image.load('Assets\Images\Sprites\Witch\Fly.png'),pygame.image.load('Assets\Images\Sprites\Witch\Death.png'))
        self.image = self.Sprites[0].subsurface(3,0,26,29)
        #self.image.fill(Functions.SelectColor('White'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 2
        self.vely = 0
        self.Pixeles = pixeles
        self.Movidos = self.Pixeles
        self.Bloques = None
        if self.Pixeles < 0:
            self.Pixeles = self.Pixeles * -1
            self.Movidos = 0

        #animacion
        self.frame = 0
        self.Muerte = 60
        self.direccion = True
        self.accion = 0
        self.espera = 2
        self.animacion = ((3,0,26,29,34,0,27,29,65,0,28,29,98,0,27,29),(4,0,22,24,36,0,21,24,68,0,21,24,100,0,21,24,133,0,20,24,165,0,20,24,197,0,21,24,228,0,22,24,260,0,23,24,292,0,20,24))
        
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
            if self.direccion == True:
                self.direccion = False
            else:
                self.direccion = True
            self.Movidos = self.Pixeles
            self.velx = self.velx * -1
        

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

    
class Estatica(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.Sprites = (pygame.image.load('Assets\Images\Sprites\Witch\Idle.png'),pygame.image.load('Assets\Images\Sprites\Witch\Death.png'),pygame.image.load('Assets\Images\Sprites\Witch\Attack.png'))
        self.image = self.Sprites[0].subsurface(4,0,22,24)
        #self.image = pygame.Surface([26,32])
        #self.image.fill(Functions.SelectColor('White'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 0
        self.vely = 0
        self.Bloques = None

        #animacion
        self.frame = 0
        self.direccion = True
        self.accion = 0
        self.espera = 2
        self.Muerte = 60
        self.animacion = ((4,0,22,24,36,0,22,24,68,0,22,24,100,0,21,24),(4,0,22,24,36,0,21,24,68,0,21,24,100,0,21,24,133,0,20,24,165,0,20,24,197,0,21,24,228,0,22,24,260,0,23,24,292,0,20,24),(4,0,22,24,34,0,25,24,66,0,22,24,97,0,22,24,133,0,22,24,166,0,22,24,196,0,24,24,228,0,24,24))
        
    def update(self):
        #Posicion y velocidad en x
        #self.rect.x += self.velx
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