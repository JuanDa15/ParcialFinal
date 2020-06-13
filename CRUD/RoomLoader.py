
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
from CRUD.Level1 import Room3 as R3
from CRUD.Level1 import Room4 as R4
from CRUD.Level1 import Room5 as R5
from CRUD.Level1 import Room6 as R6
from CRUD.Level1 import Room7 as R7
from CRUD.Level1 import Room8 as R8
from CRUD.Level1 import Room9 as R9
from CRUD.Level1 import Room10 as R10

from pygame.locals import *

def LoadRoom(Player,Players,Blocks,Cerdos,Clock,mapa,Puas,Cannons,level_type,prevRoom,nextRoom,currentLevel,currentRoom):
    #Movimiento Jugador
    # --type
    # 0 - StartLevel ->  [=
    # 1 - normal corridor -> = + =
    # 2 - Corridor + downfall ->  = + ╗
    # 3 - downfall corridor -> ║ + ║
    # 4 - downfall + corridor -> ╗ + =
    # 5 - Corridor + Climb 
    # 6 - Climb corridor
    # 7 - Climb + Corridor

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

    #Colisiones Jugador con Puas
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

    if Cerdos != None:
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
    
    for Player in Players:
        #Recoger Monedas
        ListaMonedas = eval('pygame.sprite.spritecollide(Player, Constants.Coins'+currentLevel+currentRoom+',True)')
        for i in ListaMonedas:
            Constants.CoinsList.remove(i)
        if ListaMonedas:
            Player.Coins = Player.Coins + 1

        #Recoger Manzanas
        ListaManzanas = eval('pygame.sprite.spritecollide(Player, Constants.Apples'+currentLevel+currentRoom+',True)')
        for i in ListaManzanas:
            Constants.ApplesList.remove(i)
        if ListaManzanas:
            Player.Apples = Player.Apples + 1
        #Recoger Diamantes
        ListaDiamantes = eval('pygame.sprite.spritecollide(Player, Constants.Diamonds'+currentLevel+currentRoom+',True)')
        for i in ListaDiamantes:
            Constants.DiamondsList.remove(i)
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
                        return eval('R' + nextRoom + '.StartRoom(Player,Players,-6,Player.rect.y - 1)')
    if level_type == 1:
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                return R1.StartRoom(Player,Players,100, 280)
        #Cambia de Nivel
            if Player.rect.left > Constants.limitemovimientoX:
                return eval('R' + nextRoom + '.StartRoom(Player,Players,-6,Player.rect.y + 1)')
            if Player.rect.right < 5:
                return eval('R' + prevRoom + '.StartRoom(Player,Players,779,Player.rect.y - 1)')
            
    if level_type == 2:
        #Cambia de Nivel
            if Player.rect.top > Constants.limitemovimientoY:
                return eval('R' + nextRoom + '.StartRoom(Player,Players,Player.rect.x,-6)')
            if Player.rect.right < 5:
                return eval('R' + prevRoom + '.StartRoom(Player,Players,779,Player.rect.y)')

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
    eval('Constants.Coins'+currentLevel+currentRoom+'.draw(Constants.Screen)')
    eval('Constants.Apples'+currentLevel+currentRoom+'.draw(Constants.Screen)')
    eval('Constants.Diamonds'+currentLevel+currentRoom+'.draw(Constants.Screen)')
    if Cannons != None:
        Cannons.draw(Constants.Screen)
    pygame.display.flip()
    Clock.tick(30)