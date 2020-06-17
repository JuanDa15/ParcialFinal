import pygame
import sys
import random
#Import packages
from CRUD.Menus import MainMenu as MM
from CRUD import Constants
from Classes import BackGround as BG
pygame.init()
pygame.mixer.quit()

def show_history(part):
        i = 0
        back = pygame.sprite.Group()
        Background1 = BG.Background([0,0],eval('Constants.Video_historia_'+str(part)))
        back.add(Background1)
        for i in range(len(eval('Constants.Video_historia_'+str(part)))-10):
            back.update()
            back.draw(Constants.Screen)
            pygame.display.update()
            pygame.display.flip()