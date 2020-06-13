#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from CRUD.Level1 import Room1 as R1
from Classes import Block
from pygame.locals import *


#Creacion Jugador
Player = P.Jugador([0,0])
R1.StartRoom1(Player,100, 280)

def StarGame():
    end = False
    while not end:
        #event managment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
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

        
        Constants.Screen.fill([0,0,0])
        Players.update()
        Blocks.update()
        Cerdos.update()
        Blocks.draw(Constants.Screen)
        Constants.Screen.blit(mapa,[0,0])
        Players.draw(Constants.Screen)
        Cerdos.draw(Constants.Screen)
        pygame.display.flip()
        pygame.display.flip()