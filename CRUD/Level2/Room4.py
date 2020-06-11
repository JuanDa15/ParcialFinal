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
from Classes import Cannon
from Classes import CannonBall
from Classes import pork
from Classes import Spikes

from CRUD.Level2 import Room5
from CRUD.Level2 import Room3

from pygame.locals import *

def StartGame(j ,posx, posy):
    index = 0
    limitemovimiento = 790
    mapaa = pygame.image.load('Assets\Levels\Level2\Level2d.png')

    #Definicion de Grupos
    jugadores = pygame.sprite.Group()
    Plataformas = pygame.sprite.Group()
    Bloques = pygame.sprite.Group()
    Cañones = pygame.sprite.Group()
    BolasCañon = pygame.sprite.Group()
    Cerdos = pygame.sprite.Group()
    Puas = pygame.sprite.Group()


    #Creacion Jugador
    jugadores.add(j)

    C = pork.cerdo([257,370], 130)
    Cerdos.add(C)

    for j in jugadores:
        j.rect.x = posx
        j.rect.y = posy

    
    for j in jugadores:
        print(j.vida)

    #Lectura de archivo json
    nom_archivo='Assets\Levels\Level2\Level2d.json'
    mapa_info = None
    with open(nom_archivo) as info:
        mapa_info=json.load(info)
    info.close()

    Dicc_Colisiones=mapa_info['layers'][6]['objects']
    #Dicc_Plataformas= mapa_info['layers'][12]['objects']
    #Dicc_Cañones= mapa_info['layers'][15]['objects']
    #Dicc_Pinchos= mapa_info['layers'][8]['objects']

    """
    #Creacion de los spikes
    for i in range(len(Dicc_Pinchos)):
        pincho = Spikes.spikes([(Dicc_Pinchos[i]['x']),(Dicc_Pinchos[i]['y'])],Dicc_Pinchos[i]['width'],Dicc_Pinchos[i]['height'])
        Puas.add(pincho)
    """

    #Creacion de los bloques
    for i in range(len(Dicc_Colisiones)):
        Bloque = Block.Bloque([(Dicc_Colisiones[i]['x']),(Dicc_Colisiones[i]['y'])],Dicc_Colisiones[i]['width'],Dicc_Colisiones[i]['height'])
        Bloques.add(Bloque)
    
    """
    #Creacion de las plataformas
    for i in range(len(Dicc_Plataformas)):
        Plataforma = Block.Bloque([(Dicc_Plataformas[i]['x']),(Dicc_Plataformas[i]['y'])],Dicc_Plataformas[i]['width'],Dicc_Plataformas[i]['height'])
        Bloques.add(Plataforma)

    #Creacion de los cañones
    for i in range(len(Dicc_Cañones)):
        C = Cannon.cannon([(Dicc_Cañones[i]['x']),(Dicc_Cañones[i]['y'])],(Dicc_Cañones[i]['width']),(Dicc_Cañones[i]['height']))
        if Dicc_Cañones[i]['name'] == 'False':
            C.Direccion = False
        else:
            C.Direccion = True
        Cañones.add(C)
    """


    for i in jugadores:
        i.Bloques = Bloques
    
    for c in Cañones:
        c.Bloques = Bloques

    for c in Cerdos:
        c.Bloques = Bloques

    
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
                    #if j.EnAire == False:
                    j.vely = -8
                    j.EnAire = True


                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    j.velx = 0
                if event.key == pygame.K_LEFT:
                    j.velx = 0

        for c in Cañones:
            if c.Disparo == 0:
                if c.Direccion == True:
                    B = CannonBall.cannonball([c.rect.x, c.rect.y + 4], 5)
                    B.Bloques = Bloques
                    BolasCañon.add(B)
                    c.Disparo = 80
                else:
                    B = CannonBall.cannonball([c.rect.x, c.rect.y + 4], -5)
                    B.Bloques = Bloques
                    BolasCañon.add(B)
                    c.Disparo = 80
            else:
                c.Disparo -= 1

        for Bola in BolasCañon:
            listaColision=pygame.sprite.spritecollide(Bola,Bloques,False)
            for b in listaColision:
                if ((Bola.rect.right >= b.rect.left) and (Bola.rect.right <= b.rect.right)):
                    BolasCañon.remove(Bola)
                elif ((Bola.rect.left <= b.rect.right) and (Bola.rect.left >= b.rect.left)):
                    BolasCañon.remove(Bola)
        
        for j in jugadores:
            listaColisionPuas=pygame.sprite.spritecollide(j,Puas,False)
            for b in listaColisionPuas:
                if ((j.rect.right >= b.rect.left) and (j.rect.right <= b.rect.right)):
                    print("chuzao pai")
                elif ((j.rect.left <= b.rect.right) and (j.rect.left >= b.rect.left)):
                    print("chuzao pai")

                if ((j.rect.bottom >= b.rect.top) and (j.rect.bottom <= b.rect.bottom)):
                    print("chuzao pai")
                elif ((j.rect.top <= b.rect.bottom) and (j.rect.top >= b.rect.top)):
                    print("chuzao pai")


            listaColisionBolasCañon=pygame.sprite.spritecollide(j,BolasCañon,False)
            for b in listaColisionBolasCañon:
                if ((j.rect.right >= b.rect.left) and (j.rect.right <= b.rect.right)):
                    print("Bolazo pai")
                elif ((j.rect.left <= b.rect.right) and (j.rect.left >= b.rect.left)):
                    print("Bolazo pai")

                if ((j.rect.bottom >= b.rect.top) and (j.rect.bottom <= b.rect.bottom)):
                    print("Bolazo pai")
                elif ((j.rect.top <= b.rect.bottom) and (j.rect.top >= b.rect.top)):
                    print("Bolazo pai")
            
            listaColisionCerdos=pygame.sprite.spritecollide(j,Cerdos,False)
            for b in listaColisionCerdos:
                if ((j.rect.right >= b.rect.left) and (j.rect.right <= b.rect.right)):
                    print("Encerdado pai")
                elif ((j.rect.left <= b.rect.right) and (j.rect.left >= b.rect.left)):
                    print("Encerdado pai")

                if ((j.rect.bottom >= b.rect.top) and (j.rect.bottom <= b.rect.bottom)):
                    print("Encerdado pai")
                elif ((j.rect.top <= b.rect.bottom) and (j.rect.top >= b.rect.top)):
                    print("Encerdado pai")

            for j in jugadores:
                if j.rect.y >= Constants.Height + 10:
                    StartGame(j,5, 315)


        if j.rect.left > limitemovimiento:
            Room5.StartGame(j,0, j.rect.y)

        if j.rect.right < 0:
            Room4.StartGame(j, Constants.Width - 26, j.rect.y - 2)
        
        Constants.Screen.fill([0,0,0])
        jugadores.update()
        Plataformas.update()
        Cañones.update()
        BolasCañon.update()
        Cerdos.update()
        Puas.draw(Constants.Screen)
        Constants.Screen.blit(mapaa,[0,0])
        Bloques.draw(Constants.Screen)
        jugadores.draw(Constants.Screen)
        Cañones.draw(Constants.Screen)
        BolasCañon.draw(Constants.Screen)
        Cerdos.draw(Constants.Screen)
        pygame.display.flip()
        reloj.tick(40)

        