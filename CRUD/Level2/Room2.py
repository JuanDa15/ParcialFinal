#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Door as Do
from Classes import Player as P
from Classes import Block
from Classes import VerticalMovingPlatform as VMP
from pygame.locals import *

def StartRoom(Player ,Players ,PositionX , PositionY):
    mapa = Constants.mapa2B

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Platforms = pygame.sprite.Group()
    
    #Definicion posicion inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY
    
    #Creacion de las coliciones
    for i in range(len(Constants.WallsB)):
        Temporal = Block.Bloque([(Constants.WallsB[i]['x']),(Constants.WallsB[i]['y'])],Constants.WallsB[i]['width'],Constants.WallsB[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.Platforms2B)):
        Temporal = Block.Bloque([(Constants.Platforms2B[i]['x']),(Constants.Platforms2B[i]['y'])],Constants.Platforms2B[i]['width'],Constants.Platforms2B[i]['height'])
        Blocks.add(Temporal)
    #Creacion de Plataforma movible
    Temporal = VMP.PlataformaMovil([(Constants.VMovingPlatformS2B[0]['x']),(Constants.VMovingPlatformS2B[0]['y'])],317,Constants.SmallPlatform,1)
    Platforms.add(Temporal)
    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
        Player.PlataformasY = Platforms
    #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, instakill, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, None, None, None, None, None, None, None, Platforms, None, None, Constants.Clock, mapa, 3, '1', '3', '2', '2']
