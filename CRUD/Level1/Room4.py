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

def StartRoom(Player, Players, positionX, positionY):
    mapa = Constants.mapa1D

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()
    Puas = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = positionX
        Player.rect.y = positionY

    #Creacion de los spikes
    for i in range(len(Constants.SpikesPosD)):
        Temporal = Spikes.spikes([(Constants.SpikesPosD[i]['x']),(Constants.SpikesPosD[i]['y'])],Constants.SpikesPosD[i]['width'],Constants.SpikesPosD[i]['height'])
        Puas.add(Temporal)
    #Creacion de las colisiones
    for i in range(len(Constants.CollisionsD)):
        Temporal = Block.Bloque([(Constants.CollisionsD[i]['x']),(Constants.CollisionsD[i]['y'])],Constants.CollisionsD[i]['width'],Constants.CollisionsD[i]['height'])
        Blocks.add(Temporal)
        
    for i in range(len(Constants.PlatformsD)):
        Temporal = Block.Bloque([(Constants.PlatformsD[i]['x']),(Constants.PlatformsD[i]['y'])],Constants.PlatformsD[i]['width'],Constants.PlatformsD[i]['height'])
        Blocks.add(Temporal)

    for i in range (len(Constants.CannonsPosD)):
        Temporal = Block.Bloque([(Constants.CannonsPosD[i]['x']),(Constants.CannonsPosD[i]['y'])],Constants.CannonsPosD[i]['width'],Constants.CannonsPosD[i]['height'])
        Temp = ca.cannon([(Constants.CannonsPosD[i]['x']),(Constants.CannonsPosD[i]['y'])])
        Blocks.add(Temporal)
        Cannons.add(Temp)

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    
    return [Players, Blocks, None, Puas, Cannons, None, None, None, None, None, None, None, Constants.Clock, mapa, 3, '3', '5','1','4']
