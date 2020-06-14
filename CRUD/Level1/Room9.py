#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Block
from pygame.locals import *

def StartRoom(Player ,Players ,PositionsX, PositionsY):
    mapa = Constants.mapa1I

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cerdos = pygame.sprite.Group()
    Puas = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionsX
        Player.rect.y = PositionsY
    
    #Creacion de las colisiones
    for i in range(len(Constants.CollisionsI)):
        Temporal = Block.Bloque([(Constants.CollisionsI[i]['x']),(Constants.CollisionsI[i]['y'])],Constants.CollisionsI[i]['width'],Constants.CollisionsI[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.PlatformsI)):
        Temporal = Block.Bloque([(Constants.PlatformsI[i]['x']),(Constants.PlatformsI[i]['y'])],Constants.PlatformsI[i]['width'],Constants.PlatformsI[i]['height'])
        Blocks.add(Temporal)

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    
    return [Players, Blocks, None, None, None, None, None, None, None, None, None, None, Constants.Clock, mapa, 7, '8', '10','1','9']
