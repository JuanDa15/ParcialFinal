#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Block
from Classes import Cannon as ca
from Classes import Spikes

from pygame.locals import *

def StartRoom(Player ,Players, positionX, positionY):
    mapa = Constants.mapa1E

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()
    Puas = pygame.sprite.Group()
    
    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = positionX
        Player.rect.y = positionY

    #Creacion de los spikes
    for i in range(len(Constants.SpikesPosE)):
        Temporal = Spikes.spikes([(Constants.SpikesPosE[i]['x']),(Constants.SpikesPosE[i]['y'])],Constants.SpikesPosE[i]['width'],Constants.SpikesPosE[i]['height'])
        Puas.add(Temporal)

    #Creacion de las colisiones
    for i in range(len(Constants.CollisionsE)):
        Temporal = Block.Bloque([(Constants.CollisionsE[i]['x']),(Constants.CollisionsE[i]['y'])],Constants.CollisionsE[i]['width'],Constants.CollisionsE[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.PlatformsE)):
        Temporal = Block.Bloque([(Constants.PlatformsE[i]['x']),(Constants.PlatformsE[i]['y'])],Constants.PlatformsE[i]['width'],Constants.PlatformsE[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.CannonsPosE)):
        Temporal = Block.Bloque([(Constants.CannonsPosE[i]['x']),(Constants.CannonsPosE[i]['y'])],Constants.CannonsPosE[i]['width'],Constants.CannonsPosE[i]['height'])
        Temp = ca.cannon([(Constants.CannonsPosE[i]['x']),(Constants.CannonsPosE[i]['y'])])
        Blocks.add(Temporal)
        Cannons.add(Temp)
    
    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    return [Players ,Blocks ,None ,Constants.Clock ,mapa ,Puas ,Cannons ,4 ,'4' ,'6' ,'1','5']
