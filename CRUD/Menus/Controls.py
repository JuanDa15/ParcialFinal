#Import Libraries
import sys
import pygame
#Import packages
from CRUD import Functions
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM
from CRUD.Menus import MainMenu as MM
from CRUD import Constants as C

def ControlsScreen(Screen):
    #Definition of variables-----------------
    pygame.mixer.init()
    pygame.display.set_caption('King & Pigs - Controls')
    pygame.mixer.music.load("Assets\Sounds\credits.ogg")
    pygame.mixer.music.play(-1)
    Click = False
    running = True
    while running:
        #BUTTONS COORDS
        Back = pygame.Rect(55,530,100,50)
        #LOAD ELEMENTS
        Screen.fill(Functions.SelectColor('Black'))
        Functions.MakeImage(0,0,Screen,UF.getArchive('background2'))
        Functions.MakeImage(50,25,Screen,UF.getArchive('Container'))
        Functions.MakeImage(55,530,Screen,UF.getArchive('BackImage'))
        Functions.draw_text('CONTROLS',UF.TittleFont(25),[63,56,81],Screen,249.5,40)
        Functions.MakeImage(75,110,Screen,C.Left_Arrow)
        Functions.draw_text('WALK LEFT',UF.TextFont(20),[63,56,81],Screen,149,128)
        Functions.MakeImage(75,180,Screen,C.Right_Arrow)
        Functions.draw_text('WALK RIGHT',UF.TextFont(20),[63,56,81],Screen,149,198)
        Functions.MakeImage(75,250,Screen,C.Up_Arrow)
        Functions.draw_text('CLIMB',UF.TextFont(20),[63,56,81],Screen,149,268)
        Functions.MakeImage(75,320,Screen,C.Space)
        Functions.draw_text('JUMP',UF.TextFont(20),[255,255,255],Screen,205,335)
        Functions.MakeImage(75,390,Screen,C.Q_Key)
        Functions.draw_text('EAT APPLE',UF.TextFont(20),[63,56,81],Screen,149,408)
        Functions.MakeImage(75,460,Screen,C.W_Key)
        Functions.draw_text('HIT',UF.TextFont(20),[63,56,81],Screen,149,478)
        Functions.draw_text('INTERACTION',UF.TextFont(20),[63,56,81],Screen,499,128)
        Functions.MakeImage(420,110,Screen,C.E_Key)
        
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if Back.collidepoint(mouse_x,mouse_y):
            Functions.MakeImage(55,530,Screen,UF.getArchive('BackImageSelected'))
            if Click:
                return 0
                
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