#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Block
from Classes import Door as Do

from pygame.locals import *

def StartRoom(Player, Players ,PositionX ,PositionY):
    mapa = Constants.MapaFinalA

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Doors = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de las paredes
    for i in range(len(Constants.WallsFinalBoss)):
        Temporal = Block.Bloque([(Constants.WallsFinalBoss[i]['x']),(Constants.WallsFinalBoss[i]['y'])],Constants.WallsFinalBoss[i]['width'],Constants.WallsFinalBoss[i]['height'])
        Blocks.add(Temporal)

    #Asignacion de lista de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    for i in range(len(Constants.DoorFinalBoss)):
        Temporal = Do.Door([(Constants.DoorFinalBoss[i]['x']),(Constants.DoorFinalBoss[i]['y'])],Constants.DoorFinalBoss[i]['width'],Constants.DoorFinalBoss[i]['height'],'210')
        Doors.add(Temporal)
    
        #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, None, None, None, None, None, None, Doors, None, None, None, Constants.Clock, mapa, 0, None,'2','3','1']