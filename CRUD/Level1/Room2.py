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

#Map Information
#Lectura de archivo json
FileName= 'Assets\Levels\Level1\Level1b.json'
MapInfo = None
with open(FileName) as Information:
    MapInfo=json.load(Information)
Information.close()
#Extraccion Objetos Json
Collisions = MapInfo['layers'][10]['objects']
Platforms = MapInfo['layers'][11]['objects']
CoinsPos = MapInfo['layers'][12]['objects']
ApplesPos = MapInfo['layers'][13]['objects']
DiamondsPos = MapInfo['layers'][14]['objects']
CannonsPos= MapInfo['layers'][15]['objects']
SpikesPos= MapInfo['layers'][16]['objects']

def StartRoom2(Player,PositionX, PositionY):
    mapa = Constants.mapa1B
    Clock = pygame.time.Clock()

    #Definicion de Grupos
    Players = pygame.sprite.Group()
    Blocks = pygame.sprite.Group()
    Cerdos = pygame.sprite.Group()
    Puas = pygame.sprite.Group()
    Coins = pygame.sprite.Group()
    Apples = pygame.sprite.Group()
    Diamonds = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()
    
    
    Players.add(Player)
    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion Enemigo
    C1 = pork.cerdo([257,370], 130)
    Cerdos.add(C1)

    #Creacion Cañon
    Ca = ca.cannon([CannonsPos[0]['x'],CannonsPos[0]['y']])
    Cannons.add(Ca)

    #Creacion de las puas
    for i in range(len(SpikesPos)):
        pincho = Spikes.spikes([(SpikesPos[i]['x']),(SpikesPos[i]['y'])],SpikesPos[i]['width'],SpikesPos[i]['height'])
        Puas.add(pincho)
    #Creacion de los bloques
    for i in range(len(Collisions)):
        Bloque = Block.Bloque([(Collisions[i]['x']),(Collisions[i]['y'])],Collisions[i]['width'],Collisions[i]['height'])
        Blocks.add(Bloque)
    #Creacion de las plataformas
    for i in range(len(Platforms)):
        Platform = Block.Bloque([(Platforms[i]['x']),(Platforms[i]['y'])],Platforms[i]['width'],Platforms[i]['height'])
        Blocks.add(Platform)
    for i in range(len(CannonsPos)):
        cannon = Block.Bloque([(CannonsPos[i]['x']),(CannonsPos[i]['y'])],CannonsPos[i]['width'],CannonsPos[i]['height'])
        Blocks.add(cannon)
    #Creacion de las monedas
    for i in range(len(CoinsPos)):
        Moneda = co.Coin((CoinsPos[i]['x'],CoinsPos[i]['y']))
        Coins.add(Moneda)
    #Creacion de las manzanas
    for i in range(len(ApplesPos)):
        Manzana = ap.Apple((ApplesPos[i]['x'],ApplesPos[i]['y']))
        Apples.add(Manzana)
    #Creacion de las manzanas
    for i in range(len(DiamondsPos)):
        Diamante = d.Diamond((DiamondsPos[i]['x'],DiamondsPos[i]['y']))
        Diamonds.add(Diamante)
    #Asignacion de lista de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    for Cerdo in Cerdos:
        Cerdo.Bloques = Blocks
        
    #Movimiento Jugador
    while (True):
        #event managment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Player.velx = 3
                if event.key == pygame.K_LEFT:
                    Player.velx = -3
                if event.key == pygame.K_SPACE:
                    if Player.EnAire == False:
                        Player.vely = -8
                        Player.EnAire = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    Player.velx = 0
                if event.key == pygame.K_LEFT:
                    Player.velx = 0

        #Colisiones e interacciones
        for Player in Players:
            listaColisionPuas=pygame.sprite.spritecollide(Player,Puas,False)
            for b in listaColisionPuas:
                if ((Player.rect.right >= b.rect.left) and (Player.rect.right <= b.rect.right)):
                    print("chuzao pai")
                elif ((Player.rect.left <= b.rect.right) and (Player.rect.left >= b.rect.left)):
                    print("chuzao pai")

                if ((Player.rect.bottom >= b.rect.top) and (Player.rect.bottom <= b.rect.bottom)):
                    print("chuzao pai")
                elif ((Player.rect.top <= b.rect.bottom) and (Player.rect.top >= b.rect.top)):
                    print("chuzao pai")

            listaColisionCerdos=pygame.sprite.spritecollide(Player,Cerdos,False)
            for b in listaColisionCerdos:
                if ((Player.rect.right >= b.rect.left) and (Player.rect.right <= b.rect.right)):
                    print("Encerdado pai")
                elif ((Player.rect.left <= b.rect.right) and (Player.rect.left >= b.rect.left)):
                    print("Encerdado pai")

                if ((Player.rect.bottom >= b.rect.top) and (Player.rect.bottom <= b.rect.bottom)):
                    print("Encerdado pai")
                elif ((Player.rect.top <= b.rect.bottom) and (Player.rect.top >= b.rect.top)):
                    print("Encerdado pai")

            #Recoger Monedas
            ListaMonedas = pygame.sprite.spritecollide(Player, Coins,True)
            if ListaMonedas:
                Player.Coins = Player.Coins + 1
            #Recoger Manzanas
            ListaManzanas = pygame.sprite.spritecollide(Player, Apples,True)
            if ListaManzanas:
                Player.Apples = Player.Apples + 1
            #Recoger Manzanas
            ListaDiamantes = pygame.sprite.spritecollide(Player, Diamonds,True)
            if ListaDiamantes:
                Player.Diamonds = Player.Diamonds + 1

        print (Player.Coins)
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                Room1.StartRoom1(Player,70,260)
        #Cambia de Nivel
        if Player.rect.left > Constants.limitemovimientoX:
            Room3.StartGame(Player,-5,Player.rect.y)

        if Player.rect.right < 5:
            Room1.StartRoom1(Player,779, Player.rect.y + 1)
        
        Constants.Screen.fill([0,0,0])
        Players.update()
        Cerdos.update()
        Cannons.update()
        Constants.Screen.blit(mapa,[0,0])
        Players.draw(Constants.Screen)
        Cerdos.draw(Constants.Screen)
        Coins.draw(Constants.Screen)
        Apples.draw(Constants.Screen)
        Diamonds.draw(Constants.Screen)
        Cannons.draw(Constants.Screen)
        pygame.display.flip()
        Clock.tick(40)

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