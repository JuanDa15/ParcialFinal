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
from Classes import Coin as co
from Classes import Apple as ap
from Classes import Diamond as d
from CRUD.Level1 import Room2

from pygame.locals import *

def StartRoom1(Player, PositionX,PositionY):
    Clock = pygame.time.Clock()
    mapa = Constants.mapa1A

    #Definicion de Grupos
    Players = pygame.sprite.Group()
    Blocks = pygame.sprite.Group()
    Cerdos=pygame.sprite.Group()

    Players.add(Player)
    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Creacion Enemigos
    C1 = pork.cerdo([100,320], 130)
    Cerdos.add(C1)

    C2 = pork.cerdo([610,345], 100)
    #Pixeles antes de devolverse
    C2.Movidos = 0
    Cerdos.add(C2)
    
    #Creacion de las paredes
    for i in range(len(Constants.Collisions)):
        Bloque = Block.Bloque([(Constants.Collisions[i]['x']),(Constants.Collisions[i]['y'])],Constants.Collisions[i]['width'],Constants.Collisions[i]['height'])
        Blocks.add(Bloque)
    #Creacion de las plataformas
    for i in range(len(Constants.Platforms)):
        Platform = Block.Bloque([(Constants.Platforms[i]['x']),(Constants.Platforms[i]['y'])],Constants.Platforms[i]['width'],Constants.Platforms[i]['height'])
        Blocks.add(Platform)

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
        #Colisiones Jugador con los cerdos
        for Player in Players:
            listaColisionCerdos=pygame.sprite.spritecollide(Player,Cerdos,False)
            for b in listaColisionCerdos:
                if ((Player.rect.right >= b.rect.left) and (Player.rect.right <= b.rect.right)):
                    print("Encerdado pai")
                    Player.vida -= 1
                elif ((Player.rect.left <= b.rect.right) and (Player.rect.left >= b.rect.left)):
                    print("Encerdado pai")
                    Player.vida -= 1
                if ((Player.rect.bottom >= b.rect.top) and (Player.rect.bottom <= b.rect.bottom)):
                    print("Encerdado pai")
                    Player.vida -= 1
                elif ((Player.rect.top <= b.rect.bottom) and (Player.rect.top >= b.rect.top)):
                    print("Encerdado pai")
                    Player.vida -= 1
            #Recoger Monedas
            ListaMonedas = pygame.sprite.spritecollide(Player, Constants.CoinsList,True)
            for Moneda in ListaMonedas:
                Player.Coins = Player.Coins + 1
            #Recoger Manzanas
            ListaManzanas = pygame.sprite.spritecollide(Player, Apples,True)
            if ListaManzanas:
                Player.Apples = Player.Apples + 1
            #Recoger Manzanas
            ListaDiamantes = pygame.sprite.spritecollide(Player, Diamonds,True)
            if ListaDiamantes:
                Player.Diamonds = Player.Diamonds + 1
                
        print (ListaMonedas)
        print (Player.Coins)
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                StartRoom1(Player,100,280)
        #Cambia de Nivel
        if Player.rect.left > Constants.limitemovimientoX:
            Room2.StartRoom2(Player,-5,Player.rect.y - 1)


        Constants.Screen.fill([0,0,0])
        Players.update()
        Blocks.update()
        Cerdos.update()
        Constants.Screen.blit(mapa,[0,0])
        Players.draw(Constants.Screen)
        Cerdos.draw(Constants.Screen)   
        Constants.CoinsList.draw(Constants.Screen)
        Apples.draw(Constants.Screen)
        Diamonds.draw(Constants.Screen)
        pygame.display.flip()
        Clock.tick(30)