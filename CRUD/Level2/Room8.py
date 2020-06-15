#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Door as Do
from Classes import Player as P
from Classes import Block

from pygame.locals import *

def StartRoom(Player ,Players ,PositionX , PositionY):
    mapa = Constants.mapa2H

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Doors = pygame.sprite.Group()

    #Definicion de Grupos
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de los bloques
    for i in range(len(Constants.WallsH)):
        Temporal = Block.Bloque([(Constants.WallsH[i]['x']),(Constants.WallsH[i]['y'])],Constants.WallsH[i]['width'],Constants.WallsH[i]['height'])
        Blocks.add(Temporal)
    
    #Asignacion de las coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    
    for i in range(len(Constants.DoorPos2H)):
        Temporal = Do.Door([(Constants.DoorPos2H[i]['x']),(Constants.DoorPos2H[i]['y'])],Constants.DoorPos2H[i]['width'],Constants.DoorPos2H[i]['height'],'27')
        Doors.add(Temporal)

    return [Players, Blocks, None, None, None, None, None, None, Doors, None, None, None, Constants.Clock, mapa, 0, '7', '9','2', '8']
