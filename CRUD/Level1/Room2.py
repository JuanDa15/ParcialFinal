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
from Classes import Spikes
from Classes import Coin as co
from Classes import Apple as ap
from Classes import Diamond as d
from Classes import Cannon as ca
from Classes import CannonBall as CB
from CRUD.Level1 import Room1
from CRUD.Level1 import Room3

from pygame.locals import *

def StartRoom(Player,Players,PositionX, PositionY):
    mapa = Constants.mapa1B
    Clock = pygame.time.Clock()

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cerdos = pygame.sprite.Group()
    Puas = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()

    #Creacion Enemigo
    C1 = pork.cerdo([257,370], 130)
    Cerdos.add(C1)

    #Creacion Cañon
    Ca = ca.cannon([Constants.CannonsPosB[0]['x'],Constants.CannonsPosB[0]['y']])
    Cannons.add(Ca)

    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion de las puas
    for i in range(len(Constants.SpikesPosB)):
        pincho = Spikes.spikes([(Constants.SpikesPosB[i]['x']),(Constants.SpikesPosB[i]['y'])],Constants.SpikesPosB[i]['width'],Constants.SpikesPosB[i]['height'])
        Puas.add(pincho)
    #Creacion de los bloques
    for i in range(len(Constants.CollisionsB)):
        Bloque = Block.Bloque([(Constants.CollisionsB[i]['x']),(Constants.CollisionsB[i]['y'])],Constants.CollisionsB[i]['width'],Constants.CollisionsB[i]['height'])
        Blocks.add(Bloque)
    #Creacion de las plataformas
    for i in range(len(Constants.PlatformsB)):
        Platform = Block.Bloque([(Constants.PlatformsB[i]['x']),(Constants.PlatformsB[i]['y'])],Constants.PlatformsB[i]['width'],Constants.PlatformsB[i]['height'])
        Blocks.add(Platform)
    for i in range(len(Constants.CannonsPosB)):
        cannon = Block.Bloque([(Constants.CannonsPosB[i]['x']),(Constants.CannonsPosB[i]['y'])],Constants.CannonsPosB[i]['width'],Constants.CannonsPosB[i]['height'])
        Blocks.add(cannon)
    
    #Asignacion de lista de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    for Cerdo in Cerdos:
        Cerdo.Bloques = Blocks

    return [Players,Blocks,Cerdos,Clock,mapa,Puas,Cannons,1,'1','3','2']

"""
Cannon Code


CannonBalls = pygame.sprite.Group()

for Cannon in Cannons:
    if Cannon.Disparo == 0:
        if Cannon.Direccion == True:
            B = CB.cannonball([Cannon.rect.x, Cannon.rect.y + 4], 5)
            B.Bloques = Blocks
            CannonBalls.add(B)
            Cannon.Disparo = 80
        else:
            B = CB.cannonball([Cannon.rect.x, Cannon.rect.y + 4], -5)
            B.Bloques = Blocks
            CannonBalls.add(B)
            Cannon.Disparo = 80
    else:
        Cannon.Disparo -= 1

for Bola in CannonBalls:
    listaColision=pygame.sprite.spritecollide(Bola,Blocks,False)
    for b in listaColision:
        if ((Bola.rect.right >= b.rect.left) and (Bola.rect.right <= b.rect.right)):
            CannonBalls.remove(Bola)
        elif ((Bola.rect.left <= b.rect.right) and (Bola.rect.left >= b.rect.left)):
            CannonBalls.remove(Bola)

listaColisionBolasCañon=pygame.sprite.spritecollide(Player,CannonBalls,False)
for b in listaColisionBolasCañon:
    if ((Player.rect.right >= b.rect.left) and (Player.rect.right <= b.rect.right)):
        print("Bolazo pai")
    elif ((Player.rect.left <= b.rect.right) and (Player.rect.left >= b.rect.left)):
        print("Bolazo pai")

    if ((Player.rect.bottom >= b.rect.top) and (Player.rect.bottom <= b.rect.bottom)):
        print("Bolazo pai")
    elif ((Player.rect.top <= b.rect.bottom) and (Player.rect.top >= b.rect.top)):
        print("Bolazo pai")

CannonBalls.update()


CannonBalls.draw(Constants.Screen)
"""