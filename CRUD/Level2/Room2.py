#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Door as Do
from Classes import Water
from Classes import Player as P
from Classes import Block
from Classes import VerticalMovingPlatform as VMP
from pygame.locals import *
from Classes import Ladder as La

def StartRoom(Player ,Players ,PositionX , PositionY):
    mapa = Constants.mapa2B

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Platforms = pygame.sprite.Group()
    Ladders = pygame.sprite.Group()
    WaterG = pygame.sprite.Group()
    
    #Definicion posicion inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY
    
    #Creacion Agua
    for i in range(len(Constants.WaterPosB)):
        Temporal = Water.Water([(Constants.WaterPosB[i]['x']),(Constants.WaterPosB[i]['y'])], Constants.WaterPosB[i]['width'],Constants.WaterPosB[i]['height'])
        WaterG.add(Temporal)
    
    for i in range(len(Constants.DeepWaterPosB)):
        Temporal = Water.Water([(Constants.DeepWaterPosB[i]['x']),(Constants.DeepWaterPosB[i]['y'])], Constants.DeepWaterPosB[i]['width'],Constants.DeepWaterPosB[i]['height'])
        WaterG.add(Temporal)

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
    
    for i in range(len(Constants.LaddersPosB)):
        Temporal = La.Ladder([(Constants.LaddersPosB[i]['x']),(Constants.LaddersPosB[i]['y'])],Constants.LaddersPosB[i]['width'],Constants.LaddersPosB[i]['height'])
        Ladders.add(Temporal)

    #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, instakill, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, None, None, None, Ladders, None, WaterG, None, Platforms, None, None, Constants.Clock, mapa, 3, '1', '3', '2', '2']
