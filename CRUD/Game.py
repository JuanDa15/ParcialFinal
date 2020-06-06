#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block
from pygame.locals import *

def StarGame():
    mapa = pygame.image.load('Assets\Levels\Level1\Level1a.png')
    jugadores = pygame.sprite.Group()
    j = P.Jugador([100,100])
    jugadores.add(j)
    while (True):
        #event managment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx = j.velx + 1
                    j.vely = 0
                if event.key == pygame.K_LEFT:
                    j.velx = j.velx -1
                    j.vely = 0
                if event.key == pygame.K_UP:
                    j.vely = j.vely - 1
                    j.velx = 0
                if event.key == pygame.K_DOWN:
                    j.vely = j.vely + 1
                    j.velx = 0 
            if event.type == pygame.KEYUP:
                j.vely = 0
                j.velx = 0
        
        """
        Bloques = pygame.sprite.Group()
        
        collisions = L3.GetTraps()
        for i in range(len(collisions)):
            Bloque = Block.Bloque([(100 + collisions[i]['x']),(50 + collisions[i]['y'])],collisions[i]['width'],collisions[i]['height'])
            Bloques.add(Bloque)
            
        
        Constants.Screen.blit(L3.L3map,[100,50])
        Bloques.update()
        Bloques.draw(Constants.Screen)
        """
        Constants.Screen.fill([0,0,0])
        Constants.Screen.blit(mapa,[0,0])
        jugadores.update()
        jugadores.draw(Constants.Screen)
        pygame.display.flip()
