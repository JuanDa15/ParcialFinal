#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block
from Classes import Cannon as ca
from Classes import pork
from Classes import Spikes
from CRUD.Level1 import Room1
from CRUD.Level1 import Room3
from CRUD.Level1 import Room5

from pygame.locals import *

def StartRoom4(Player,positionX, positionY):
    mapa = Constants.mapa1D
    Clock = pygame.time.Clock()

    #Definicion de Grupos
    Players = pygame.sprite.Group()
    Blocks = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()
    Cerdos = pygame.sprite.Group()
    Puas = pygame.sprite.Group()

    Players.add(Player)
    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = positionX
        Player.rect.y = positionY

    #Creacion de los spikes
    for i in range(len(Constants.SpikesPosD)):
        pincho = Spikes.spikes([(Constants.SpikesPosD[i]['x']),(Constants.SpikesPosD[i]['y'])],Constants.SpikesPosD[i]['width'],Constants.SpikesPosD[i]['height'])
        Puas.add(pincho)
    #Creacion de las colisiones
    for i in range(len(Constants.CollisionsD)):
        Bloque = Block.Bloque([(Constants.CollisionsD[i]['x']),(Constants.CollisionsD[i]['y'])],Constants.CollisionsD[i]['width'],Constants.CollisionsD[i]['height'])
        Blocks.add(Bloque)
        
    for i in range(len(Constants.PlatformsD)):
        Plataforma = Block.Bloque([(Constants.PlatformsD[i]['x']),(Constants.PlatformsD[i]['y'])],Constants.PlatformsD[i]['width'],Constants.PlatformsD[i]['height'])
        Blocks.add(Plataforma)

    for i in range (len(Constants.CannonsPosD)):
        Cannon = Block.Bloque([(Constants.CannonsPosD[i]['x']),(Constants.CannonsPosD[i]['y'])],Constants.CannonsPosD[i]['width'],Constants.CannonsPosD[i]['height'])
        Can = ca.cannon([(Constants.CannonsPosD[i]['x']),(Constants.CannonsPosD[i]['y'])])
        Blocks.add(Cannon)
        Cannons.add(Can)
    #Asignacion de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks


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
            ListaMonedas = pygame.sprite.spritecollide(Player, Constants.CoinsList,True)
            if ListaMonedas:
                Player.Coins = Player.Coins + 1
            #Recoger Manzanas
            ListaManzanas = pygame.sprite.spritecollide(Player, Constants.ApplesList,True)
            if ListaManzanas:
                Player.Apples = Player.Apples + 1
            #Recoger Diamantes
            ListaDiamantes = pygame.sprite.spritecollide(Player, Constants.DiamondsList,True)
            if ListaDiamantes:
                Player.Diamonds = Player.Diamonds + 1
        #Retroceder mapa
        if Player.rect.bottom < 5:
            Room3.StartRoom3(Player,Player.rect.y, 579)
        #Avanzar mapa
        if Player.rect.top > Constants.limitemovimientoY:
            Room5.StartGame(Player,Player.rect.x,-5)
        
        Constants.Screen.fill([0,0,0])
        Players.update()
        Cannons.update()
        Cerdos.update()
        Constants.Screen.blit(mapa,[0,0])
        Players.draw(Constants.Screen)
        Cannons.draw(Constants.Screen)
        Cerdos.draw(Constants.Screen)
        Constants.CoinsList.draw(Constants.Screen)
        Constants.ApplesList.draw(Constants.Screen)
        Constants.DiamondsList.draw(Constants.Screen)
        pygame.display.flip()
        Clock.tick(40)
