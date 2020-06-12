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
from CRUD.Level1 import Room1 as R1
from CRUD.Level1 import Room2 as R2

from pygame.locals import *

def LoadRoom(Player,Players,Blocks,Cerdos,Clock,mapa,Puas,Cannons,level_type,prevRoom,nextRoom,currentLevel):
    #Movimiento Jugador
    # --type
    # 0 - StartLevel ->  [=
    # 1 - normal corridor -> = + =
    # 2 - Corridor + downfall ->  = + ╗
    # 3 - downfall corridor -> ║ + ║
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
    if Puas != None:
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
        ListaMonedas = eval('pygame.sprite.spritecollide(Player, Constants.Coins'+currentLevel+',True)')
        for i in ListaMonedas:
            Constants.CoinsList.remove(i)
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

    if level_type == 0:
        # 1 Left - 2 Right - 3 Restart     
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                return R1.StartRoom(Player,Players,100, 280)
            #Cambia de Nivel
            if Player.rect.left > Constants.limitemovimientoX:
                if nextRoom != None:
                    return eval('R' + nextRoom + '.StartRoom(Player,Players,6,Player.rect.y - 1)')
    if level_type == 1:
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                return R1.StartRoom(Player,Players,100, 280)
        #Cambia de Nivel
            if Player.rect.left > Constants.limitemovimientoX:
                return eval('R' + nextRoom + '.StartRoom(Player,Players,6,Player.rect.y - 1)')
            if Player.rect.right < 5:
                return eval('R' + prevRoom + '.StartRoom(Player,Players,794,Player.rect.y - 1)')
            
    if level_type == 2:
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                return R1.StartRoom(Player,Players,100, 280)
        #Cambia de Nivel
            if Player.rect.left > Constants.limitemovimientoX:
                return eval('R' + nextRoom + '.StartRoom(Player,Players,6,Player.rect.y - 1)')
            if Player.rect.right < 5:
                return eval('R' + prevRoom + '.StartRoom(Player,Players,794,Player.rect.y - 1)')

    Constants.Screen.fill([0,0,0])
    Players.update()
    Blocks.update()
    if Cerdos != None:
        Cerdos.update()
    if Cannons != None:
        Cannons.update()
    Constants.Screen.blit(mapa,[0,0])
    Players.draw(Constants.Screen)
    if Cerdos != None:
        Cerdos.draw(Constants.Screen)   
    eval('Constants.Coins'+currentLevel+'.draw(Constants.Screen)')
    Constants.ApplesList.draw(Constants.Screen)
    Constants.DiamondsList.draw(Constants.Screen)
    if Cannons != None:
        Cannons.draw(Constants.Screen)
    pygame.display.flip()
    Clock.tick(30)