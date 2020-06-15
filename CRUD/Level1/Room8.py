#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block
from Classes import Cannon as ca
from Classes import VerticalMovingPlatform as VMP
from pygame.locals import *

def StartRoom(Player ,Players ,PositionX, PositionY):

    mapa = Constants.mapa1H

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()
    PlatformsY = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de las colisiones
    for i in range(len(Constants.CollisionsH)):
        Temporal = Block.Bloque([(Constants.CollisionsH[i]['x']),(Constants.CollisionsH[i]['y'])],Constants.CollisionsH[i]['width'],Constants.CollisionsH[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.PlatformsH)):
        Temporal = Block.Bloque([(Constants.PlatformsH[i]['x']),(Constants.PlatformsH[i]['y'])],Constants.PlatformsH[i]['width'],Constants.PlatformsH[i]['height'])
        Blocks.add(Temporal)

    #Creacion de los cañones
    for i in range(len(Constants.CannonsPosH)):
        if Constants.CannonsPosH[i]['name'] == 'False':
            Temporal = Block.Bloque([(Constants.CannonsPosH[i]['x']),(Constants.CannonsPosH[i]['y'])],Constants.CannonsPosH[i]['width'],Constants.CannonsPosH[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosH[i]['x']),(Constants.CannonsPosH[i]['y'])],Constants.CannonIDLEL,1)
            Blocks.add(Temporal)
            Cannons.add(Temp)
        else:
            Temporal = Block.Bloque([(Constants.CannonsPosH[i]['x']),(Constants.CannonsPosH[i]['y'])],Constants.CannonsPosH[i]['width'],Constants.CannonsPosH[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosH[i]['x']),(Constants.CannonsPosH[i]['y'])],Constants.CannonIDLER,0)
            Blocks.add(Temporal)
            Cannons.add(Temp)

    Distance = (Constants.VMovingPlatformSSR[0]['y'] - Constants.VMovingPlatformESR[0]['y']) - 2
    Temporal = VMP.PlataformaMovil([(Constants.VMovingPlatformSSR[0]['x']),((Constants.VMovingPlatformSSR[0]['y']) - 15)],Distance,Constants.LongPlatform,-1)
    PlatformsY.add(Temporal)

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
        Player.PlataformasY = PlatformsY
    #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, instakill, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players,Blocks,None, None, Cannons, None, None, None, 'Una puerta', PlatformsY, None, None, Constants.Clock, mapa, 6,'7', '9','1','8']