#Import libraries
import pygame
import sys
#Import Packages
from CRUD import Functions
from CRUD.Menus import MainMenu as MM
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM
from CRUD import Constants as C
import datetime

#------------------------------
def Victory_Menu(Screen):
    #music upload
    pygame.mixer.init()
    pygame.mixer.music.load("Assets\Sounds\winner.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    #Definition of variables-----------------
    Click = False
    while True:
        #buttons
        MainMenu = pygame.Rect(300,110,220,50)
        StarAgain = pygame.Rect(300,170,220,50)
        #Draw in screen 
        Screen.fill(Functions.SelectColor('Black'))
        Functions.MakeImage(0,0,Screen,UF.getArchive('background2'))
        Functions.MakeImage(50,25,Screen,UF.getArchive('Container'))
        Functions.MakeImage(300,110,Screen,UF.getArchive('ButtonImage'))
        Functions.MakeImage(300,170,Screen,UF.getArchive('ButtonImage'))
        Functions.MakeImage(300,326,Screen,C.DeadMinotair)
        Functions.MakeImage(485,350,Screen,C.Cyclopdead)
        Functions.MakeImage(220,350,Screen,C.KingPigDead)
        Functions.MakeImage(309,235,Screen,C.KingHuman)
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if MainMenu.collidepoint ([mouse_x,mouse_y]):
            Functions.MakeImage(300,110,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                pygame.mixer.music.stop()
                Click = False
                return 1
        if StarAgain.collidepoint ([mouse_x,mouse_y]):
            Functions.MakeImage(300,170,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                pygame.mixer.music.stop()
                Click = False
                return 2
        
        Sprites = [UF.getArchive('SoundOffImg'),UF.getArchive('SoundOnImg'),UF.getArchive('SoundUpImg'),UF.getArchive('SoundDownImg')]
        SpritesSelected = [UF.getArchive('SoundOffSelectedImg'),UF.getArchive('SoundOnSelectedImg'),UF.getArchive('SoundUpSelectedImg'),UF.getArchive('SoundDownSelectedImg')]
        Click = SM.VolumeModule(Click,Screen,Sprites,SpritesSelected)
        
        #event managment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sis.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
        #update
        Functions.draw_text('YOU WIN',UF.TittleFont(50),[63,56,81],Screen,174,400)
        Functions.draw_text('MAIN MENU',UF.getArchive('ButtonFont'),[63,56,81],Screen,310,118.5)
        Functions.draw_text('RESTART',UF.getArchive('ButtonFont'),[63,56,81],Screen,332,178.5)
        Functions.draw_text(' Total Coins: '+str(C.Total_Monedas),UF.TextFont(16),Functions.SelectColor('Black'),C.Screen,70+35,220+20)
        Functions.draw_text(' Total Diamonds: '+str(C.Total_Diamantes),UF.TextFont(16),Functions.SelectColor('Black'),C.Screen,70+35,220+40)
        Functions.draw_text(' Total Apples: '+str(C.Total_Manzanas),UF.TextFont(16),Functions.SelectColor('Black'),C.Screen,70+35,220+60)
        Functions.draw_text(' Time: '+C.Total_Time,UF.TextFont(16),Functions.SelectColor('Black'),C.Screen,70+35,220)
        Functions.draw_text(' SCORE: '+str(C.Total_Monedas*10 + C.Total_Diamantes*50 + C.Total_Manzanas*5 - C.Total_Minutos*5),UF.TextFont(16),Functions.SelectColor('Black'),C.Screen,70+35,220+90)
        pygame.display.update()
        pygame.display.flip()
