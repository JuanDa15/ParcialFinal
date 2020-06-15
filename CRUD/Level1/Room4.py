#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Block
from Classes import Cannon as ca
from Classes import VerticalMovingPlatform as VMP
from Classes import Spikes

from pygame.locals import *

def StartRoom(Player, Players, positionX, positionY):
    mapa = Constants.mapa1D

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()
    Puas = pygame.sprite.Group()
    Platforms = pygame.sprite.Group()

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

    for i in range(len(Constants.CannonsPosD)):
        if Constants.CannonsPosD[i]['name'] == 'False':
            Temporal = Block.Bloque([(Constants.CannonsPosD[i]['x']),(Constants.CannonsPosD[i]['y'])],Constants.CannonsPosD[i]['width'],Constants.CannonsPosD[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosD[i]['x']),(Constants.CannonsPosD[i]['y'])],Constants.CannonIDLEL,1)
            Blocks.add(Temporal)
            Cannons.add(Temp)
        else:
            Temporal = Block.Bloque([(Constants.CannonsPosD[i]['x']),(Constants.CannonsPosD[i]['y'])],Constants.CannonsPosD[i]['width'],Constants.CannonsPosD[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosD[i]['x']),(Constants.CannonsPosD[i]['y'])],Constants.CannonIDLER,0)
            Blocks.add(Temporal)
            Cannons.add(Temp)
    
    #Creacion de Plataformas movibles
    Temporal = VMP.PlataformaMovil([(Constants.MovingPlatformED[0]['x']),(Constants.MovingPlatformED[0]['y'])],160,Constants.SmallPlatform,-1)
    Platforms.add(Temporal)
    Temporal = VMP.PlataformaMovil([(Constants.MovingPlatformSD[0]['x']),(Constants.MovingPlatformSD[0]['y'])],185,Constants.SmallPlatform,2)
    Platforms.add(Temporal)

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
        Player.PlataformasY = Platforms
    
    #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, instakill, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, None, Puas, Cannons, None, None, None, None, Platforms, None, None, Constants.Clock, mapa, 3, '3', '5','1','4']
