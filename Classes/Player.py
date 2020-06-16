import pygame
from CRUD import Constants
from CRUD import Functions

class Jugador(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        #Orden = (Idle, Correr, Hit)
        self.image =  pygame.surface.Surface([24,28])
        self.image.fill(Functions.SelectColor('White'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

        self.HammerGroup = pygame.sprite.Group()
        self.Hammer = pygame.sprite.Sprite()
        self.Hammer.image = pygame.surface.Surface([40,28])
        self.Hammer.image.fill((255,0,0))
        self.Hammer.rect = self.Hammer.image.get_rect()
        self.Hammer.rect.x = position[0]
        self.Hammer.rect.y = position[1]
        self.HammerGroup.add(self.Hammer)
        self.DireccionHammer = 0

        self.Animacion = pygame.sprite.Sprite()
        self.AnimacionSprites = (pygame.image.load('Assets\Images\Sprites\Player\Hit (78x58).png'), pygame.image.load('Assets\Images\Sprites\Player\Run (78x58).png'),pygame.image.load('Assets\Images\Sprites\Player\Idle (78x58).png'),pygame.image.load('Assets\Images\Sprites\Player\Jump (78x58).png'))
        self.Animacion.image = self.AnimacionSprites[0].subsurface(7,14,37,28)
        self.Animacion.rect = self.Animacion.image.get_rect()
        self.Animacion.rect.x = position[0]+20
        self.Animacion.rect.y = position[1]

        self.velx = 0
        self.vely = 0
        self.vida = 100
        self.invisibility = 0
        self.EnAire = False
        self.EnLava = False
        self.EnAgua = False
        self.respiracion = 0
        self.InmunidadFuego = False
        self.Bloques = None
        self.Coins = 0
        self.Apples = 0
        self.Diamonds = 0
        self.Charge = 1.0
        self.quemadura = False
        self.TQuemadura = 0
        self.Fquemadura = 0
        self.gravity = 0.5


        #Animaciones
        self.accion = 2
        self.direccion = True
        self.espera = 2
        self.frame = 0
        self.animacion = ((7,14,37,26,86,15,37,26),(9,18,37,28,87,16,37,28,165,17,37,28,243,20,37,28,321,18,37,28,399,16,37,28,477,17,37,28,555,20,37,28),
                        (9,0,37,28,87,0,37,28,165,0,37,28,243,0,37,28,321,0,37,28,399,0,37,28,477,0,37,28,555,0,37,28,633,0,37,28,711,0,37,28,789,0,37,28),
                        (9,15,37,29))

    def update(self):
        #Posicion y velocidad en x
        if self.vida > 100:
            self.vida = 100
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
            if ((self.rect.bottom >= b.rect.top) and (self.rect.bottom <= b.rect.bottom)):
                self.vely = 0
                self.EnAire = False
                self.rect.bottom = b.rect.top
                Constants.PlataformaMovil = False
            elif ((self.rect.top <= b.rect.bottom) and (self.rect.top >= b.rect.top)):
                self.vely = 0
                self.rect.top = b.rect.bottom
                self.vely += 0.5
            
        if self.velx == 0:
            self.accion = 2
        else:
            self.accion = 1


        if self.frame < len(self.animacion[self.accion]) - 1:
            if self.direccion == True:
                self.Animacion.image = self.AnimacionSprites[self.accion].subsurface(self.animacion[self.accion][self.frame],self.animacion[self.accion][self.frame+1],self.animacion[self.accion][self.frame+2],self.animacion[self.accion][self.frame+3])
            else:
                self.Animacion.image = pygame.transform.flip(self.AnimacionSprites[self.accion].subsurface(self.animacion[self.accion][self.frame],self.animacion[self.accion][self.frame+1],self.animacion[self.accion][self.frame+2],self.animacion[self.accion][self.frame+3]), True, False)
            if self.espera == 0: 
                self.frame += 4
                self.espera = 2
            else:
                self.espera -= 1 
        else:
            self.frame = 0

        self.vely += self.gravity
        self.Hammer.rect.x = self.rect.x
        self.Hammer.rect.y = self.rect.y

        self.Animacion.rect.x = self.rect.x
        self.Animacion.rect.y = self.rect.y
        if self.DireccionHammer == 0:
            self.Hammer.rect.x -= 16
        if self.DireccionHammer == 1:
            self.Animacion.rect.x -= 13

    def UpdateRespiration(self):
        self.respiracion += 1
        
    def getRespiracion(self):
        return self.respiracion

