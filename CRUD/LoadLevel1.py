#Libraries Import
import pygame
import json
#Packages Import
from CRUD import Functions
from CRUD import Constants

L1map = pygame.image.load('Assets\Maps\Level1\Level1.png')
FileName ='Assets\Maps\Level1\Level1.json'
mapInfo = None

#Extract .json map information in mapInfo
with open(FileName) as information:
    mapInfo=json.load(information)
information.close()

wallCollisions = mapInfo['layers'][8]['objects']
waterLimits = mapInfo['layers'][9]['objects']
TreeCollisions = mapInfo['layers'][10]['objects']
SwampArea = mapInfo['layers'][11]['objects']
EndPoint = mapInfo['layers'][12]['objects']
StartPoint = mapInfo['layers'][13]['objects']

    
def GetStartPoint():
    Xposition = 100 + StartPoint[0]['x']
    Yposition = 50 + StartPoint[0]['y']
    return [Xposition,Yposition]

def GetCollisions():
    return wallCollisions
