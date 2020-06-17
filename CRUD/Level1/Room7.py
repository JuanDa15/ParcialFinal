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
from Classes import pork
from Classes import Bomber
from Classes import Cannon as ca
from Classes import VerticalMovingPlatform as VMP

from pygame.locals import *

def StartRoom(Player, Players ,PositionX, PositionY):
    mapa = Constants.mapa1G

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    PlatformsY = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY
    

    #Creacion de las coliciones
    for i in range(len(Constants.CollisionsG)):
        Temporal = Block.Bloque([(Constants.CollisionsG[i]['x']),(Constants.CollisionsG[i]['y'])],Constants.CollisionsG[i]['width'],Constants.CollisionsG[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.PlatformsG)):
        Temporal = Block.Bloque([(Constants.PlatformsG[i]['x']),(Constants.PlatformsG[i]['y'])],Constants.PlatformsG[i]['width'],Constants.PlatformsG[i]['height'])
        Blocks.add(Temporal)

    #Creacion de Plataformas movibles
    Temporal = VMP.PlataformaMovil([(Constants.VMovingPlatformSG[0]['x']),(Constants.VMovingPlatformSG[0]['y'])],160,Constants.SmallPlatform, -2)
    PlatformsY.add(Temporal)

    EnemysG = pygame.sprite.Group()
    for i in range(len(Constants.Enemys1G)):
        if Constants.Enemys1G[i]['name'] == 'CerdoC':
            Temp = pork.cerdo([(Constants.Enemys1G[i]['x']),(Constants.Enemys1G[i]['y'])-12],(Constants.Enemys1G[i]['properties'][0]['value']))
            EnemysG.add(Temp)
        elif Constants.Enemys1G[i]['name'] == 'CerdoB':
            Temp = Bomber.Bomber([(Constants.Enemys1G[i]['x']),(Constants.Enemys1G[i]['y'])],Constants.Bomber,1)
            EnemysG.add(Temp)
    
    Instakill = pygame.sprite.Group()
    for i in range(len(Constants.InstakillPosG)):
        Temporal = Block.Bloque([(Constants.InstakillPosG[i]['x']),(Constants.InstakillPosG[i]['y'])],Constants.InstakillPosG[i]['width'],Constants.InstakillPosG[i]['height'])
        Instakill.add(Temporal)

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
        Player.PlataformasY = PlatformsY
    
    for Enemy in EnemysG:
        Enemy.Bloques = Blocks
     #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, instakill, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, EnemysG, None, None, None, None, None, None, PlatformsY, None, Instakill, Constants.Clock, mapa, 5,'6','8','1','7']