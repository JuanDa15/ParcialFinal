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

def StartRoom(Player, Players, PositionX, PositionY):

    mapa = Constants.mapa2A

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY
    
    #Creacion de los bloques
    for i in range(len(Constants.WallsA)):
        Temporal = Block.Bloque([(Constants.WallsA[i]['x']),(Constants.WallsA[i]['y'])],Constants.WallsA[i]['width'],Constants.WallsA[i]['height'])
        Blocks.add(Temporal)

    #Asignacion de bloques a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, None, None, None, None, None, None, None, None, None, None,Constants.Clock, mapa, 3, None, '2', '2', '1']
