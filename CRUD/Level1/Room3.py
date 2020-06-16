#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Block
from Classes import pork
from Classes import Bomber
from Classes import Cannon as ca
from Classes import VerticalMovingPlatform as VMP
from Classes import Spikes

from pygame.locals import *

def StartRoom(Player, Players, positionX, positionY):
    mapa = Constants.mapa1C
    
    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cerdos = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()
    Platforms = pygame.sprite.Group()
    Puas = pygame.sprite.Group()
    
    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = positionX
        Player.rect.y = positionY

    #Creacion Enemigos
    #Enemigos
    for i in range(len(Constants.Enemys1C)):
        if Constants.Enemys1C[i]['name'] == 'CerdoC':
            Temp = pork.cerdo([(Constants.Enemys1C[i]['x']),(Constants.Enemys1C[i]['y'])-12],(Constants.Enemys1C[i]['properties'][0]['value']))
            Cerdos.add(Temp)
        elif Constants.Enemys1C[i]['name'] == 'CerdoB':
            Temp = Bomber.Bomber([(Constants.Enemys1C[i]['x']),(Constants.Enemys1C[i]['y'])],Constants.Bomber,1)
            Cerdos.add(Temp)

    #Creacion de las puas
    for i in range(len(Constants.SpikesPosC)):
        Temporal = Spikes.spikes([(Constants.SpikesPosC[i]['x']),(Constants.SpikesPosC[i]['y'])],Constants.SpikesPosC[i]['width'],Constants.SpikesPosC[i]['height'])
        Puas.add(Temporal)

    #Creacion de las colisiones
    for i in range(len(Constants.CollisionsC)):
        Temporal = Block.Bloque([(Constants.CollisionsC[i]['x']),(Constants.CollisionsC[i]['y'])],Constants.CollisionsC[i]['width'],Constants.CollisionsC[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.PlatformsC)):
        Temporal = Block.Bloque([(Constants.PlatformsC[i]['x']),(Constants.PlatformsC[i]['y'])],Constants.PlatformsC[i]['width'],Constants.PlatformsC[i]['height'])
        Blocks.add(Temporal)
    
    for i in range(len(Constants.CannonsPosC)):
        if Constants.CannonsPosC[i]['name'] == 'False':
            Temporal = Block.Bloque([(Constants.CannonsPosC[i]['x']),(Constants.CannonsPosC[i]['y'])],Constants.CannonsPosC[i]['width'],Constants.CannonsPosC[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosC[i]['x']),(Constants.CannonsPosC[i]['y'])],Constants.CannonIDLEL,1)
            Blocks.add(Temporal)
            Cannons.add(Temp)
        else:
            Temporal = Block.Bloque([(Constants.CannonsPosC[i]['x']),(Constants.CannonsPosC[i]['y'])],Constants.CannonsPosC[i]['width'],Constants.CannonsPosC[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosC[i]['x']),(Constants.CannonsPosC[i]['y'])],Constants.CannonIDLER,0)
            Blocks.add(Temporal)
            Cannons.add(Temp)

    #Creacion de Plataformas movibles
    Temporal = VMP.PlataformaMovil([(Constants.MovingPlatformSC[0]['x']),(Constants.MovingPlatformSC[0]['y'])],190,Constants.SmallPlatform,1)
    Platforms.add(Temporal)
        
    #Asignacion de lista de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
        Player.PlataformasY = Platforms

    for Cerdo in Cerdos:
        Cerdo.Bloques = Blocks
    
    #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, instakill, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, Cerdos, Puas, Cannons, None, None, None, None, Platforms, None, None, Constants.Clock, mapa, 2,'2','4','1','3']