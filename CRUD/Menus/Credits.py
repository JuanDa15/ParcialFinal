#Import Libraries
import sys
import pygame
#Import Packages
from CRUD import Functions
from CRUD import Constants as C
from CRUD.Menus import MainMenu
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM
from CRUD.Menus import Credits2

def Credits(Screen):
    pygame.display.set_caption('King & Pigs - Credits')
    #Load and play Music
    pygame.mixer.music.load("Assets\Sounds\credits.ogg")
    pygame.mixer.music.play(-1)
    #Definition of variables-----------------
    Click = False
    running = True
    while running:
        #BUTTONS COORDS
        Back = pygame.Rect(55,530,100,50)
        Next = pygame.Rect(650,530,100,50)
        
        #LOAD ELEMENTS
        Screen.fill(Functions.SelectColor(r'Black'))
        Functions.MakeImage(0,0,Screen,UF.getArchive('background2'))
        Functions.MakeImage(50,25,Screen,UF.getArchive('Container'))
        Functions.MakeImage(55,530,Screen,UF.getArchive('BackImage'))
        Functions.MakeImage(650,530,Screen,UF.getArchive('NextImage'))
        #-----------------------------------------------------------------------
        Functions.draw_text('CREDITS',UF.TittleFont(25),[63,56,81],Screen,274.5,40)
        #------------------------------------------------------------------------------
        Functions.draw_text('DEVELOPERS: ',UF.TextFont(20),[63,56,81],Screen,312,100)
        Functions.draw_text('JHONATAN OSPINA OSORIO ',UF.TextFont(15),[63,56,81],Screen,273,130)
        Functions.draw_text('JUAN DAVID OSORIO ORTIZ',UF.TextFont(15),[63,56,81],Screen,277.5,150)
        Functions.draw_text('ESTEBAN SANCHEZ LOPEZ',UF.TextFont(15),[63,56,81],Screen,282.5,170)
        Functions.draw_text('SPECIAL THANKS TO ', UF.TittleFont(20),[63,56,81],Screen,166,200)
        Functions.draw_text('SPRITES CREATORS: ', UF.TextFont(20),[63,56,81],Screen,268,240)
        Functions.draw_text('PIXEL FROG - KING AND PIGS ASSET PACK', UF.TextFont(15),[63,56,81],Screen,202,270)
        Functions.draw_text('PIXEL FROG - PIRATE BOMB ASSET PACK',UF.TextFont(15),[63,56,81],Screen,213.5,290)
        Functions.draw_text('BLACKSPIRE STUDIO - MEDIEVAL PIXEL ART ASSET', UF.TextFont(15),[63,56,81],Screen,166,310)
        Functions.draw_text('ELTHENS PIXEL ART SHOP - MINOTAUR SPRITES',UF.TextFont(15),[63,56,81],Screen,179,330)
        Functions.draw_text('FREE GAME ASSETS - SWAMP 2D TILESET', UF.TextFont(15),[63,56,81],Screen,209,350)
        Functions.draw_text('BIGBUCKBUNNY - PLATFORMER ASSETS PACK', UF.TextFont(15),[63,56,81],Screen,193,370)
        Functions.draw_text('PIXELYZR - MYTHICAL DUNGEON TILESET', UF.TextFont(15),[63,56,81],Screen,208,390)
        Functions.draw_text('PIXELYZR - DECORATIONS FOR MYTHICAL TILESET', UF.TextFont(15),[63,56,81],Screen,168.5,410)
        Functions.draw_text('PIXELYZR - ROCKY GRASS TILESET', UF.TextFont(15),[63,56,81],Screen,239,430)
        Functions.draw_text('PIXELYZR - ROCKY SLABS TILESET', UF.TextFont(15),[63,56,81],Screen,239,450)
        Functions.draw_text('ELTHENS PIXEL ART SHOP - CYCLOPS SPRITES', UF.TextFont(15),[63,56,81],Screen,186,470)
        Functions.draw_text('ELTHENS PIXEL ART SHOP - WITCH SPRITES', UF.TextFont(15),[63,56,81],Screen,197.5,490)
        Functions.draw_text('ELTHENS PIXEL ART SHOP - COBRA SPRITES', UF.TextFont(15),[63,56,81],Screen,198,510)
        
        
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if Back.collidepoint(mouse_x,mouse_y):
            Functions.MakeImage(55,530,Screen,UF.getArchive('BackImageSelected'))
            if Click:
                return 0
        if Next.collidepoint(mouse_x,mouse_y):
            Functions.MakeImage(650,530,Screen,UF.getArchive('NextImageSelected'))
            if Click:
                Credits2.Credits(Screen)
        
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