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
        self.Dead = False

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
        self.AnimacionSprites = (pygame.image.load('Assets\Images\Sprites\Minotaur\Run.png'), pygame.image.load('Assets\Images\Sprites\Minotaur\Dead.png'),pygame.image.load('Assets\Images\Sprites\Minotaur\stomp.png'),pygame.image.load('Assets\Images\Sprites\Minotaur\hack.png'))
        self.Animacion.image = self.AnimacionSprites[0].subsurface(26,13,52,41)
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
        self.accion = 0
        self.direccion = True
        self.espera = 2
        self.frame = 0
        self.animacion = ((26,13,52,41,121,11,52,41,218,13,52,41,315,15,52,41,412,13,52,41,509,11,52,41,604,13,52,41,699,15,52,41),(28,7,52,41,125,7,53,41,226,6,54,41,322,7,55,41,418,7,53,41,514,7,53,41),
                        (23,17,38,41,119,17,38,41,215,17,38,41,311,17,38,41,407,17,38,41,503,17,38,41),
                        (5,16,56,45,126,20,58,41,220,20,57,41,316,20,57,41,412,20,55,41,508,20,55,41,603,20,50,41,700,20,48,41,796,20,52,41))

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

        if not self.Dead:
            #Interacciones
            #Golpear al jugador con el hacha
            if not self.Angry:
                if self.intervalo < 20:
                    self.intervalo += 1
                listaColision=pygame.sprite.spritecollide(self.player,self.AxeGroup,False)
                if listaColision:
                    if self.intervalo == 20:
                        self.intervalo = 0
                        self.frame = 0
                        self.accion = 3
                        Constants.LifeManager.hitPlayer(20)
            #Golpear en area y ser invulnerable
            if self.Angry:
                self.velx = 0
                if self.AngryTime < 30:
                    listaColision=pygame.sprite.spritecollide(self.player,self.AreaGroup,False)
                    if listaColision:
                        self.frame = 0
                        self.accion = 2
                        self.player.vely = -10
                        Constants.LifeManager.hitPlayer(20)
                        self.Angry = False
                        self.AngryTime = 100

        if not self.Dead:
            if self.Angry:
                self.AngryTime -= 1
            if self.AngryTime == 0:
                self.frame = 0
                self.accion = 2
                self.AngryTime = 100
                self.Angry = False


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
            if self.accion == 1:
                self.frame = len(self.animacion[self.accion])-1
            else:
                self.frame = 0
                self.accion = 0
                
        if not self.Dead:
            self.vely += self.gravity
            self.Axe.rect.x = self.rect.x
            self.Axe.rect.y = self.rect.y

            self.Area.rect.x = self.rect.x - 10
            self.Area.rect.y = self.rect.y - 10

            self.Animacion.rect.x = self.rect.x
            self.Animacion.rect.y = self.rect.y
            
            if not self.Angry:
                if self.player.rect.x < self.rect.x - 22:
                    self.velx = -2
                    self.DireccionAxe = 0
                    self.direccion = False
                elif self.player.rect.x > self.rect.x + 22:
                    self.DireccionAxe = 1
                    self.velx = 2
                    self.direccion = True
