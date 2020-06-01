#Import of libraries
import pygame
import sys
import json
from Classes import Block

pygame.init()

Screen = pygame.display.set_mode([1080,720])
Container = pygame.Rect(100,50,900,620)
mapa = pygame.image.load('Assets\Maps\Level1\Level1.png')
#------------------------------
def Main_Menu():
    #Definition of variables-----------------
    #music upload
    end = False
    while not end:
        #event managment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        
        nom_archivo='Assets\Maps\Level1\Level1.json'
        mapa_info = None
        with open(nom_archivo) as info:
            mapa_info=json.load(info)
        info.close()

        dicc_mapa=mapa_info['layers'][8]['objects']
        
        Bloques = pygame.sprite.Group()
        
        for i in range(len(dicc_mapa)):
            Bloque = Block.Bloque([(100 + dicc_mapa[i]['x']),(50 + dicc_mapa[i]['y'])],dicc_mapa[i]['width'],dicc_mapa[i]['height'])
            Bloques.add(Bloque)
            
        pygame.draw.rect(Screen,[255,255,255],Container)
        Screen.blit(mapa,[100,50])
        Bloques.update()
        Bloques.draw(Screen)
        pygame.display.flip()
    
Main_Menu()
