import pygame
from CRUD import Constants
from CRUD import UploadedFiles as UF
from CRUD import Functions
import datetime

class Shop(pygame.sprite.Sprite):
    def __init__(self,position,player,prices):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets\Images\Sprites\Collectables\Shop.png')
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.player = player
        self.ShopItems = pygame.sprite.Group()
        self.ShopItems.add(self)
        self.precioPotiLava = prices[0]
        self.potiLava = True
        self.precioPotiVel = prices[1]
        self.potiVel = True
        self.precioGapple = prices[2]
        self.Gapple = True

    def update(self):
        pass