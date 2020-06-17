#Import of libraries
import pygame
import sys
import random
#Import packages
from CRUD.Menus import MainMenu as MM
from CRUD import Constants
from Classes import BackGround as BG
pygame.init()
pygame.mixer.quit()

#------------------------------
def introduccion():
    #Definition of variables-----------------
    #music upload
    Screen = Constants.Screen
    Temporizador = 1200
    limit = random.randrange(20)
    i = 0
    Image = 1
    Video = []
    while Image <= 191:
        Temp = eval('pygame.transform.scale(pygame.image.load("Assets\Images\Introduction\ezgif-frame-'+ str(Image) +'.jpg"),[Constants.Width,Constants.Height])')
        Video.append(Temp)
        Image += 1
    
    IntroImage = pygame.image.load("Assets\Images\BackGrounds\Kings and Pigs.png")
    IntroImageScallated = pygame.transform.scale(IntroImage,(134*5,14*5))
    introduccion = False
    back = pygame.sprite.Group()
    Background1 = BG.Background([0,0],Video)
    back.add(Background1)
    
    while not introduccion:
        #event managment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT()

        if (limit >= 0) and (limit < 10 ):
            Screen.fill([255,255,255])
            Screen.blit(IntroImageScallated,[65,265])
        if (limit >= 10) and (limit < 20):
            Screen.fill([63,56,81])
            Screen.blit(IntroImageScallated,[65,265])

        if i == Temporizador:
            MM.Main_Menu(Screen)
            introduccion = True
        
        i += 1
        #update
        back.update()
        back.draw(Screen)
        pygame.display.update()
        pygame.display.flip()