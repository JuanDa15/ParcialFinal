import pygame
from CRUD import Constants
from CRUD import UploadedFiles as UF
from CRUD import Functions
import datetime

class Shop(pygame.sprite.Sprite):
    def __init__(self,position,player,prices):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load('Assets\Images\Sprites\Collectables\Shop.png')
        self.image = self.imagen.subsurface(1,0,127,80)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.player = player
        self.ShopItems = pygame.sprite.Group()
        self.Tendero = pygame.sprite.Group()
        self.Tendero.add(self)

        self.potiLavaSprite = pygame.sprite.Sprite()
        self.potiLavaSprite.image = pygame.image.load('Assets\Images\Sprites\Collectables\lava.png')
        self.potiLavaSprite.rect = self.potiLavaSprite.image.get_rect()
        self.potiLavaSprite.type = 0
        self.precioPotiLava = prices[0]
        self.potiLava = True
        self.ShopItems.add(self.potiLavaSprite)
        
        self.potiVelSprite = pygame.sprite.Sprite()
        self.potiVelSprite.image = pygame.image.load('Assets\Images\Sprites\Collectables\speed.png')
        self.potiVelSprite.rect = self.potiVelSprite.image.get_rect()
        self.potiVelSprite.type = 1
        self.precioPotiVel = prices[1]
        self.potiVel = True
        self.ShopItems.add(self.potiVelSprite)
        
        self.GappleSprite = pygame.sprite.Sprite()
        self.GappleSprite.image = pygame.image.load('Assets\Images\Sprites\Collectables\Gapple.png')
        self.GappleSprite.rect = self.GappleSprite.image.get_rect()
        self.GappleSprite.type = 2
        self.precioGapple = prices[2]
        self.Gapple = True
        self.ShopItems.add(self.GappleSprite)

        #Animacion
        self.frame = 0
        self.espera = 2
        self.recortes = (1,0,127,80,128,0,126,80,255,0,126,80,382,0,126,80,509,0,126,80)

    def update(self):
        if self.frame < len(self.recortes) - 1:
            self.image = self.imagen.subsurface(self.recortes[self.frame],self.recortes[self.frame + 1],self.recortes[self.frame + 2],self.recortes[self.frame + 3])
            if self.espera == 0: 
                self.frame += 4
                self.espera = 4
            else:
                self.espera -= 1
        else:
            self.frame = 0 
            
        if self.Gapple:
            Functions.draw_text('$'+str(self.precioGapple),UF.TextFont(12),Functions.SelectColor('White'),Constants.Screen,self.rect.x + 25 + (126/3)*0,self.rect.y+50+38)
            self.GappleSprite.rect.x = self.rect.x + 30 + (126/3)*0
            self.GappleSprite.rect.y = self.rect.y + 50
        else:
            self.ShopItems.remove(self.GappleSprite)

        if self.potiVel:
            Functions.draw_text('$'+str(self.precioPotiVel),UF.TextFont(12),Functions.SelectColor('White'),Constants.Screen,self.rect.x + 25 + (126/3)*1,self.rect.y+50+38)
            self.potiVelSprite.rect.x = self.rect.x + 30 + (126/3)*1
            self.potiVelSprite.rect.y = self.rect.y + 50
        else:
            self.ShopItems.remove(self.potiVelSprite)
        
        if self.potiLava:
            Functions.draw_text('$'+str(self.precioPotiLava),UF.TextFont(12),Functions.SelectColor('White'),Constants.Screen,self.rect.x + 25 + (126/3)*2,self.rect.y+50+38)
            self.potiLavaSprite.rect.x = self.rect.x + 30 + (126/3)*2
            self.potiLavaSprite.rect.y = self.rect.y + 50
        else:
            self.ShopItems.remove(self.potiLavaSprite)
        pass
