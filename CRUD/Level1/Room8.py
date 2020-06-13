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
from pygame.locals import *

def StartRoom(Player ,Players ,PositionX, PositionY):

    mapa = Constants.mapa1H

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()

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
        Temporal = Block.Bloque([(Constants.CannonsPosH[i]['x']),(Constants.CannonsPosH[i]['y'] - 15)],(Constants.CannonsPosH[i]['width']),(Constants.CannonsPosH[i]['height']))
        Temp = ca.cannon([(Constants.CannonsPosH[i]['x']),(Constants.CannonsPosH[i]['y'])])
        Blocks.add(Temporal)
        Cannons.add(Temp)

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

<<<<<<< HEAD
    return [Players,Blocks,None,Constants.Clock, mapa, None, Cannons, 6,'7', '9','1','8']
=======
    return [Players,Blocks,None, None, Cannons, None, None, None, 'Una puerta', None, None, None, Constants.Clock, mapa, 6,'7', '9','1','8']
>>>>>>> Potter
