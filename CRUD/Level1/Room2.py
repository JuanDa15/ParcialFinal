#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Block
from Classes import Bomber
from Classes import pork
from Classes import Spikes
from Classes import Cannon as ca

from pygame.locals import *

def StartRoom(Player ,Players ,PositionX, PositionY):
    mapa = Constants.mapa1B

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cerdos = pygame.sprite.Group()
    Puas = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()
    
    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Enemigos
    for i in range(len(Constants.Enemys1B)):
        if Constants.Enemys1B[i]['name'] == 'CerdoC':
            Temp = pork.cerdo([(Constants.Enemys1B[i]['x']),(Constants.Enemys1B[i]['y'])-12],(Constants.Enemys1B[i]['properties'][0]['value'])-20)
            Cerdos.add(Temp)
        elif Constants.Enemys1B[i]['name'] == 'CerdoB':
            Temp = Bomber.Bomber([(Constants.Enemys1B[i]['x']),(Constants.Enemys1B[i]['y'])],Constants.Bomber,1)
            Cerdos.add(Temp)
    
    #Creacion de las puas
    for i in range(len(Constants.SpikesPosB)):
        Temporal = Spikes.spikes([(Constants.SpikesPosB[i]['x']),(Constants.SpikesPosB[i]['y'])],Constants.SpikesPosB[i]['width'],Constants.SpikesPosB[i]['height'])
        Puas.add(Temporal)
    #Creacion de los bloques
    for i in range(len(Constants.CollisionsB)):
        Temporal = Block.Bloque([(Constants.CollisionsB[i]['x']),(Constants.CollisionsB[i]['y'])],Constants.CollisionsB[i]['width'],Constants.CollisionsB[i]['height'])
        Blocks.add(Temporal)
    #Creacion de las plataformas
    for i in range(len(Constants.PlatformsB)):
        Temporal = Block.Bloque([(Constants.PlatformsB[i]['x']),(Constants.PlatformsB[i]['y'])],Constants.PlatformsB[i]['width'],Constants.PlatformsB[i]['height'])
        Blocks.add(Temporal)
        
    for i in range(len(Constants.CannonsPosB)):
        if Constants.CannonsPosB[i]['name'] == 'False':
            Temporal = Block.Bloque([(Constants.CannonsPosB[i]['x']),(Constants.CannonsPosB[i]['y'])],Constants.CannonsPosB[i]['width'],Constants.CannonsPosB[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosB[i]['x']),(Constants.CannonsPosB[i]['y'])],Constants.CannonIDLEL,1)
            Blocks.add(Temporal)
            Cannons.add(Temp)
        else:
            Temporal = Block.Bloque([(Constants.CannonsPosB[i]['x']),(Constants.CannonsPosB[i]['y'])],Constants.CannonsPosB[i]['width'],Constants.CannonsPosB[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosB[i]['x']),(Constants.CannonsPosB[i]['y'])],Constants.CannonIDLER,0)
            Blocks.add(Temporal)
            Cannons.add(Temp)
    
    #Asignacion de lista de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    for Cerdo in Cerdos:
        Cerdo.Bloques = Blocks

    #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, Cerdos, Puas, Cannons, None, None, None, None, None, None, None, Constants.Clock, mapa, 1,'1','3','1','2']