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
from Classes import Ladder as La
from Classes import Lava

from pygame.locals import *

def StartRoom(Player ,Players ,PositionX , PositionY):

    mapa = Constants.mapa2G

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Doors = pygame.sprite.Group()
    Ladders = pygame.sprite.Group()
    LavaG = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY


    #Creacion de los bloques
    for i in range(len(Constants.WallsG)):
        Bloque = Block.Bloque([(Constants.WallsG[i]['x']),(Constants.WallsG[i]['y'])],Constants.WallsG[i]['width'],Constants.WallsG[i]['height'])
        Blocks.add(Bloque)
    
    #Creacion Lava
    for i in range(len(Constants.LavaPosG)):
        Temporal = Lava.Lava([(Constants.LavaPosG[i]['x']),(Constants.LavaPosG[i]['y'])], Constants.LavaPosG[i]['width'],Constants.LavaPosG[i]['height'])
        LavaG.add(Temporal)

    for i in range(len(Constants.DoorPos2G)):
        Temporal = Do.Door([(Constants.DoorPos2G[i]['x']),(Constants.DoorPos2G[i]['y'])],Constants.DoorPos2G[i]['width'],Constants.DoorPos2G[i]['height'],'28')
    Doors.add(Temporal)

    #Asignacion de colisiones a las entidades
    for Playeri in Players:
        Player.Bloques = Blocks
    
    EnemysG = pygame.sprite.Group()
    for i in range(len(Constants.Enemys2G)):
        if Constants.Enemys2G[i]['name'] == 'BrujaE':
            Temp = Brujas.Escoba([(Constants.Enemys2G[i]['x']),(Constants.Enemys2G[i]['y'])-12],(Constants.Enemys2G[i]['properties'][0]['value']))
            EnemysG.add(Temp)
        elif Constants.Enemys2G[i]['name'] == 'BrujaC':
            Temp = Brujas.Estatica([(Constants.Enemys2G[i]['x']),(Constants.Enemys2G[i]['y'])-12])
            EnemysG.add(Temp)
    
    for Enemy in EnemysG:
        Enemy.Bloques = Blocks
    
    return [Players, Blocks, EnemysG, None, None, None, LavaG, None, Doors, None, None,None, Constants.Clock, mapa, 1, '6', '8', '2', '7']

        