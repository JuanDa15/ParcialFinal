#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Spikes
from Classes import Block
from Classes import Lava
from Classes import Brujas
from pygame.locals import *

def StartRoom(Player ,Players ,PositionX , PositionY):
    mapa = Constants.mapa2C

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    LavaG = pygame.sprite.Group()
    Puas = pygame.sprite.Group()

    #Definicion posicion inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion Lava
    for i in range(len(Constants.LavaPosC)):
        Temporal = Lava.Lava([(Constants.LavaPosC[i]['x']),(Constants.LavaPosC[i]['y'])], Constants.LavaPosC[i]['width'],Constants.LavaPosC[i]['height'])
        LavaG.add(Temporal)

    #Creacion de los spikes
    for i in range(len(Constants.SpikesPos2C)):
        Temporal = Spikes.spikes([(Constants.SpikesPos2C[i]['x']),(Constants.SpikesPos2C[i]['y'])],Constants.SpikesPos2C[i]['width'],Constants.SpikesPos2C[i]['height'])
        Puas.add(Temporal)

    #Creacion de las colisiones
    for i in range(len(Constants.WallsC)):
        Temporal = Block.Bloque([(Constants.WallsC[i]['x']),(Constants.WallsC[i]['y'])],Constants.WallsC[i]['width'],Constants.WallsC[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.Platforms2C)):
        Temporal = Block.Bloque([(Constants.Platforms2C[i]['x']),(Constants.Platforms2C[i]['y'])],Constants.Platforms2C[i]['width'],Constants.Platforms2C[i]['height'])
        Blocks.add(Temporal)
    
    EnemysG = pygame.sprite.Group()
    for i in range(len(Constants.Enemys2C)):
        if Constants.Enemys2C[i]['name'] == 'BrujaE':
            Temp = Brujas.Escoba([(Constants.Enemys2C[i]['x']),(Constants.Enemys2C[i]['y'])-12],(Constants.Enemys2C[i]['properties'][0]['value']))
            EnemysG.add(Temp)
        elif Constants.Enemys2C[i]['name'] == 'BrujaC':
            Temp = Brujas.Estatica([(Constants.Enemys2C[i]['x']),(Constants.Enemys2C[i]['y'])-12])
            EnemysG.add(Temp)
    
    for Enemy in EnemysG:
        Enemy.Bloques = Blocks

    #Definicion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, instakill, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, EnemysG, Puas, None, None, LavaG, None, None, None, None, None, Constants.Clock, mapa, 4, '2', '4', '2', '3']
