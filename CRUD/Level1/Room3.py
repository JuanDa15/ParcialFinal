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
from CRUD.Level1 import Room2
from CRUD.Level1 import Room4

from pygame.locals import *

def StartRoom3(Player,positionX, positionY):
    mapa = Constants.mapa1C
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

    #Creacion de las puas
    for i in range(len(Constants.SpikesPosC)):
        pincho = Spikes.spikes([(Constants.SpikesPosC[i]['x']),(Constants.SpikesPosC[i]['y'])],Constants.SpikesPosC[i]['width'],Constants.SpikesPosC[i]['height'])
        Puas.add(pincho)

    #Creacion de las colisiones
    for i in range(len(Constants.CollisionsC)):
        Bloque = Block.Bloque([(Constants.CollisionsC[i]['x']),(Constants.CollisionsC[i]['y'])],Constants.CollisionsC[i]['width'],Constants.CollisionsC[i]['height'])
        Blocks.add(Bloque)

    for i in range(len(Constants.PlatformsC)):
        platform = Block.Bloque([(Constants.PlatformsC[i]['x']),(Constants.PlatformsC[i]['y'])],Constants.PlatformsC[i]['width'],Constants.PlatformsC[i]['height'])
        Blocks.add(platform)
    
    for i in range(len(Constants.CannonsPosC)):
        cannon = Block.Bloque([(Constants.CannonsPosC[i]['x']),(Constants.CannonsPosC[i]['y'])],Constants.CannonsPosC[i]['width'],Constants.CannonsPosC[i]['height'])
        can = ca.cannon([(Constants.CannonsPosC[i]['x']),(Constants.CannonsPosC[i]['y'])])
        Blocks.add(cannon)
        Cannons.add(can)
        
    #Asignacion de lista de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks

    for Cerdo in Cerdos:
        Cerdos.Bloques = Blocks
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
              
        #Pasar Nivel
        if Player.rect.top > Constants.limitemovimientoY:
            Room4.StartRoom4(Player, Player.rect.x,-5)
        #Devolverse del nivel
        if Player.rect.right < 5:
            Room2.StartRoom2(Player,779, Player.rect.y)
        
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
