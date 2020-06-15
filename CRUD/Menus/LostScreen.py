#Import libraries
import pygame
import sys
#Import Packages
from CRUD import Functions
from CRUD.Menus import MainMenu as MM
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM

def lostMenu(Screen):
    #music upload
    pygame.mixer.music.load("Assets\Sounds\Game Over II.ogg")
    pygame.mixer.music.play(-1)
    #Definition of variables-----------------
    Click = False
    while True:
        #buttons
        MainMenu = pygame.Rect(300,250,200,50)
        StarAgain = pygame.Rect(300,310,200,50)
        #Draw in screen
        Screen.fill(Functions.SelectColor('Black'))
        Functions.MakeImage(300,250,Screen,UF.getArchive('ButtonImage'))
        Functions.MakeImage(300,310,Screen,UF.getArchive('ButtonImage'))
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if MainMenu.collidepoint ([mouse_x,mouse_y]):
            Functions.MakeImage(300,250,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                return 1
        if StarAgain.collidepoint ([mouse_x,mouse_y]):
            Functions.MakeImage(300,310,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                Click = False
                return 2
                
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
        #update
        Functions.draw_text('YOU DIE',UF.TittleFont(70),Functions.SelectColor('White'),Screen,89,50)
        Functions.draw_text('MAIN MENU',UF.getArchive('ButtonFont'),Functions.SelectColor('White'),Screen,309,258.5)
        Functions.draw_text('RESTART',UF.getArchive('ButtonFont'),Functions.SelectColor('White'),Screen,332,318.5)
        pygame.display.update()
        pygame.display.flip()
