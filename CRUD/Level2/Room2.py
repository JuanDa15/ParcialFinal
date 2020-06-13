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

    mapa = Constants.mapa2B

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    
    #Definicion posicion inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY
    
    #Creacion de las coliciones
    for i in range(len(Constants.WallsB)):
        Temporal = Block.Bloque([(Constants.WallsB[i]['x']),(Constants.WallsB[i]['y'])],Constants.WallsB[i]['width'],Constants.WallsB[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.Platforms2B)):
        Temporal = Block.Bloque([(Constants.Platforms2B[i]['x']),(Constants.Platforms2B[i]['y'])],Constants.Platforms2B[i]['width'],Constants.Platforms2B[i]['height'])
        Blocks.add(Temporal)

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    
    return [Players, Blocks, None, None, None, None, None, None, None, None, None, None, Constants.Clock, mapa, 3, '1', '3', '2', '2']