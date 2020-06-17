import pygame
from CRUD import Constants
from CRUD import Functions

class Vida(pygame.sprite.Sprite):
    def __init__(self,position,player):
        pygame.sprite.Sprite.__init__(self)
        self.SpriteSalud = pygame.image.load('Assets\Images\Sprites\Life\Vida Rey.png')
        self.SpriteVida = pygame.image.load('Assets\Images\Sprites\Life\Live Bar.png')
        self.image = pygame.transform.scale(self.SpriteSalud.subsurface(0,0,50,24), (150,72))
        self.vida = self.SpriteVida.subsurface(0,102,66,34)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.player = player
        self.vidas = 3
        self.showLost = 25

        self.shield = pygame.sprite.Sprite()
        self.shield.image = pygame.image.load('Assets\Images\Sprites\Life\Shield.png')
        self.shield.rect = self.shield.image.get_rect()
        self.shield.rect.x = position[0]
        self.shield.rect.y = position[1]

        self.quemadura = pygame.sprite.Sprite()
        self.quemadura.image = pygame.transform.scale(pygame.image.load('Assets\Images\Sprites\Life\Fire.png'),(self.shield.image.get_rect()[2]+3,self.shield.image.get_rect()[3]+3))
        self.quemadura.rect = self.quemadura.image.get_rect()
        self.quemadura.rect.x = position[0]
        self.quemadura.rect.y = position[1]

        self.vidaLost = pygame.sprite.Sprite()
        self.vidaLost.image = pygame.transform.scale(pygame.image.load('Assets\Images\Sprites\Life\LostLife.png'),(24,23))
        self.vidaLost.rect = self.vidaLost.image.get_rect()
        self.vidaLost.rect.x = position[0]
        self.vidaLost.rect.y = position[1]

    def hitPlayer(self,amount):
        if self.player.invisibility == 0:
            self.player.vida -= amount
            self.player.invisibility = 25
    
    def instakill(self):
        self.vidas -= 1
        self.player.vida = 100

        self.vida = self.SpriteVida.subsurface(0,34 * self.vidas,66,34)

    def update(self):
        if self.showLost < 25:
            self.showLost += 1
            Constants.Screen.blit(self.vidaLost.image, [self.player.rect.x,self.player.rect.y-self.showLost])
            
        if self.player.invisibility > 0:
            self.player.invisibility -= 1
        if self.player.vida <= 0:
            self.vidas -= 1
            self.player.vida = 100
            self.vida = self.SpriteVida.subsurface(0,34 * self.vidas,66,34)
            self.showLost = 0
        if self.vidas == 0:
            self.player.vida = 100
            

        if self.player.vida > 90:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(0,0,50,24), (150,72))
        if self.player.vida <= 90 and self.player.vida > 80:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(50,0,50,24), (150,72))
        if self.player.vida <= 80 and self.player.vida > 70:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(0,25,50,24), (150,72))
        if self.player.vida <= 70 and self.player.vida > 60:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(50,25,50,24), (150,72))
        if self.player.vida <= 60 and self.player.vida > 50:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(0,50,50,24), (150,72))
        if self.player.vida <= 50 and self.player.vida > 40:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(50,50,50,24), (150,72))
        if self.player.vida <= 40 and self.player.vida > 30:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(0,75,50,24), (150,72))
        if self.player.vida <= 30 and self.player.vida > 20:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(50,75,50,24), (150,72))
        if self.player.vida <= 20 and self.player.vida > 10:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(0,100,50,24), (150,72))
        if self.player.vida <= 10:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(50,100,50,24), (150,72))

