#Import Libraries
import sys
import pygame
#Import Packages
from CRUD import Functions
from CRUD.Menus import MainMenu
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM
from CRUD.Menus import Credits as C

def Credits(Screen):
    pygame.display.set_caption('Credits')
    #Load and play Music
    pygame.mixer.music.load("Assets\Sounds\credits.ogg")
    pygame.mixer.music.play(-1)
    #Definition of variables-----------------
    Click = False
    running = True
    while running:
        #BUTTONS COORDS
        Back = pygame.Rect(55,530,100,50)
        
        #LOAD ELEMENTS
        Screen.fill(Functions.SelectColor('Black'))
        Functions.MakeImage(50,25,Screen,UF.getArchive('Container'))
        Functions.MakeImage(55,530,Screen,UF.getArchive('BackImage'))
        Functions.draw_text('PIXELYZR - ROCKY GRASS TILESET', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,170.5,50)
        Functions.draw_text('PIXELYZR - ROCKY SLABS TILESET', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,170.5,80)
        Functions.draw_text('ELTHENS PIXEL ART SHOP - CYCLOPS SPRITES', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,94,110)
        Functions.draw_text('ELTHENS PIXEL ART SHOP - WITCH SPRITES', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,110.5,140)
        Functions.draw_text('ELTHENS PIXEL ART SHOP - COBRA SPRITES', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,110.5,170)
        
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if Back.collidepoint(mouse_x,mouse_y):
            Functions.MakeImage(55,530,Screen,UF.getArchive('BackImageSelected'))
            if Click:
                C.Credits(Screen)
                
        Click = SM.VolumeModule(Click,Screen)
        #event managment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
        #REFRESH SCREEN
        pygame.display.update()
        pygame.display.flip()