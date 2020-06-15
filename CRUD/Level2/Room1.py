#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block
from Classes import Lava

from pygame.locals import *

def StartRoom(Player, Players, PositionX, PositionY):

    mapa = Constants.mapa2A

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    LavaG = pygame.sprite.Group()

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

    #Creacion Lava
    for i in range(len(Constants.LavaPosA)):
        Temporal = Lava.Lava([(Constants.LavaPosA[i]['x']),(Constants.LavaPosA[i]['y'])], Constants.LavaPosA[i]['width'],Constants.LavaPosA[i]['height'])
        LavaG.add(Temporal)
    #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, None, None, None, None, LavaG, None, None, None, None, None,Constants.Clock, mapa, 3, None, '2', '2', '1']
