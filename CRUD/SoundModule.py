import pygame
from CRUD import UploadedFiles as UF
from CRUD import Functions

def VolumeModule(Click,Screen,Sprites,SpritesSelected):
    volume = pygame.mixer.music.get_volume()
    [mouse_x , mouse_y] = pygame.mouse.get_pos()
    
    MusicOff = pygame.Rect(751,260,40,40)
    MusicOn = pygame.Rect(751,315,40,40)
    Mas = pygame.Rect(751,370,280,40)
    Menos = pygame.Rect(751,425,40,40)
    
    Functions.MakeImage(751,260,Screen,Sprites[0])
    Functions.MakeImage(751,315,Screen,Sprites[1])
    Functions.MakeImage(751,370,Screen,Sprites[2])
    Functions.MakeImage(751,425,Screen,Sprites[3])

    if MusicOff.collidepoint([mouse_x,mouse_y]):
        Functions.MakeImage(757,255,Screen,SpritesSelected[0])
        if Click:
            pygame.mixer.music.pause()
            Click = False
            return Click
    if MusicOn.collidepoint([mouse_x,mouse_y]):
        Functions.MakeImage(757,315,Screen,SpritesSelected[1])
        if Click:
            pygame.mixer.music.unpause()
            Click = False
            return Click
    if Mas.collidepoint([mouse_x,mouse_y]):
        Functions.MakeImage(757,370,Screen,SpritesSelected[2])
        if Click:
            volume = volume + 0.1
            Click  = False
            if volume > 1:
                volume = 1
            pygame.mixer.music.set_volume(volume)
            return Click
    if Menos.collidepoint([mouse_x,mouse_y]):
        Functions.MakeImage(757,430,Screen,SpritesSelected[3])
        if Click:
            volume = volume - 0.1
            Click  = False
            if volume < 0:
                volume = 0
            pygame.mixer.music.set_volume(volume)
            return Click