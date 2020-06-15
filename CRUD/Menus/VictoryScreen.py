#Import libraries
import pygame
import sys
#Import Packages
from Functions import MenuFunctions as MF
from GUI import MainMenu as MM
from Classes import background as BG
from Functions import UploadesFiles as UF
from Functions import SoundModule as SM
#Definition of constant
pygame.display.set_caption('Victory')
Screen = pygame.display.set_mode([MF.getSpecifications()[0],MF.getSpecifications()[1]])
#------------------------------
def Victory_Menu():
    #music upload
    pygame.mixer.music.load("Assets\Sounds\winner.ogg")
    pygame.mixer.music.play(-1)
    #Definition of variables-----------------
    Click = False
    back = pygame.sprite.Group()
    Background1 = BG.Background([0,0],MF.getSpecifications()[0],MF.getSpecifications()[1])
    back.add(Background1)
    
    while True:
        #buttons
        MainMenu = pygame.Rect(440,110,200,50)
        StarAgain = pygame.Rect(440,170,200,50)
        #Draw in screen
        Screen.fill(MF.SelectColor('Black'))   
        back.update()
        back.draw(Screen)
        MF.MakeImage(440,110,Screen,UF.getArchive('ButtonImage'))
        MF.MakeImage(440,170,Screen,UF.getArchive('ButtonImage'))
        MF.MakeImage(406,227,Screen,UF.getArchive('VictorySkeleton'))
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if MainMenu.collidepoint ([mouse_x,mouse_y]):
            MF.MakeImage(440,110,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                MM.Main_Menu()
                Click = False
        if StarAgain.collidepoint ([mouse_x,mouse_y]):
            MF.MakeImage(440,170,Screen,UF.getArchive('ButtonSelectedImage'))
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
        MF.draw_text('YOU WIN',UF.TittleFont(50),MF.SelectColor('White'),Screen,314,500)
        MF.draw_text('MAIN MENU',UF.getArchive('ButtonFont'),MF.SelectColor('White'),Screen,450.5,118.5)
        MF.draw_text('RESTART',UF.getArchive('ButtonFont'),MF.SelectColor('White'),Screen,471,178.5)
        pygame.display.flip()
