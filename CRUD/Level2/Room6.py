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
    mapa = Constants.mapa2F

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()

    #Definicion Posicion inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de los bloques
    for i in range(len(Constants.WallsF)):
        Temporal = Block.Bloque([(Constants.WallsF[i]['x']),(Constants.WallsF[i]['y'])],Constants.WallsF[i]['width'],Constants.WallsF[i]['height'])
        Blocks.add(Temporal)
    
    #Asignacion colisiones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    return [Players, Blocks, None, None, None, None, None, None, None, None, None, None, Constants.Clock, mapa, 7, '5', '7', '2', '6']
