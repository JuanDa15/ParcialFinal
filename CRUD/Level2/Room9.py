#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block

from pygame.locals import *

def StartRoom(Player ,Players ,PositionX , PositionY):
    mapa = Constants.mapa2I
    #Definicion de Grupos
    Blocks = pygame.sprite.Group()

    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de las colisiones
    for i in range(len(Constants.WallsI)):
        Temporal = Block.Bloque([(Constants.WallsI[i]['x']),(Constants.WallsI[i]['y'])],Constants.WallsI[i]['width'],Constants.WallsI[i]['height'])
        Blocks.add(Temporal)
    
    #Asignacion coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks


    return [Players, Blocks, None, None, None, None, None, None, None, None, None, None,  Constants.Clock, mapa, 1, '8', '10', 2, 9]
