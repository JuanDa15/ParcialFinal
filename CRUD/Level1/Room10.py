#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block
from Classes import Spikes

from pygame.locals import *

def StartRoom(Player, Players, PositionX, PositionY):

    mapa = Constants.mapa1J

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Puas = pygame.sprite.Group()

    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY
    
    #Creacion de los spikes
    for i in range(len(Constants.SpikesPosJ)):
        Temporal = Spikes.spikes([(Constants.SpikesPosJ[i]['x']),(Constants.SpikesPosJ[i]['y'])],Constants.SpikesPosJ[i]['width'],Constants.SpikesPosJ[i]['height'])
        Puas.add(Temporal)

    #Creacion de los bloques
    for i in range(len(Constants.CollisionsJ)):
        Temporal = Block.Bloque([(Constants.CollisionsJ[i]['x']),(Constants.CollisionsJ[i]['y'])],Constants.CollisionsJ[i]['width'],Constants.CollisionsJ[i]['height'])
        Blocks.add(Temporal)

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    return [Players ,Blocks ,None ,Constants.Clock ,mapa ,Puas ,None ,1 ,'9','1','10']