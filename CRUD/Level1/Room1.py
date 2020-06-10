#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block
from Classes import HorizontalMovingPlatform as HMP
from Classes import VerticalMovingPlatform as VMP
from Classes import StaticBox as SB
from Classes import pork
from CRUD.Level1 import Room2

from pygame.locals import *

def StartGame(j, posx,posy):
    index = 0
    limitemovimiento = 790
    mapaa = pygame.image.load('Assets\Levels\Level1\Level1a.png')

    #Definicion de Grupos
    jugadores = pygame.sprite.Group()
    Plataformas = pygame.sprite.Group()
    Bloques = pygame.sprite.Group()
    Cerdos=pygame.sprite.Group()

    jugadores.add(j)

    for j in jugadores:
        j.rect.x = posx
        j.rect.y = posy

    C = pork.cerdo([100,320], 130)
    Cerdos.add(C)

    C = pork.cerdo([610,345], 100)
    C.Movidos = 0
    Cerdos.add(C)

    """
    Ca = Cañon.Cañon([200,200])
    Cañones.add(Ca)
    """


    #Lectura de archivo json
    nom_archivo='Assets\Levels\Level1\Level1a.json'
    mapa_info = None
    with open(nom_archivo) as info:
        mapa_info=json.load(info)
    info.close()

    Dicc_Colisiones=mapa_info['layers'][13]['objects']
    Dicc_Plataformas= mapa_info['layers'][14]['objects']
    
    #Creacion de los bloques
    for i in range(len(Dicc_Colisiones)):
        Bloque = Block.Bloque([(Dicc_Colisiones[i]['x']),(Dicc_Colisiones[i]['y'])],Dicc_Colisiones[i]['width'],Dicc_Colisiones[i]['height'])
        Bloques.add(Bloque)

    #Creacion de las plataformas
    for i in range(len(Dicc_Plataformas)):
        Plataforma = Block.Bloque([(Dicc_Plataformas[i]['x']),(Dicc_Plataformas[i]['y'])],Dicc_Plataformas[i]['width'],Dicc_Plataformas[i]['height'])
        Bloques.add(Plataforma)

    for i in jugadores:
        i.Bloques = Bloques

    for c in Cerdos:
        c.Bloques = Bloques

    """
    for c in Cañones:
        c.Bloques = Bloques
    """

    reloj = pygame.time.Clock()

    while (True):
        #event managment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx = 3
                if event.key == pygame.K_LEFT:
                    j.velx = -3
                if event.key == pygame.K_SPACE:
                    if j.EnAire == False:
                        j.vely = -8
                        j.EnAire = True


                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    j.velx = 0
                if event.key == pygame.K_LEFT:
                    j.velx = 0

        """
        for c in Cañones:
            if c.Disparo == 0:
                B = BolaCañon.BolaCañon([c.rect.x, c.rect.y])
                B.Bloques = Bloques
                BolasCañon.add(B)
                c.Disparo = 80
            else:
                c.Disparo -= 1
        """
        for j in jugadores:
            listaColisionCerdos=pygame.sprite.spritecollide(j,Cerdos,False)
            for b in listaColisionCerdos:
                if ((j.rect.right >= b.rect.left) and (j.rect.right <= b.rect.right)):
                    print("Encerdado pai")
                    j.vida -= 1
                elif ((j.rect.left <= b.rect.right) and (j.rect.left >= b.rect.left)):
                    print("Encerdado pai")
                    j.vida -= 1
                if ((j.rect.bottom >= b.rect.top) and (j.rect.bottom <= b.rect.bottom)):
                    print("Encerdado pai")
                    j.vida -= 1
                elif ((j.rect.top <= b.rect.bottom) and (j.rect.top >= b.rect.top)):
                    print("Encerdado pai")
                    j.vida -= 1

            for j in jugadores:
                if j.rect.y >= Constants.Height + 10:
                    StartGame(j,38,254)


        if j.rect.left > limitemovimiento:
            Room2.StartGame(j, 0,j.rect.y)

        
 


        Constants.Screen.fill([0,0,0])
        jugadores.update()
        Bloques.update()
        Plataformas.update()
        Cerdos.update()
        Bloques.draw(Constants.Screen)
        Constants.Screen.blit(mapaa,[0,0])
        jugadores.draw(Constants.Screen)
        Cerdos.draw(Constants.Screen)
        pygame.display.flip()
        reloj.tick(40)