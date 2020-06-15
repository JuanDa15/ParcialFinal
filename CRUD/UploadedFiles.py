#Librarie Imports
#PYGAME INITIALIZATION
#Todos los archivos utilizados por el menu y demas ventanas
import pygame
from pygame.locals import *
pygame.init()

#Font Imports
ButtonFont = pygame.font.Font("Assets\Fonts\pixel dead.ttf", 35)
TextFont= pygame.font.Font("Assets\Fonts\pixelmix_bold.ttf", 20)
#buttons Sprites Imports
ButtonImage = pygame.image.load("Assets\Images\MenuImages\Button.png")
ButtonSelectedImage = pygame.image.load("Assets\Images\MenuImages\SelectedButton.png")
SoundOnImg = pygame.image.load("Assets\Images\MenuImages\Sound-On.png")
SoundOnSelectedImg = pygame.image.load("Assets\Images\MenuImages\Sound-OnSelected.png")
SoundOffImg = pygame.image.load("Assets\Images\MenuImages\Sound-Off.png")
SoundOffSelectedImg = pygame.image.load("Assets\Images\MenuImages\Sound-OffSelected.png")
SoundUpImg = pygame.image.load("Assets\Images\MenuImages\Sound-Up.png")
SoundUpSelectedImg = pygame.image.load("Assets\Images\MenuImages\Sound-UpSelected.png")
SoundDownImg = pygame.image.load("Assets\Images\MenuImages\Sound-Down.png")
SoundDownSelectedImg = pygame.image.load("Assets\Images\MenuImages\Sound-DownSelected.png")
BackImage = pygame.image.load("Assets\Images\MenuImages\Back-Arrow.png")
BackImageSelected = pygame.image.load("Assets\Images\MenuImages\Back-ArrowSelected.png")
NextImage = pygame.image.load(r"Assets\Images\MenuImages\Next-Button.png")
NextImageSelected = pygame.image.load(r"Assets\Images\MenuImages\Next-Buttonselected.png")
background1 = pygame.image.load("Assets\Images\BackGrounds\Pantalla principal.png")
#Images
Container = pygame.image.load("Assets\Images\MenuImages\Contenedor.png")
LeftArrow =pygame.image.load("Assets\Images\MenuImages\Left-Arrow.png")
RightArrow = pygame.image.load("Assets\Images\MenuImages\Right-Arrow.png")
Ckey = pygame.image.load("Assets\Images\MenuImages\C.png")
Ekey = pygame.image.load("Assets\Images\MenuImages\E.png")
Bkey = pygame.image.load("Assets\Images\MenuImages\B.png")

def TittleFont(Size):
    TittleFont = pygame.font.Font("Assets\Fonts\Pixelmania.ttf", Size)
    return TittleFont

def TextFont(Size):
    textFont = pygame.font.Font("Assets\Fonts\pixelmix_bold.ttf", Size)
    return textFont

def getArchive(ArchiveID):
    if ArchiveID == 'TittleFont':
        return TittleFont
    if ArchiveID == 'ButtonFont':
        return ButtonFont
    if ArchiveID == 'TextFont':
        return TextFont
    if ArchiveID == 'ButtonImage':
        return ButtonImage
    if ArchiveID == 'ButtonSelectedImage':
        return ButtonSelectedImage
    if ArchiveID == 'SoundOnImg':
        return SoundOnImg
    if ArchiveID == 'SoundOnSelectedImg':
        return SoundOnSelectedImg
    if ArchiveID == 'SoundOffImg':
        return SoundOffImg
    if ArchiveID == 'SoundOffSelectedImg':
        return SoundOffSelectedImg
    if ArchiveID == 'SoundUpImg':
        return SoundUpImg
    if ArchiveID == 'SoundUpSelectedImg':
        return SoundUpSelectedImg
    if ArchiveID == 'SoundDownImg':
        return SoundDownImg
    if ArchiveID == 'SoundDownSelectedImg':
        return SoundDownSelectedImg
    if ArchiveID == 'Container':
        return Container
    if ArchiveID == 'BackImage':
        return BackImage
    if ArchiveID == 'BackImageSelected':
        return BackImageSelected
    if ArchiveID == 'LeftArrow':
        return LeftArrow
    if ArchiveID == 'RightArrow':
        return RightArrow
    if ArchiveID == 'Ckey':
        return Ckey
    if ArchiveID == 'Ekey':
        return Ekey
    if ArchiveID == 'Bkey':
        return Bkey
    if ArchiveID == 'NextImage':
        return NextImage
    if ArchiveID == 'NextImageSelected':
        return NextImageSelected
    if ArchiveID == 'background1':
        return background1