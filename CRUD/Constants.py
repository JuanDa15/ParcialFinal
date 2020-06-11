#Libraries Import
import pygame
from pygame.locals import *
#CONSTANTS
Width = 800
Height = 608
limitemovimientoX = 795
#Pygame Init
pygame.init()
pygame.display.set_caption('Tittle Game')
Screen = pygame.display.set_mode([Width,Height])
#Mapa Tutorial
MapaTutorial = pygame.image.load('Assets\Levels\Tutorial\Tutorial.png')
#Mapa nivel 1
mapa1A = pygame.image.load('Assets\Levels\Level1\Level1a.png')
mapa1B = pygame.image.load('Assets\Levels\Level1\Level1b.png')
mapa1C = pygame.image.load('Assets\Levels\Level1\Level1c.png')
mapa1D = pygame.image.load('Assets\Levels\Level1\Level1d.png')
mapa1E = pygame.image.load('Assets\Levels\Level1\Level1e.png')
mapa1F = pygame.image.load('Assets\Levels\Level1\Level1f.png')
mapa1G = pygame.image.load('Assets\Levels\Level1\Level1g.png')
mapa1H = pygame.image.load('Assets\Levels\Level1\Level1h.png')
mapa1I = pygame.image.load('Assets\Levels\Level1\Level1i.png')
mapa1J = pygame.image.load('Assets\Levels\Level1\Level1j.png')
#Mapa nivel 2
mapa2A = pygame.image.load('Assets\Levels\Level2\Level2a.png')
mapa2B = pygame.image.load('Assets\Levels\Level2\Level2b.png')
mapa2C = pygame.image.load('Assets\Levels\Level2\Level2c.png')
mapa2D = pygame.image.load('Assets\Levels\Level2\Level2d.png')
mapa2E = pygame.image.load('Assets\Levels\Level2\Level2e.png')
mapa2F = pygame.image.load('Assets\Levels\Level2\Level2f.png')
mapa2G = pygame.image.load('Assets\Levels\Level2\Level2g.png')
mapa2H = pygame.image.load('Assets\Levels\Level2\Level2h.png')
mapa2I = pygame.image.load('Assets\Levels\Level2\Level2i.png')
mapa2J = pygame.image.load('Assets\Levels\Level2\Level2j.png')
#Mapa Final Boss
MapaFinalA = pygame.image.load('Assets\Levels\Final Boss\FinalBossA.png')
MapaFinalB = pygame.image.load('Assets\Levels\Final Boss\FinalBossB.png')