#Import Libraries
import sys
import pygame
#Import Packages
from CRUD import Functions
from CRUD.Menus import MainMenu
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM
from CRUD.Menus import Credits2

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
        Next = pygame.Rect(650,530,100,50)
        
        #LOAD ELEMENTS
        Screen.fill(Functions.SelectColor(r'Black'))
        Functions.MakeImage(50,25,Screen,UF.getArchive('Container'))
        Functions.MakeImage(55,530,Screen,UF.getArchive('BackImage'))
        Functions.MakeImage(650,530,Screen,UF.getArchive('NextImage'))
        Functions.draw_text('CREDITS',UF.TittleFont(25),Functions.SelectColor('Orange'),Screen,274.5,40)
        Functions.draw_text('DEVELOPERS: ',UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,312,120)
        Functions.draw_text('JHONATAN OSPINA OSORIO ',UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,218,150)
        Functions.draw_text('JUAN DAVID OSORIO ORTIZ',UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,224.5,180)
        Functions.draw_text('ESTEBAN SANCHEZ LOPEZ',UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,232.5,210)
        Functions.draw_text('SPECIAL THANKS TO:', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,264.5,250)
        Functions.draw_text('PIXEL FROG - KING AND PIGS ASSET PACK', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,117,280)
        Functions.draw_text('PIXEL FROG - PIRATE BOMB ASSET PACK', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,133,310)
        Functions.draw_text('BLACKSPIRE STUDIO - MEDIEVAL PIXEL ART ASSET', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,66.5,340)
        Functions.draw_text('ELTHENS PIXEL ART SHOP - MINOTAUR SPRITES', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,84,370)
        Functions.draw_text('FREE GAME ASSETS - SWAMP 2D TILESET', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,128,400)
        Functions.draw_text('BIGBUCKBUNNY - PLATFORMER ASSETS PACK', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,104,430)
        Functions.draw_text('PIXELYZR - MYTHICAL DUNGEON TILESET', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,127.5,460)
        Functions.draw_text('PIXELYZR - DECORATIONS FOR MYTHICAL TILESET', UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,70.5,490)
        
        
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if Back.collidepoint(mouse_x,mouse_y):
            Functions.MakeImage(55,530,Screen,UF.getArchive('BackImageSelected'))
            if Click:
                MainMenu.Main_Menu()
        if Next.collidepoint(mouse_x,mouse_y):
            Functions.MakeImage(650,530,Screen,UF.getArchive('NextImageSelected'))
            if Click:
                Credits2.Credits(Screen)
                
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