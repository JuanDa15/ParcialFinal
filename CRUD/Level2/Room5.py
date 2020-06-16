#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Water
from Classes import Brujas
from Classes import Block
from Classes import Ladder as La

from pygame.locals import *

def StartRoom(Player ,Players ,PositionX , PositionY):
    mapa = Constants.mapa2E

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Ladders = pygame.sprite.Group()
    WaterG = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion Agua
    for i in range(len(Constants.WaterPosE)):
        Temporal = Water.Water([(Constants.WaterPosE[i]['x']),(Constants.WaterPosE[i]['y'])], Constants.WaterPosE[i]['width'],Constants.WaterPosE[i]['height'])
        WaterG.add(Temporal)

    #Creacion de los bloques
    for i in range(len(Constants.WallsE)):
        Temporal = Block.Bloque([(Constants.WallsE[i]['x']),(Constants.WallsE[i]['y'])],Constants.WallsE[i]['width'],Constants.WallsE[i]['height'])
        Blocks.add(Temporal)
    
    #Asignacion de las coliciones a las entidades
    for Playeri in Players:
        Player.Bloques = Blocks
    
    for i in range(len(Constants.LaddersPosE)):
        Temporal = La.Ladder([(Constants.LaddersPosE[i]['x']),(Constants.LaddersPosE[i]['y'])],Constants.LaddersPosE[i]['width'],Constants.LaddersPosE[i]['height'])
        Ladders.add(Temporal)
    
    EnemysG = pygame.sprite.Group()
    for i in range(len(Constants.Enemys2E)):
        if Constants.Enemys2E[i]['name'] == 'BrujaE':
            Temp = Brujas.Escoba([(Constants.Enemys2E[i]['x']),(Constants.Enemys2E[i]['y'])-12],(Constants.Enemys2E[i]['properties'][0]['value']))
            EnemysG.add(Temp)
        elif Constants.Enemys2E[i]['name'] == 'BrujaC':
            Temp = Brujas.Estatica([(Constants.Enemys2E[i]['x']),(Constants.Enemys2E[i]['y'])-12])
            EnemysG.add(Temp)
    
    for Enemy in EnemysG:
        Enemy.Bloques = Blocks
    
    return [Players, Blocks, EnemysG, None, None, Ladders, None, WaterG, None, None, None, None, Constants.Clock, mapa, 5, '4', '6', '2', '5']
