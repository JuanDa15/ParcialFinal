#Import libraries
import pygame
import sys
#Import Packages
from CRUD import Functions
from CRUD.Menus import MainMenu as MM
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM
from CRUD import Constants as C

def lostMenu(Screen):
    #music upload
    pygame.mixer.init()
    pygame.mixer.music.load("Assets\Sounds\Game Over II.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.001)
    #Definition of variables-----------------
    Click = False
    while True:
        #buttons
        MainMenu = pygame.Rect(300,250,200,50)
        StarAgain = pygame.Rect(300,310,200,50)
        #Draw in screen
        Screen.fill(Functions.SelectColor('Black'))
        Functions.MakeImage(0,0,Screen,UF.getArchive('background2'))
        Functions.MakeImage(50,25,Screen,UF.getArchive('Container'))
        Functions.MakeImage(300,250,Screen,UF.getArchive('ButtonImage'))
        Functions.MakeImage(300,310,Screen,UF.getArchive('ButtonImage'))
        Functions.MakeImage(300,450,Screen,C.KilledKing)
        Functions.MakeImage(390,380,Screen,C.KingPig)
        Functions.MakeImage(150,350,Screen,C.Minotaur)
        Functions.MakeImage(460,360,Screen,C.Cyclop)
        Functions.MakeImage(150,200,Screen,C.Witch)
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if MainMenu.collidepoint ([mouse_x,mouse_y]):
            Functions.MakeImage(300,250,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                MM.Main_Menu(Screen)
                Click = False
        if StarAgain.collidepoint ([mouse_x,mouse_y]):
            Functions.MakeImage(300,310,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                Click = False
                
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
                    pygame.quit()
                    sis.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
        #update
        Functions.draw_text('YOU DIE',UF.TittleFont(70),[63,56,81],Screen,89,50)
        Functions.draw_text('MAIN MENU',UF.getArchive('ButtonFont'),[63,56,81],Screen,309,258.5)
        Functions.draw_text('RESTART',UF.getArchive('ButtonFont'),[63,56,81],Screen,332,318.5)
        pygame.display.update()
        pygame.display.flip()
