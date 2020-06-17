#Import Libraries
import sys
import pygame
#Import packages
from CRUD import Functions
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM
from CRUD.Menus import MainMenu

def ControlsScreen(Screen):
    #Definition of variables-----------------
    pygame.display.set_caption('Controls')
    Click = False
    running = True
    while running:
        #BUTTONS COORDS
        BackButton = pygame.Rect(55,530,100,50)
        #LOAD ELEMENTS
        Screen.fill(Functions.SelectColor('Black'))
        Functions.MakeImage(50,25,Screen,UF.getArchive('Container'))
        Functions.MakeImage(110,610,Screen,UF.getArchive('BackImage'))
        Functions.draw_text('CONTROLS',UF.TittleFont(25),Functions.SelectColor('Orange'),Screen,249.5,50)
        
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if BackButton.collidepoint(mouse_x,mouse_y):
            Functions.MakeImage(110,610,Screen,UF.getArchive('BackImageSelected'))
            if Click:
                MainMenu.Main_Menu()
                
        Click = SM.VolumeModule(Click,Screen)
        #event managment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
        #REFRESH SCREEN
        pygame.display.update()
        pygame.display.flip()