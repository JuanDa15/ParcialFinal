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
from Classes import Brujas
from Classes import Lava
from Classes import Ladder as La
from Classes import Water

from pygame.locals import *

def StartRoom(Player, Players, PositionX, PositionY):

    mapa = Constants.mapa2A

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    LavaG = pygame.sprite.Group()
    WaterG = pygame.sprite.Group()
    Doors = pygame.sprite.Group()
    Ladders = pygame.sprite.Group()

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

    #Creacion Agua
    for i in range(len(Constants.WaterPosA)):
        Temporal = Water.Water([(Constants.WaterPosA[i]['x']),(Constants.WaterPosA[i]['y'])], Constants.WaterPosA[i]['width'],Constants.WaterPosA[i]['height'])
        WaterG.add(Temporal)
    #Creacion Lava
    for i in range(len(Constants.LavaPosA)):
        Temporal = Lava.Lava([(Constants.LavaPosA[i]['x']),(Constants.LavaPosA[i]['y'])], Constants.LavaPosA[i]['width'],Constants.LavaPosA[i]['height'])
        LavaG.add(Temporal)
        
    #Creacion Puertas
    for i in range(len(Constants.DoorPos2A)):
        Temporal = Do.Door([(Constants.DoorPos2A[i]['x']),(Constants.DoorPos2A[i]['y'])],Constants.DoorPos2A[i]['width'],Constants.DoorPos2A[i]['height'],'110')
        Doors.add(Temporal)
    #Creacion de escaleras
    for i in range(len(Constants.LaddersPosA)):
        Temporal = La.Ladder([(Constants.LaddersPosA[i]['x']),(Constants.LaddersPosA[i]['y'])],Constants.LaddersPosA[i]['width'],Constants.LaddersPosA[i]['height'])
        Ladders.add(Temporal)
    
    #Enemigos
    EnemysG = pygame.sprite.Group()
    for i in range(len(Constants.Enemys2A)):
        if Constants.Enemys2A[i]['name'] == 'BrujaE':
            Temp = pork.cerdo([(Constants.Enemys2A[i]['x']),(Constants.Enemys2A[i]['y'])-12],(Constants.Enemys2A[i]['properties'][0]['value']))
            EnemysG.add(Temp)
        elif Constants.Enemys2A[i]['name'] == 'BrujaP':
            Temp = Bomber.Bomber([(Constants.Enemys2A[i]['x']),(Constants.Enemys2A[i]['y'])],Constants.Bomber,1)
            EnemysG.add(Temp)

    #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, instakill, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, EnemysG, None, None, Ladders, LavaG, WaterG, Doors, None, None, None,Constants.Clock, mapa, 3, None, '2', '2', '1']
