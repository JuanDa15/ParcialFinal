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

    def hitPlayer(self,amount):
        if self.player.invisibility == 0:
            self.player.vida -= amount
            self.player.invisibility = 25
    
    def instakill(self):
        self.vidas -= 1
        self.player.vida = 100

        self.vida = self.SpriteVida.subsurface(0,34 * self.vidas,66,34)

    def update(self):
        #print("Healt: "+str(self.player.vida)+" Lifes: "+str(self.vidas))
        if self.player.invisibility > 0:
            self.player.invisibility -= 1
        if self.player.vida <= 0:
            self.vidas -= 1
            self.player.vida = 100
            self.vida = self.SpriteVida.subsurface(0,34 * self.vidas,66,34)
        if self.vidas == 0:
            quit()

        if self.player.vida > 80:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(0,0,50,24), (150,72))
        if self.player.vida <= 80 and self.player.vida > 60:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(0,25,50,24), (150,72))
        if self.player.vida <= 60 and self.player.vida > 40:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(0,50,50,24), (150,72))
        if self.player.vida <= 40 and self.player.vida > 20:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(0,75,50,24), (150,72))
        if self.player.vida <= 20:
            self.image = pygame.transform.scale(self.SpriteSalud.subsurface(0,100,50,24), (150,72))

