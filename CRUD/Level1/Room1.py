#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block
from Classes import pork
from CRUD.Level1 import Room2

from pygame.locals import *

def StartRoom(Player, Players, PositionX, PositionY):
    Clock = pygame.time.Clock()
    mapa = Constants.mapa1A

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cerdos = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.right = PositionX
        Player.rect.y = PositionY

    #Creacion Enemigos
    C1 = pork.cerdo([100,320], 130)
    Cerdos.add(C1)

    C2 = pork.cerdo([610,345], 100)
    #Pixeles antes de devolverse
    C2.Movidos = 0
    Cerdos.add(C2)
    
    #Creacion de las paredes
    for i in range(len(Constants.CollisionsA)):
        Bloque = Block.Bloque([(Constants.CollisionsA[i]['x']),(Constants.CollisionsA[i]['y'])],Constants.CollisionsA[i]['width'],Constants.CollisionsA[i]['height'])
        Blocks.add(Bloque)
    #Creacion de las plataformas
    for i in range(len(Constants.PlatformsA)):
        Platform = Block.Bloque([(Constants.PlatformsA[i]['x']),(Constants.PlatformsA[i]['y'])],Constants.PlatformsA[i]['width'],Constants.PlatformsA[i]['height'])
        Blocks.add(Platform)

    #Asignacion de lista de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    for Cerdo in Cerdos:
        Cerdo.Bloques = Blocks

    return [Players,Blocks,Cerdos,Clock,mapa,None,None,0,None,'2','1']