#Import libraries
import pygame
import sys
#Import Packages
from CRUD import Functions
from CRUD.Menus import MainMenu as MM
from CRUD import UploadedFiles as UF
from CRUD import SoundModule as SM

#------------------------------
def Victory_Menu(Screen):
    #music upload
    pygame.mixer.music.load("Assets\Sounds\winner.ogg")
    pygame.mixer.music.play(-1)
    #Definition of variables-----------------
    Click = False
    while True:
        #buttons
        MainMenu = pygame.Rect(300,110,200,50)
        StarAgain = pygame.Rect(300,170,200,50)
        #Draw in screen
        Screen.fill(Functions.SelectColor('Black'))   
        Functions.MakeImage(300,110,Screen,UF.getArchive('ButtonImage'))
        Functions.MakeImage(300,170,Screen,UF.getArchive('ButtonImage'))
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if MainMenu.collidepoint ([mouse_x,mouse_y]):
            Functions.MakeImage(300,110,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                MM.Main_Menu()
                Click = False
        if StarAgain.collidepoint ([mouse_x,mouse_y]):
            Functions.MakeImage(300,170,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                pass
                Click = False
        
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
        Functions.draw_text('YOU WIN',UF.TittleFont(50),Functions.SelectColor('White'),Screen,174,400)
        Functions.draw_text('MAIN MENU',UF.getArchive('ButtonFont'),Functions.SelectColor('White'),Screen,310,118.5)
        Functions.draw_text('RESTART',UF.getArchive('ButtonFont'),Functions.SelectColor('White'),Screen,332,178.5)
        pygame.display.update()
        pygame.display.flip()
