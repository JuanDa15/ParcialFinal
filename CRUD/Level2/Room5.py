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
    mapa = Constants.mapa2E

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de los bloques
    for i in range(len(Constants.WallsE)):
        Temporal = Block.Bloque([(Constants.WallsE[i]['x']),(Constants.WallsE[i]['y'])],Constants.WallsE[i]['width'],Constants.WallsE[i]['height'])
        Blocks.add(Temporal)
    
    #Asignacion de las coliciones a las entidades
    for Playeri in Players:
        Player.Bloques = Blocks
    
    return [Players, Blocks, None, None, None, None, None, None, None, None, None, None, Constants.Clock, mapa, 5, '4', '6', '2', '5']