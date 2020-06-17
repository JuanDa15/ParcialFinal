#Import of libraries
import pygame
import sys
#Import packages
from CRUD import Functions
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM
from CRUD import Constants
from CRUD.Menus import Credits
from CRUD.Menus import Controls

pygame.display.set_caption('King & Pigs')
#------------------------------
def Main_Menu(Screen):
    #Definition of variables-----------------
    #music upload
    pygame.mixer.init()
    pygame.mixer.music.load("Assets\Sounds\Spring Village.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.001)
    Click = False

    while True:
        #buttons coords
        Start = pygame.Rect(300,250,200,50)
        Creditos = pygame.Rect(300,310,200,50)
        Controles = pygame.Rect(300,370,200,50)
        Close = pygame.Rect(300,430,200,50) 

        #Draw in screen
        Screen.fill(Functions.SelectColor('Black'))  
        Functions.MakeImage(0,0,Screen,UF.getArchive('background1'))
        Functions.MakeImage(300,250,Screen,UF.getArchive('ButtonImage'))
        Functions.MakeImage(300,310,Screen,UF.getArchive('ButtonImage'))
        Functions.MakeImage(300,370,Screen,UF.getArchive('ButtonImage'))
        Functions.MakeImage(300,430,Screen,UF.getArchive('ButtonImage'))
       
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if Start.collidepoint ([mouse_x,mouse_y]):
            Functions.MakeImage(300,250,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                Click = False
                return 0
        if Creditos.collidepoint ([mouse_x,mouse_y]):
            Functions.MakeImage(300,310,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                Credits.Credits(Screen)
                Click = False
        if Controles.collidepoint ([mouse_x,mouse_y]):
            Functions.MakeImage(300,370,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                Controls.ControlsScreen(Screen)
                Click = False
        if Close.collidepoint([mouse_x,mouse_y]):
            Functions.MakeImage(300,430,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                pygame.quit()
                sys.exit()
        
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
        #refresh
        #update
        Functions.draw_text('MAIN MENU',UF.TittleFont(39),[251,202,151],Screen,160.5,30)
        Functions.draw_text('KING',UF.TittleFont(23),Functions.SelectColor('White'),Screen,8,375)
        Functions.draw_text('AND',UF.TittleFont(20),Functions.SelectColor('White'),Screen,25,415)
        Functions.draw_text('PIGS',UF.TittleFont(23),Functions.SelectColor('White'),Screen,8,450)
        Functions.draw_text('START',UF.getArchive('ButtonFont'),[63,56,81],Screen,351,258.5)
        Functions.draw_text('CREDITS',UF.getArchive('ButtonFont'),[63,56,81],Screen,331.5,318.5)
        Functions.draw_text('CONTROLS',UF.getArchive('ButtonFont'),[63,56,81],Screen,319,378.5)
        Functions.draw_text('CLOSE',UF.getArchive('ButtonFont'),[63,56,81],Screen,353,438.5)
        pygame.display.update()
        pygame.display.flip()