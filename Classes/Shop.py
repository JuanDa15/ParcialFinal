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

        self.GappleSprite = pygame.sprite.Sprite()
        self.GappleSprite.image = pygame.image.load('Assets\Images\Sprites\Collectables\Gapple.png')
        self.GappleSprite.rect = self.GappleSprite.image.get_rect()
        self.precioGapple = prices[2]
        self.Gapple = True
        self.ShopItems.add(self.GappleSprite)

    def update(self):
        if self.Gapple:
            Functions.draw_text('$'+str(self.precioGapple),UF.TextFont(12),Functions.SelectColor('White'),Constants.Screen,self.rect.x,self.rect.y+45-18)
            self.GappleSprite.rect.x = self.rect.x
            self.GappleSprite.rect.y = self.rect.y + 45
        else:
            self.ShopItems.remove(self.GappleSprite)
        pass