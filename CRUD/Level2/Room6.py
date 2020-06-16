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

def StartRoom(Player ,Players ,PositionX , PositionY):
    mapa = Constants.mapa2F

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Ladders = pygame.sprite.Group()
    LavaG = pygame.sprite.Group()

    #Definicion Posicion inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de los bloques
    for i in range(len(Constants.WallsF)):
        Temporal = Block.Bloque([(Constants.WallsF[i]['x']),(Constants.WallsF[i]['y'])],Constants.WallsF[i]['width'],Constants.WallsF[i]['height'])
        Blocks.add(Temporal)
    
    #Creacion Lava
    for i in range(len(Constants.LavaPosF)):
        Temporal = Lava.Lava([(Constants.LavaPosF[i]['x']),(Constants.LavaPosF[i]['y'])], Constants.LavaPosF[i]['width'],Constants.LavaPosF[i]['height'])
        LavaG.add(Temporal)

    for i in range(len(Constants.LaddersPosF)):
        Temporal = La.Ladder([(Constants.LaddersPosF[i]['x']),(Constants.LaddersPosF[i]['y'])],Constants.LaddersPosF[i]['width'],Constants.LaddersPosF[i]['height'])
        Ladders.add(Temporal)

    #Asignacion colisiones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    
    EnemysG = pygame.sprite.Group()
    for i in range(len(Constants.Enemys2F)):
        if Constants.Enemys2F[i]['name'] == 'BrujaE':
            Temp = Brujas.Escoba([(Constants.Enemys2F[i]['x']),(Constants.Enemys2F[i]['y'])-12],(Constants.Enemys2F[i]['properties'][0]['value']))
            EnemysG.add(Temp)
        elif Constants.Enemys2F[i]['name'] == 'BrujaC':
            Temp = Brujas.Estatica([(Constants.Enemys2F[i]['x']),(Constants.Enemys2F[i]['y'])-12])
            EnemysG.add(Temp)
    
    for Enemy in EnemysG:
        Enemy.Bloques = Blocks
    

    return [Players, Blocks, EnemysG, None, None, Ladders, LavaG, None, None, None, None, None, Constants.Clock, mapa, 7, '5', '7', '2', '6']
