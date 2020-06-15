import pygame
from CRUD import Constants
from CRUD import Functions

class Vida(pygame.sprite.Sprite):
    def __init__(self,position,player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([26,32])
        self.image.fill(Functions.SelectColor('White'))
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

    def update(self):
        #print("Healt: "+str(self.player.vida)+" Lifes: "+str(self.vidas))
        if self.player.invisibility > 0:
            self.player.invisibility -= 1
        if self.player.vida <= 0:
            self.vidas -= 1
            self.player.vida = 100
        if self.vidas == 0:
            quit()