#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Block
from Classes import Cannon as ca
from Classes import Ladder as La
from Classes import Lava
from Classes import Water
from Classes import Door as Do

from pygame.locals import *

def StartRoom(Player, Players ,PositionX ,PositionY):
    mapa = Constants.MapaFinalB

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()
    Ladders = pygame.sprite.Group()
    LavaG = pygame.sprite.Group()
    WaterG = pygame.sprite.Group()
    Doors = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY
    
    #Water
    for i in range(len(Constants.WaterPosFB)):
        Temporal = Water.Water([(Constants.WaterPosFB[i]['x']),(Constants.WaterPosFB[i]['y'])], Constants.WaterPosFB[i]['width'],Constants.WaterPosFB[i]['height'])
        WaterG.add(Temporal)

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
    
    for i in range(len(Constants.LaddersFinalBoss)):
        Temporal = La.Ladder([(Constants.LaddersFinalBoss[i]['x']-635),(Constants.LaddersFinalBoss[i]['y'])],Constants.LaddersFinalBoss[i]['width'],Constants.LaddersFinalBoss[i]['height'])
        Ladders.add(Temporal)
    
    for i in range(len(Constants.LavaPosFB)):
        Temporal = Lava.Lava([(Constants.LavaPosFB[i]['x']),(Constants.LavaPosFB[i]['y'])], Constants.LavaPosFB[i]['width'],Constants.LavaPosFB[i]['height'])
        LavaG.add(Temporal)
    
    for i in range(len(Constants.DoorPosFB)):
        Temporal = Do.Door([(Constants.DoorPosFB[i]['x']),(Constants.DoorPosFB[i]['y'])],Constants.DoorPosFB[i]['width'],Constants.DoorPosFB[i]['height'],'31')
        Doors.add(Temporal)
    
    
        #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, None, None, Cannons, Ladders, LavaG, WaterG, Doors, None, None, None, Constants.Clock, mapa, 8, None,None,'3','2']