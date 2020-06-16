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
from Classes import Spikes

from pygame.locals import *

def StartRoom(Player, Players, positionX, positionY):

    mapa = Constants.mapa1F

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Puas = pygame.sprite.Group()
    EnemysG = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = positionX
        Player.rect.y = positionY
    
    #Creacion de los spikes
    for i in range(len(Constants.SpikesPosF)):
        Temporal = Spikes.spikes([(Constants.SpikesPosF[i]['x']),(Constants.SpikesPosF[i]['y'])],Constants.SpikesPosF[i]['width'],Constants.SpikesPosF[i]['height'])
        Puas.add(Temporal)

    #Creacion de las colisiones
    for i in range(len(Constants.CollisionsF)):
        Temporal = Block.Bloque([(Constants.CollisionsF[i]['x']),(Constants.CollisionsF[i]['y'])],Constants.CollisionsF[i]['width'],Constants.CollisionsF[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.PlatformsF)):
        Temporal = Block.Bloque([(Constants.PlatformsF[i]['x']),(Constants.PlatformsF[i]['y'])],Constants.PlatformsF[i]['width'],Constants.PlatformsF[i]['height'])
        Blocks.add(Temporal)

    for i in range(len(Constants.Enemys1F)):
        if Constants.Enemys1F[i]['name'] == 'CerdoC':
            Temp = pork.cerdo([(Constants.Enemys1F[i]['x']),(Constants.Enemys1F[i]['y'])-12],(Constants.Enemys1F[i]['properties'][0]['value']))
            EnemysG.add(Temp)
        elif Constants.Enemys1F[i]['name'] == 'CerdoB':
            Temp = Bomber.Bomber([(Constants.Enemys1F[i]['x']),(Constants.Enemys1F[i]['y'])],Constants.Bomber,1)
            EnemysG.add(Temp)

    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    for Enemy in EnemysG:
        Enemy.Bloques = Blocks
        
    return [Players,Blocks,EnemysG,Puas,None, None, None, None, None, None, None, None, Constants.Clock, mapa,1,'5','7','1','6']