#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block
from Classes import Ladder as La

from pygame.locals import *

def StartRoom(Player, Players, PositionX, PositionY):

    mapa = Constants.mapa2D

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Ladders = pygame.sprite.Group()

    #Definicion Posicion inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de los bloques
    for i in range(len(Constants.WallsD)):
        Temporal = Block.Bloque([(Constants.WallsD[i]['x']),(Constants.WallsD[i]['y'])],Constants.WallsD[i]['width'],Constants.WallsD[i]['height'])
        Blocks.add(Temporal)

    #Asignacion colisiones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    
    for i in range(len(Constants.LaddersPosD)):
        Temporal = La.Ladder([(Constants.LaddersPosD[i]['x']),(Constants.LaddersPosD[i]['y'])],Constants.LaddersPosD[i]['width'],Constants.LaddersPosD[i]['height'])
        Ladders.add(Temporal)
    
    return [Players, Blocks, None, None, None, Ladders, None, None, None, None, None, None, Constants.Clock, mapa, 1, '3', '5', '2', '4']
