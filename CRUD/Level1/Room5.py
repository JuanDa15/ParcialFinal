#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Block
from Classes import Cannon as ca
from Classes import pork
from Classes import Bomber
from Classes import Spikes
from Classes import VerticalMovingPlatform as VMP
from Classes import HorizontalMovingPlatform as HMP

from pygame.locals import *

def StartRoom(Player ,Players, positionX, positionY):
    mapa = Constants.mapa1E

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()
    PlatformsX = pygame.sprite.Group()
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
        if Constants.CannonsPosE[i]['name'] == 'False':
            Temporal = Block.Bloque([(Constants.CannonsPosE[i]['x']),(Constants.CannonsPosE[i]['y'])],Constants.CannonsPosE[i]['width'],Constants.CannonsPosE[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosE[i]['x']),(Constants.CannonsPosE[i]['y'])],Constants.CannonIDLEL,1)
            Blocks.add(Temporal)
            Cannons.add(Temp)
        else:
            Temporal = Block.Bloque([(Constants.CannonsPosE[i]['x']),(Constants.CannonsPosE[i]['y'])],Constants.CannonsPosE[i]['width'],Constants.CannonsPosE[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosE[i]['x']),(Constants.CannonsPosE[i]['y'])],Constants.CannonIDLER,0)
            Blocks.add(Temporal)
            Cannons.add(Temp)

    #Creacion de Plataformas movibles
    Distance = Constants.HMovingPlatformEE[0]['x'] - Constants.HMovingPlatformSE[0]['x']
    Temporal = HMP.PlataformaMovil([(Constants.HMovingPlatformSE[0]['x']),(Constants.HMovingPlatformSE[0]['y'])],Distance,Constants.SmallPlatform)
    PlatformsX.add(Temporal)

    EnemysG = pygame.sprite.Group()
    for i in range(len(Constants.Enemys1E)):
        if Constants.Enemys1E[i]['name'] == 'CerdoC':
            Temp = pork.cerdo([(Constants.Enemys1E[i]['x']),(Constants.Enemys1E[i]['y'])-12],(Constants.Enemys1E[i]['properties'][0]['value']))
            EnemysG.add(Temp)
        elif Constants.Enemys1E[i]['name'] == 'CerdoB':
            Temp = Bomber.Bomber([(Constants.Enemys1E[i]['x']),(Constants.Enemys1E[i]['y'])],Constants.Bomber,1)
            EnemysG.add(Temp)

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
        Player.PlataformasX = PlatformsX
     #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, instakill, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players ,Blocks ,EnemysG , Puas, Cannons, None, None, None, None, PlatformsX, None, None, Constants.Clock, mapa ,4 ,'4' ,'6' ,'1','5']
