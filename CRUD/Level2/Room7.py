#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block

from pygame.locals import *

def StartRoom(Player ,Players ,PositionX , PositionY):

    mapa = Constants.mapa2G

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY


    #Creacion de los bloques
    for i in range(len(Constants.WallsG)):
        Bloque = Block.Bloque([(Constants.WallsG[i]['x']),(Constants.WallsG[i]['y'])],Constants.WallsG[i]['width'],Constants.WallsG[i]['height'])
        Blocks.add(Bloque)
    

    #Asignacion de colisiones a las entidades
    for Playeri in Players:
        Player.Bloques = Blocks
    
    
    return [Players, Blocks, None, None, None, None, None, None, None, None, None,None, Constants.Clock, mapa, 1, '6', '8', '2', 7]

        