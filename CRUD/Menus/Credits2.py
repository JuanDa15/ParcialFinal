#Import Libraries
import sys
import pygame
#Import Packages
from CRUD import Functions
from CRUD.Menus import MainMenu
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM
from CRUD.Menus import Credits as cre
from CRUD import Constants as C

def Credits(Screen):
    pygame.display.set_caption('King & Pigs - Credits')
    pygame.mixer.init()
    pygame.mixer.music.load("Assets\Sounds\credits.ogg")
    pygame.mixer.music.play(-1)
    #Load and play Music
    #Definition of variables-----------------
    Click = False
    running = True
    while running:
        #BUTTONS COORDS
        Back = pygame.Rect(55,530,100,50)
        #LOAD ELEMENTS
        Screen.fill(Functions.SelectColor(r'Black'))
        Functions.MakeImage(0,0,Screen,UF.getArchive('background2'))
        Functions.MakeImage(50,25,Screen,UF.getArchive('Container'))
        Functions.MakeImage(55,530,Screen,UF.getArchive('BackImage'))
        Functions.draw_text('CHEEKYINKLING - SHIKASHIS FANTASY ICONS PACK', UF.TextFont(15),[63,56,81],Screen,156.5,60)
        Functions.draw_text('GREEN-PIXELS - 014 MERCHANT [ANIMATED] ', UF.TextFont(15),[63,56,81],Screen,188.5,80)
        Functions.draw_text('HYOHNOO - KEYBOARD AND CONTROLLER KEY ', UF.TextFont(15),[63,56,81],Screen,186,100)
        
    
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if Back.collidepoint(mouse_x,mouse_y):
            Functions.MakeImage(55,530,Screen,UF.getArchive('BackImageSelected'))
            if Click:
                cre.Credits(Screen)
                
        Sprites = [C.Sound_Off_2,C.Sound_On_2,C.Sound_Up_2,C.Sound_Dowm_2,]
        SelectedSprites = [C.Sound_Off_Selected_2,C.Sound_On_Selected_2,C.Sound_Up_Selected_2,C.Sound_Down_Selected_2]
        Click = SM.VolumeModule(Click,Screen,Sprites,SelectedSprites)
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