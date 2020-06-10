"""
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
    index = 0
    indexy = 0
    limitemovimiento = 799
    limitemovimientoy = 590
    """
    mapaa = pygame.image.load('Assets\Levels\Level1\Level1a.png')
    mapab = pygame.image.load('Assets\Levels\Level1\Level1b.png')
    mapac = pygame.image.load('Assets\Levels\Level1\Level1c.png')
    mapad = pygame.image.load('Assets\Levels\Level1\Level1d.png')
    mapae = pygame.image.load('Assets\Levels\Level1\Level1e.png')
    mapaf = pygame.image.load('Assets\Levels\Level1\level1f.png')
    mapag = pygame.image.load('Assets\Levels\Level1\level1g.png')
    mapah = pygame.image.load('Assets\Levels\Level1\level1h.png')
    mapai = pygame.image.load('Assets\Levels\Level1\level1i.png')
    mapaj = pygame.image.load('Assets\Levels\Level1\level1j.png')
    level1 = [mapaa,mapab,mapac,mapad,mapae,mapaf,mapag,mapah,mapai,mapaj]
    rectfondo = level1[index].get_rect()
    """
    """
    mapaa = pygame.image.load('Assets\Levels\Level2\Level2a.png')
    mapab = pygame.image.load('Assets\Levels\Level2\Level2b.png')
    mapac = pygame.image.load('Assets\Levels\Level2\Level2c.png')
    mapad = pygame.image.load('Assets\Levels\Level2\Level2d.png')
    mapae = pygame.image.load('Assets\Levels\Level2\Level2e.png')
    mapaf = pygame.image.load('Assets\Levels\Level2\Level2f.png')
    mapag = pygame.image.load('Assets\Levels\Level2\Level2g.png')
    mapah = pygame.image.load('Assets\Levels\Level2\Level2h.png')
    mapai = pygame.image.load('Assets\Levels\Level2\Level2i.png')
    mapaj = pygame.image.load('Assets\Levels\Level2\Level2j.png')
    level2 = [mapaa,mapab,mapac,mapad,mapae,mapaf,mapag,mapah,mapai,mapaj]
    rectfondo = level2[index].get_rect()
    """
    mapaa = pygame.image.load('Assets\Levels\Final Boss\FinalBossA.png')
    mapab = pygame.image.load('Assets\Levels\Final Boss\FinalBossB.png')
    level3 = [mapaa,mapab]

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
                    j.velx = j.velx + 5
                    j.vely = 0
                if event.key == pygame.K_LEFT:
                    j.velx = j.velx -5
                    j.vely = 0
                if event.key == pygame.K_UP:
                    j.vely = j.vely - 5
                    j.velx = 0
                if event.key == pygame.K_DOWN:
                    j.vely = j.vely + 5
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
        longitud = len(level3)

        if j.rect.x > limitemovimiento:
            j.rect.x = 1
            index += 1
        if j.rect.right < 10:
            j.rect.x = 775
            index -=1
        """ Map movement level 1
        if j.rect.x > limitemovimiento:
            j.rect.x = 1
            index += 1
        if j.rect.right < 10:
            j.rect.x = 775
            index -=1

        if (j.rect.y > limitemovimientoy) and ((index >= 2) and (index < 6)):
            j.rect.y = 0
            index += 1
        if (j.rect.bottom < 10) and ((index >= 2) and (index < 6)):
            j.rect.y = 590
            index -=1
        
        if(j.rect.bottom < 4) and (index >= 6):
            j.rect.y = 574
            index += 1
        if(j.rect.top > 600) and (index >= 6):
            j.rect.y = 26
            index -= 1 
        """
        Constants.Screen.fill([0,0,0])
        Constants.Screen.blit(level3[index],[0,0])
        jugadores.update()
        jugadores.draw(Constants.Screen)
        pygame.display.flip()
"""