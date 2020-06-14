#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Block
from Classes import pork
from Classes import Cannon as ca
from Classes import Spikes

from pygame.locals import *

def StartRoom(Player, Players ,PositionX ,PositionY):
    mapa = Constants.MapaTutorial

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    cannons = pygame.sprite.Group()
    Puas = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de spykes
    for i in range(len(Constants.SpikesPosTutos)):
        Temporal = Spikes.spikes([(Constants.SpikesPosTutos[i]['x']),(Constants.SpikesPosTutos[i]['y'])],Constants.SpikesPosTutos[i]['width'],Constants.SpikesPosTutos[i]['height'])
        Puas.add(Temporal)

    #Creacion de las paredes
    for i in range(len(Constants.WallsTutorial)):
        Temporal = Block.Bloque([(Constants.WallsTutorial[i]['x']),(Constants.WallsTutorial[i]['y'])],Constants.WallsTutorial[i]['width'],Constants.WallsTutorial[i]['height'])
        Blocks.add(Temporal)

    #Creacion de cañones
    for i in range(len(Constants.CannonsPosTuto)):
        Temporal = Block.Bloque([(Constants.CannonsPosTuto[i]['x']),(Constants.CannonsPosTuto[i]['y'])],Constants.CannonsPosTuto[i]['width'],Constants.CannonsPosTuto[i]['height'])
        Temp = ca.cannon([(Constants.CannonsPosTuto[i]['x']),(Constants.CannonsPosTuto[i]['y'])])
        Blocks.add(Temporal)
        cannons.add(Temp)
    #Asignacion de lista de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
    
        #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, None, Puas, cannons, None, None, None, 'Una puerta', None, None, None, Constants.Clock, mapa, 0, None,None,'0','1']