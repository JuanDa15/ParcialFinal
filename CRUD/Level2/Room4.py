#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block
from Classes import Brujas
from Classes import Ladder as La
from Classes import Lava

from pygame.locals import *

def StartRoom(Player, Players, PositionX, PositionY):

    mapa = Constants.mapa2D

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Ladders = pygame.sprite.Group()
    LavaG = pygame.sprite.Group()

    #Definicion Posicion inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion Lava
    for i in range(len(Constants.LavaPosD)):
        Temporal = Lava.Lava([(Constants.LavaPosD[i]['x']),(Constants.LavaPosD[i]['y'])], Constants.LavaPosD[i]['width'],Constants.LavaPosD[i]['height'])
        LavaG.add(Temporal)

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
    
    EnemysG = pygame.sprite.Group()
    for i in range(len(Constants.Enemys2D)):
        if Constants.Enemys2D[i]['name'] == 'BrujaE':
            Temp = Brujas.Escoba([(Constants.Enemys2D[i]['x']),(Constants.Enemys2D[i]['y'])-12],(Constants.Enemys2D[i]['properties'][0]['value']))
            EnemysG.add(Temp)
        elif Constants.Enemys2D[i]['name'] == 'BrujaC':
            Temp = Brujas.Estatica([(Constants.Enemys2D[i]['x']),(Constants.Enemys2D[i]['y'])-12])
            EnemysG.add(Temp)
    
    for Enemy in EnemysG:
        Enemy.Bloques = Blocks
    
    return [Players, Blocks, EnemysG, None, None, Ladders, LavaG, None, None, None, None, None, Constants.Clock, mapa, 1, '3', '5', '2', '4']
