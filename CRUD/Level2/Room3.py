#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Spikes
from Classes import Block

from pygame.locals import *

def StartRoom(Player ,Players ,PositionX , PositionY):
    mapa = Constants.mapa2C

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Puas = pygame.sprite.Group()

    #Definicion posicion inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    
    #Creacion de los spikes
    for i in range(len(Constants.SpikesPos2C)):
        Temporal = Spikes.spikes([(Constants.SpikesPos2C[i]['x']),(Constants.SpikesPos2C[i]['y'])],Constants.SpikesPos2C[i]['width'],Constants.SpikesPos2C[i]['height'])
        Puas.add(Temporal)

    #Creacion de las colisiones
    for i in range(len(Constants.WallsC)):
        Temporal = Block.Bloque([(Constants.WallsC[i]['x']),(Constants.WallsC[i]['y'])],Constants.WallsC[i]['width'],Constants.WallsC[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.Platforms2C)):
        Temporal = Block.Bloque([(Constants.Platforms2C[i]['x']),(Constants.Platforms2C[i]['y'])],Constants.Platforms2C[i]['width'],Constants.Platforms2C[i]['height'])
        Blocks.add(Temporal)

    #Definicion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    return [Players, Blocks, None, Puas, None, None, None, None, None, None, None, None, Constants.Clock, mapa, 4, '2', '4', '2', '3']