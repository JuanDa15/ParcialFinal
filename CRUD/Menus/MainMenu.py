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

pygame.display.set_caption('Main Menu')
Screen = Constants.Screen
#------------------------------
def Main_Menu():
    #Definition of variables-----------------
    #music upload
    pygame.mixer.music.load("Assets\Sounds\Spring Village.ogg")
    pygame.mixer.music.play(-1)
    Click = False
    while True:
    
        #buttons coords
        Start = pygame.Rect(300,250,200,50)
        Creditos = pygame.Rect(300,310,200,50)
        Controles = pygame.Rect(300,370,200,50)
        Close = pygame.Rect(300,430,200,50) 

        #Draw in screen
        Screen.fill(Functions.SelectColor('Black'))  
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
        
        Click = SM.VolumeModule(Click,Screen)
        
        #event managment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sis.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
        #refresh
        #update
        Functions.draw_text('MAIN MENU',UF.TittleFont(40),Functions.SelectColor('White'),Screen,155.5,50)
        Functions.draw_text('START',UF.getArchive('ButtonFont'),Functions.SelectColor('White'),Screen,351,258.5)
        Functions.draw_text('CREDITS',UF.getArchive('ButtonFont'),Functions.SelectColor('White'),Screen,331.5,318.5)
        Functions.draw_text('CONTROLS',UF.getArchive('ButtonFont'),Functions.SelectColor('White'),Screen,319,378.5)
        Functions.draw_text('CLOSE',UF.getArchive('ButtonFont'),Functions.SelectColor('White'),Screen,353,438.5)
        pygame.display.update()
        pygame.display.flip()