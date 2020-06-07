#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block
from Classes import PlataformaMovilHorizontal as PMH
from Classes import PlataformaMovilVertical as PMV
from Classes import CajaEstatica as CS

from pygame.locals import *

def StarGame():
    index = 0
    limitemovimiento = 780
    mapaa = pygame.image.load('Assets\Level1\Level1a.png')

    #Definicion de Grupos
    jugadores = pygame.sprite.Group()
    Plataformas = pygame.sprite.Group()
    Bloques = pygame.sprite.Group()


    #Creacion Jugador
    j = P.Jugador([50,250])
    jugadores.add(j)


    #Lectura de archivo json
    nom_archivo='Assets\Level1\Level1a.json'
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




        if j.rect.x > limitemovimiento:
            j.rect.x = 0
            index = 1
        
        Constants.Screen.fill([0,0,0])
        Constants.Screen.blit(mapaa,[0,0])
        jugadores.update()
        Bloques.update()
        Plataformas.update()
        jugadores.draw(Constants.Screen)
        Bloques.draw(Constants.Screen)
        pygame.display.flip()
        reloj.tick(40)
