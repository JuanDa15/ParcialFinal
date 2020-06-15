import pygame
from CRUD import Constants
from CRUD import Functions

class Jugador(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        #self.Sprites = pygame.image.load('Assets\Images\Sprites\Player\Run (78x58).png')
        self.image = pygame.surface.Surface([24,28])
        #self.image = self.Sprites.subsurface(9,18,37,25)
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
        self.AnimacionSprites = pygame.image.load('Assets\Images\Sprites\Player\Run (78x58).png')
        self.Animacion.image = self.AnimacionSprites.subsurface(9,18,37,25)
        self.Animacion.rect = self.Animacion.image.get_rect()
        self.Animacion.rect.x = position[0]
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
        self.vely += self.gravity
        self.Hammer.rect.x = self.rect.x
        self.Hammer.rect.y = self.rect.y

        self.Animacion.rect.x = self.rect.x
        self.Animacion.rect.y = self.rect.y
        if self.DireccionHammer == 0:
            self.Hammer.rect.x -= 16

    def UpdateRespiration(self):
        self.respiracion += 1
        
    def getRespiracion(self):
        return self.respiracion
