import pygame
from CRUD import Constants
from CRUD import Functions

class Minotauro(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        #Orden = (Idle, Correr, Hit)
        self.image =  pygame.surface.Surface([30,41])
        self.image.fill(Functions.SelectColor('White'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.player = None
        self.intervalo = 20
        self.Angry = False
        self.AngryTime = 100

        self.AxeGroup = pygame.sprite.Group()
        self.Axe = pygame.sprite.Sprite()
        self.Axe.image = pygame.surface.Surface([52,41])
        self.Axe.image.fill((255,0,0))
        self.Axe.rect = self.Axe.image.get_rect()
        self.Axe.rect.x = position[0]
        self.Axe.rect.y = position[1]
        self.AxeGroup.add(self.Axe)
        self.DireccionAxe = 0

        self.AreaGroup = pygame.sprite.Group()
        self.Area = pygame.sprite.Sprite()
        self.Area.image = pygame.surface.Surface([72,51])
        self.Area.image.fill((0,255,0))
        self.Area.rect = self.Area.image.get_rect()
        self.Area.rect.x = position[0]
        self.Area.rect.y = position[1]
        self.AreaGroup.add(self.Area)

        self.Animacion = pygame.sprite.Sprite()
        self.AnimacionSprites = (pygame.image.load('Assets\Images\Sprites\Player\Hit (78x58).png'), pygame.image.load('Assets\Images\Sprites\Player\Run (78x58).png'),pygame.image.load('Assets\Images\Sprites\Player\Idle (78x58).png'),pygame.image.load('Assets\Images\Sprites\Player\Jump (78x58).png'),pygame.image.load('Assets\Images\Sprites\Player\Attack (78x58).png'))
        self.Animacion.image = self.AnimacionSprites[0].subsurface(7,14,37,28)
        self.Animacion.rect = self.Animacion.image.get_rect()
        self.Animacion.rect.x = position[0]+20
        self.Animacion.rect.y = position[1]

        self.velx = 0
        self.vely = 0
        self.vida = 5
        self.invisibility = 0
        self.Bloques = None
        self.gravity = 0.5
        self.premio = 50

        #Animaciones
        self.accion = 2
        self.direccion = True
        self.espera = 2
        self.frame = 0
        self.animacion = ((7,14,37,26,86,15,37,26),(9,18,37,28,87,16,37,28,165,17,37,28,243,20,37,28,321,18,37,28,399,16,37,28,477,17,37,28,555,20,37,28),
                        (9,0,37,28,87,0,37,28,165,0,37,28,243,0,37,28,321,0,37,28,399,0,37,28,477,0,37,28,555,0,37,28,633,0,37,28,711,0,37,28,789,0,37,28),
                        (9,15,37,29),(20,0,58,26,100,0,49,26,165,0,37,26))

    def update(self):
        if self.invisibility > 0:
            self.invisibility -= 1
        #Posicion y velocidad en x
        self.rect.x += self.velx
        #colision x--------------------------------------------------------------------------------------
        listaColision=pygame.sprite.spritecollide(self,self.Bloques,False)
        for b in listaColision:
            if ((self.rect.right >= b.rect.left) and (self.rect.right <= b.rect.right)):
                self.rect.right = b.rect.left
                self.vely = -5
            elif ((self.rect.left <= b.rect.right) and (self.rect.left >= b.rect.left)):
                self.rect.left = b.rect.right
                self.vely = -5

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

        #Interacciones
        #Golpear al jugador con el hacha
        if not self.Angry:
            if self.intervalo < 20:
                self.intervalo += 1
            listaColision=pygame.sprite.spritecollide(self.player,self.AxeGroup,False)
            if listaColision:
                if self.intervalo == 20:
                    self.intervalo = 0
                    #Animacion de golpear con hacha
                    Constants.LifeManager.hitPlayer(20)
        #Golpear en area y ser invulnerable
        if self.Angry:
            self.velx = 0
            if self.AngryTime < 30:
                listaColision=pygame.sprite.spritecollide(self.player,self.AreaGroup,False)
                if listaColision:
                    #Animacion de golpear en el suelo
                    self.player.vely = -10
                    Constants.LifeManager.hitPlayer(20)
                    self.Angry = False
                    self.AngryTime = 100

        if self.Angry:
            self.AngryTime -= 1
        if self.AngryTime == 0:
            self.AngryTime = 100
            self.Angry = False

        if self.accion != 4:  
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
            if self.accion == 4:
                self.accion = 1

        self.vely += self.gravity
        self.Axe.rect.x = self.rect.x
        self.Axe.rect.y = self.rect.y

        self.Area.rect.x = self.rect.x - 22
        self.Area.rect.y = self.rect.y - 10

        self.Animacion.rect.x = self.rect.x
        self.Animacion.rect.y = self.rect.y
        if self.DireccionAxe == 0:
            self.Axe.rect.x -= 22
        if self.DireccionAxe == 1:
            #self.Axe.rect.x += 30
            self.Animacion.rect.x -= 13
        
        if not self.Angry:
            if self.player.rect.x < self.rect.x - 22:
                self.velx = -2
                self.DireccionAxe = 0
                self.direccion = False
            elif self.player.rect.x > self.rect.x + 22:
                self.DireccionAxe = 1
                self.velx = 2
                self.direccion = True