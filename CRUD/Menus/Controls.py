#Import Libraries
import sys
import pygame
#Import packages
from GUI import MainMenu
from Classes import background as BG
from Functions import MenuFunctions as MF
from Functions import UploadesFiles as UF
from Functions import SoundModule as SM

def ControlsScreen(Screen):
    #Definition of variables-----------------
    pygame.display.set_caption('Controls')
    Click = False
    running = True
    back = pygame.sprite.Group()
    Background1 = BG.Background([0,0],MF.getSpecifications()[0],MF.getSpecifications()[1])
    back.add(Background1)
    while running:
        #BUTTONS COORDS
        BackButton = pygame.Rect(110,610,100,50)
        #LOAD ELEMENTS
        Screen.fill(MF.SelectColor('Black'))
        back.update()
        back.draw(Screen)
        MF.MakeImage(100,50,Screen,UF.getArchive('Container'))
        MF.MakeImage(110,610,Screen,UF.getArchive('BackImage'))
        MF.draw_text('CONTROLS',UF.TittleFont(50),MF.SelectColor('Orange'),Screen,290,50)
        MF.MakeImage(150,200,Screen,UF.getArchive('LeftArrow'))
        MF.draw_text('WALK BACKWARDS',UF.getArchive('TextFont'),MF.SelectColor('Orange'),Screen,260,250)
        MF.MakeImage(150,325,Screen,UF.getArchive('RightArrow'))
        MF.draw_text('WALK FORWARD',UF.getArchive('TextFont'),MF.SelectColor('Orange'),Screen,260,375)
        MF.MakeImage(150,450,Screen,UF.getArchive('Ckey'))
        MF.draw_text('HIT',UF.getArchive('TextFont'),MF.SelectColor('Orange'),Screen,260,500)
        MF.MakeImage(600,200,Screen,UF.getArchive('Bkey'))
        MF.draw_text('PLASMA SHOOT',UF.getArchive('TextFont'),MF.SelectColor('Orange'),Screen,710,250)
        MF.MakeImage(600,325,Screen,UF.getArchive('Ekey'))
        MF.draw_text('PICK UP',UF.getArchive('TextFont'),MF.SelectColor('Orange'),Screen,710,375)
        
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if BackButton.collidepoint(mouse_x,mouse_y):
            MF.MakeImage(110,610,Screen,UF.getArchive('BackImageSelected'))
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