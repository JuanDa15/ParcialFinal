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

def StartRoom(Player, Players ,PositionX, PositionY):
    mapa = Constants.mapa1G

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()

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

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    return [Players, Blocks, None, Constants.Clock, mapa, None, None,5,'6','8','1','7']