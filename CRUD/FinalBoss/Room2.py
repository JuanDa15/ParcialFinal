#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Block
from Classes import Cannon as ca

from pygame.locals import *

def StartRoom(Player, Players ,PositionX ,PositionY):
    mapa = Constants.MapaFinalB

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()


    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de las paredes
    for i in range(len(Constants.WallsFinalBossB)):
        Temporal = Block.Bloque([(Constants.WallsFinalBossB[i]['x']),(Constants.WallsFinalBossB[i]['y'])],Constants.WallsFinalBossB[i]['width'],Constants.WallsFinalBossB[i]['height'])
        Blocks.add(Temporal)

     #Creacion de cañones
    #Creacion de los cañones
    for i in range(len(Constants.CannonsPosFB)):
        if Constants.CannonsPosFB[i]['name'] == 'False':
            Temporal = Block.Bloque([(Constants.CannonsPosFB[i]['x']),(Constants.CannonsPosFB[i]['y'])],Constants.CannonsPosFB[i]['width'],Constants.CannonsPosFB[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosFB[i]['x']),(Constants.CannonsPosFB[i]['y'])],Constants.CannonIDLEL,1)
            Blocks.add(Temporal)
            Cannons.add(Temp)
        else:
            Temporal = Block.Bloque([(Constants.CannonsPosFB[i]['x']),(Constants.CannonsPosFB[i]['y'])],Constants.CannonsPosFB[i]['width'],Constants.CannonsPosFB[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosFB[i]['x']),(Constants.CannonsPosFB[i]['y'])],Constants.CannonIDLER,0)
            Blocks.add(Temporal)
            Cannons.add(Temp)

    #Asignacion de lista de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    
        #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, None, None, Cannons, None, None, None, None, None, None, None, Constants.Clock, mapa, 8, None,None,'3','2']