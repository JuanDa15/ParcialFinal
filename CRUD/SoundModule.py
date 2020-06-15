import pygame
from CRUD import UploadedFiles as UF
from CRUD import Functions

def VolumeModule(Click,Screen):
    volume = pygame.mixer.music.get_volume()
    [mouse_x , mouse_y] = pygame.mouse.get_pos()
    
    MusicOff = pygame.Rect(730,250,40,40)
    MusicOn = pygame.Rect(730,310,40,40)
    Mas = pygame.Rect(730,370,280,40)
    Menos = pygame.Rect(730,430,40,40)
    
    Functions.MakeImage(730,250,Screen,UF.getArchive('SoundOffImg'))
    Functions.MakeImage(730,310,Screen,UF.getArchive('SoundOnImg'))
    Functions.MakeImage(730,370,Screen,UF.getArchive('SoundUpImg'))
    Functions.MakeImage(730,430,Screen,UF.getArchive('SoundDownImg'))

    if MusicOff.collidepoint([mouse_x,mouse_y]):
        Functions.MakeImage(730,250,Screen,UF.getArchive('SoundOffSelectedImg'))
        if Click:
            pygame.mixer.music.pause()
            Click = False
            return Click
    if MusicOn.collidepoint([mouse_x,mouse_y]):
        Functions.MakeImage(730,310,Screen,UF.getArchive('SoundOnSelectedImg'))
        if Click:
            pygame.mixer.music.unpause()
            Click = False
            return Click
    if Mas.collidepoint([mouse_x,mouse_y]):
        Functions.MakeImage(730,370,Screen,UF.getArchive('SoundUpSelectedImg'))
        if Click:
            volume = volume + 0.1
            Click  = False
            if volume > 1:
                volume = 1
            pygame.mixer.music.set_volume(volume)
            return Click
    if Menos.collidepoint([mouse_x,mouse_y]):
        Functions.MakeImage(730,430,Screen,UF.getArchive('SoundDownSelectedImg'))
        if Click:
            volume = volume - 0.1
            Click  = False
            if volume < 0:
                volume = 0
            pygame.mixer.music.set_volume(volume)
            return Click