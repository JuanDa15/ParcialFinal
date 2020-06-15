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
from Classes import Ladder as La

from pygame.locals import *

def StartRoom(Player ,Players ,PositionX , PositionY):

    mapa = Constants.mapa2G

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Doors = pygame.sprite.Group()
    Ladders = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY


    #Creacion de los bloques
    for i in range(len(Constants.WallsG)):
        Bloque = Block.Bloque([(Constants.WallsG[i]['x']),(Constants.WallsG[i]['y'])],Constants.WallsG[i]['width'],Constants.WallsG[i]['height'])
        Blocks.add(Bloque)
    

    #Asignacion de colisiones a las entidades
    for Playeri in Players:
        Player.Bloques = Blocks

    for i in range(len(Constants.DoorPos2G)):
        Temporal = Do.Door([(Constants.DoorPos2G[i]['x']),(Constants.DoorPos2G[i]['y'])],Constants.DoorPos2G[i]['width'],Constants.DoorPos2G[i]['height'],'28')
        Doors.add(Temporal)
    
    for i in range(len(Constants.LaddersPosFB)):
        Temporal = La.Ladder([(Constants.LaddersPosFB[i]['x']),(Constants.LaddersPosFB[i]['y'])],Constants.LaddersPosFB[i]['width'],Constants.LaddersPosFB[i]['height'])
        Ladders.add(Temporal)
    
    return [Players, Blocks, None, None, None, Ladders, None, None, Doors, None, None,None, Constants.Clock, mapa, 1, '6', '8', '2', '7']

        