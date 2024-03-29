import pygame
from CRUD import Constants
from CRUD import UploadedFiles as UF
from CRUD import Functions
import datetime

class Score(pygame.sprite.Sprite):
    def __init__(self,position,player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets\Images\Sprites\Collectables\Score.png')
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.player = player
        self.Scores = pygame.sprite.Group()
        self.Scores.add(self)

    def update(self):
        Functions.draw_text(' X '+str(self.player.Coins),UF.TittleFont(10),Functions.SelectColor('Black'),Constants.Screen,self.rect.x+35,self.rect.y+18)
        Functions.draw_text(' X '+str(self.player.Diamonds),UF.TittleFont(10),Functions.SelectColor('Black'),Constants.Screen,self.rect.x+35,self.rect.y+43)
        Functions.draw_text(' X '+str(self.player.Apples),UF.TittleFont(10),Functions.SelectColor('Black'),Constants.Screen,self.rect.x+35,self.rect.y+71)
        Functions.draw_text(''+str(datetime.timedelta(seconds=((pygame.time.get_ticks() - Constants.ClockStart) / 1000)))[:-4],UF.TextFont(10),Functions.SelectColor('Black'),Constants.Screen,self.rect.x+28,self.rect.y+3)
        Constants.Total_Minutos = int(((pygame.time.get_ticks() - Constants.ClockStart) / 1000)/60)
        Constants.Total_Time = ''+str(datetime.timedelta(seconds=((pygame.time.get_ticks() - Constants.ClockStart) / 1000)))[:-4]
        if Constants.AppleTime <= 250 and Constants.AppleTime > 200:
            Functions.draw_text('-',UF.TextFont(16),Functions.SelectColor('Black'),Constants.Screen,self.rect.x+26,self.rect.y+95)
        if Constants.AppleTime <= 200 and Constants.AppleTime > 150:
            Functions.draw_text('--',UF.TextFont(16),Functions.SelectColor('Black'),Constants.Screen,self.rect.x+26,self.rect.y+95)
        if Constants.AppleTime <= 150 and Constants.AppleTime > 100:
            Functions.draw_text('---',UF.TextFont(16),Functions.SelectColor('Black'),Constants.Screen,self.rect.x+26,self.rect.y+95)
        if Constants.AppleTime <= 100 and Constants.AppleTime > 50:
            Functions.draw_text('----',UF.TextFont(16),Functions.SelectColor('Black'),Constants.Screen,self.rect.x+26,self.rect.y+95)
        if Constants.AppleTime <= 50 and Constants.AppleTime > 0:
            Functions.draw_text('-----',UF.TextFont(16),Functions.SelectColor('Black'),Constants.Screen,self.rect.x+26,self.rect.y+95)
        if Constants.AppleTime == 0:
            Functions.draw_text('READY',UF.TextFont(16),Functions.SelectColor('Black'),Constants.Screen,self.rect.x+26,self.rect.y+95)