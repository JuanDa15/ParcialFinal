#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Door as Do
from Classes import Player as P
from Classes import Water
from Classes import Block
from Classes import Lava

from pygame.locals import *

def StartRoom(Player ,Players ,PositionX , PositionY):

    mapa = Constants.mapa2J

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Doors = pygame.sprite.Group()
    WaterG = pygame.sprite.Group()
    LavaG = pygame.sprite.Group()

    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion Agua
    for i in range(len(Constants.WaterPosJ)):
        Temporal = Water.Water([(Constants.WaterPosJ[i]['x']),(Constants.WaterPosJ[i]['y'])], Constants.WaterPosJ[i]['width'],Constants.WaterPosJ[i]['height'])
        WaterG.add(Temporal)

    #Creacion de los bloques
    for i in range(len(Constants.WallsJ)):
        Temporal = Block.Bloque([(Constants.WallsJ[i]['x']),(Constants.WallsJ[i]['y'])],Constants.WallsJ[i]['width'],Constants.WallsJ[i]['height'])
        Blocks.add(Temporal)
    
    for i in range(len(Constants.LavaPosJ)):
        Temporal = Lava.Lava([(Constants.LavaPosJ[i]['x']),(Constants.LavaPosJ[i]['y'])], Constants.LavaPosJ[i]['width'],Constants.LavaPosJ[i]['height'])
        LavaG.add(Temporal)
    

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    
    for i in range(len(Constants.Door2j)):
        Temporal = Do.Door([(Constants.Door2j[i]['x']),(Constants.Door2j[i]['y'])],Constants.Door2j[i]['width'],Constants.Door2j[i]['height'],'31')
        Doors.add(Temporal)

    Enemies = pygame.sprite.Group()
    
    return [Players, Blocks, Enemies, None, None, None, LavaG, WaterG, Doors, None, None ,None, Constants.Clock, mapa, 8, None, None, '2', '10']
