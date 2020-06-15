#Import libraries
import pygame
import sys
#Import Packages
from Functions import MenuFunctions as MF
from GUI import MainMenu as MM
from Functions import UploadesFiles as UF
from Functions import SoundModule as SM
import Jugador
#Definition of constant
pygame.display.set_caption('Game Over')
Screen = pygame.display.set_mode([MF.getSpecifications()[0],MF.getSpecifications()[1]])

def lostMenu():
    #music upload
    pygame.mixer.music.load("Assets\Sounds\Game Over II.ogg")
    pygame.mixer.music.play(-1)
    #Definition of variables-----------------
    Click = False
    while True:
        #buttons
        MainMenu = pygame.Rect(440,250,200,50)
        StarAgain = pygame.Rect(440,310,200,50)
        #Draw in screen
        Screen.fill(MF.SelectColor('Black'))
        MF.MakeImage(0,0,Screen,UF.getArchive('LoseBackGround')) 
        MF.MakeImage(440,250,Screen,UF.getArchive('ButtonImage'))
        MF.MakeImage(440,310,Screen,UF.getArchive('ButtonImage'))
        MF.MakeImage(400,370,Screen,UF.getArchive('LoseSkeleton'))
        #get mouse position--------------
        [mouse_x , mouse_y] = pygame.mouse.get_pos()
        
        if MainMenu.collidepoint ([mouse_x,mouse_y]):
            MF.MakeImage(440,250,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                MM.Main_Menu()
        if StarAgain.collidepoint ([mouse_x,mouse_y]):
            MF.MakeImage(440,310,Screen,UF.getArchive('ButtonSelectedImage'))
            if Click:
                Jugador.game(Screen)
                Click = False
                
        Click = SM.VolumeModule(Click,Screen)
