#Import Libraries
import sys
import pygame
#Import Packages
from CRUD import Functions
from CRUD.Menus import MainMenu
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM

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
        Back = pygame.Rect(110,610,100,50)
        
        #LOAD ELEMENTS
        Screen.fill(Functions.SelectColor('Black'))
        Functions.MakeImage(100,50,Screen,UF.getArchive('Container'))
        Functions.MakeImage(110,610,Screen,UF.getArchive('BackImage'))
        Functions.draw_text('CREDITS',UF.TittleFont(50),Functions.SelectColor('Orange'),Screen,290,50)
        Functions.draw_text('SPECIAL THANKS TO: ',UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,398,180)
        Functions.draw_text('JHONATAN OSPINA OSORIO ',UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,358,250)
        Functions.draw_text('ESTEBAN SANCHEZ LOPEZ',UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,372.5,290)
        Functions.draw_text('JUAN DAVID OSORIO ORTIZ',UF.getArchive('TextFont'),Functions.SelectColor('Orange'),Screen,364.5,330)
        
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if Back.collidepoint(mouse_x,mouse_y):
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
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
        #REFRESH SCREEN
        pygame.display.update()
        pygame.display.flip()