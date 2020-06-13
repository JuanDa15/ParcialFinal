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

    mapa = Constants.mapa2J

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()

    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de los bloques
    for i in range(len(Constants.WallsJ)):
        Temporal = Block.Bloque([(Constants.WallsJ[i]['x']),(Constants.WallsJ[i]['y'])],Constants.WallsJ[i]['width'],Constants.WallsJ[i]['height'])
        Blocks.add(Temporal)

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    
    return [Players, Blocks, None, None, None, None, None, None, None, None, None ,None, Constants.Clock, mapa, 8, None, None, '2', '10']