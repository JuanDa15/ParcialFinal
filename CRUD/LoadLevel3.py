#Libraries Import
import pygame
import json
#Packages Import
from CRUD import Functions
from CRUD import Constants

L3map = pygame.image.load('Assets\Maps\Level3\Level3.png')
FileName ='Assets\Maps\Level3\Level3.json'
mapInfo = None

#Extract .json map information in mapInfo
with open(FileName) as information:
    mapInfo=json.load(information)
information.close()

wallCollisions = mapInfo['layers'][6]['objects']
Traps  = mapInfo['layers'][7]['objects']
Gems = mapInfo['layers'][8]['objects']
MushRooms = mapInfo['layers'][9]['objects']
Holes = mapInfo['layers'][10]['objects']
StartPoint = mapInfo['layers'][11]['objects']
EndPoint = mapInfo['layers'][12]['objects']

def GetStartPoint():
    Xposition = 100 + StartPoint[0]['x']
    Yposition = 50 + StartPoint[0]['y']
    return [Xposition,Yposition]

def GetTraps():
    return Traps