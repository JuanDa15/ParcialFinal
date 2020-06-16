#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Door as Do
from Classes import Block
from Classes import Cobra
from Classes import Brujas
from Classes import pork
from Classes import Bomber

from pygame.locals import *

def StartRoom(Player, Players ,PositionX ,PositionY):
    mapa = Constants.mapa1A

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Doors = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    """#Creacion Enemigos
    C1 = pork.cerdo([100,320], 130)
    Cerdos.add(C1)

    C2 = pork.cerdo([610,345], 100)
    #Pixeles antes de devolverse
    C2.Movidos = 0
    Cerdos.add(C2)"""

    #Creacion de las paredes
    for i in range(len(Constants.CollisionsA)):
        Temporal = Block.Bloque([(Constants.CollisionsA[i]['x']),(Constants.CollisionsA[i]['y'])],Constants.CollisionsA[i]['width'],Constants.CollisionsA[i]['height'])
        Blocks.add(Temporal)
    #Creacion de las plataformas
    for i in range(len(Constants.PlatformsA)):
        Temporal = Block.Bloque([(Constants.PlatformsA[i]['x']),(Constants.PlatformsA[i]['y'])],Constants.PlatformsA[i]['width'],Constants.PlatformsA[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.DoorA)):
        Temporal = Do.Door([(Constants.DoorA[i]['x']),(Constants.DoorA[i]['y'])],Constants.DoorA[i]['width'],Constants.DoorA[i]['height'],'0')
        Doors.add(Temporal)
    
    #Enemigos
    EnemysG = pygame.sprite.Group()
    for i in range(len(Constants.Enemys1A)):
        if Constants.Enemys1A[i]['name'] == 'CerdoC':
            Temp = pork.cerdo([(Constants.Enemys1A[i]['x']),(Constants.Enemys1A[i]['y'])-12],(Constants.Enemys1A[i]['properties'][0]['value']))
            EnemysG.add(Temp)
        elif Constants.Enemys1A[i]['name'] == 'CerdoB':
            Temp = Bomber.Bomber([(Constants.Enemys1A[i]['x']),(Constants.Enemys1A[i]['y'])],Constants.Bomber,1)
            EnemysG.add(Temp)

    #Asignacion de lista de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    
    for e in EnemysG:
        e.Bloques = Blocks
        
    #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, instakill Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, EnemysG, None, None, None, None, None, Doors, None, None, None, Constants.Clock, mapa, 0, None,'2','1','1']