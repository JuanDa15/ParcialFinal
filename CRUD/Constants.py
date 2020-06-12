#Libraries Import
import pygame
import json
from Classes import Coin as co
from Classes import Apple as ap
from Classes import Diamond as d
from pygame.locals import *
#CONSTANTS
Width = 800
Height = 608
limitemovimientoX = 795
limitemovimientoY = 595
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
#Listas Colecionables Nivel 1
CoinsList = pygame.sprite.Group()
ApplesList = pygame.sprite.Group()
DiamondsList = pygame.sprite.Group()
#-----------------------------------------------------------------------------------------------
MapInfo = None
#Room Information A
#Lectura de archivo json
FileName= 'Assets\Levels\Level1\Level1a.json'
with open(FileName) as Information:
    MapInfo=json.load(Information)
Information.close()
#Extraccion Objetos Json
CollisionsA = MapInfo['layers'][13]['objects']
PlatformsA = MapInfo['layers'][14]['objects']
DiamondsPosA = MapInfo['layers'][10]['objects']
ApplesPosA = MapInfo['layers'][11]['objects']
CoinsPosA = MapInfo['layers'][12]['objects']
DoorA = MapInfo['layers'][15]['objects']

#Se agregan las monedas cuarto a
for i in range(len(CoinsPosA)):
    Moneda = co.Coin((CoinsPosA[i]['x'],CoinsPosA[i]['y']))
    CoinsList.add(Moneda)
#Se agregan las Manzanas cuarto a
for i in range(len(ApplesPosA)):
    Manzana = ap.Apple((ApplesPosA[i]['x'],ApplesPosA[i]['y']))
    ApplesList.add(Manzana)
#Se agregan los diamantes cuarto a
for i in range(len(DiamondsPosA)):
    Diamante = d.Diamond((DiamondsPosA[i]['x'],DiamondsPosA[i]['y']))
    DiamondsList.add(Diamante)

#Room Information b
#Map Information
#Lectura de archivo json
FileName= 'Assets\Levels\Level1\Level1b.json'

with open(FileName) as Information:
    MapInfo=json.load(Information)
Information.close()
#Extraccion Objetos Json
CollisionsB = MapInfo['layers'][10]['objects']
PlatformsB = MapInfo['layers'][11]['objects']
CoinsPosB = MapInfo['layers'][12]['objects']
ApplesPosB = MapInfo['layers'][13]['objects']
DiamondsPosB = MapInfo['layers'][14]['objects']
CannonsPosB= MapInfo['layers'][15]['objects']
SpikesPosB= MapInfo['layers'][16]['objects']

#Creacion de las monedas
for i in range(len(CoinsPosB)):
    Moneda = co.Coin((CoinsPosB[i]['x'],CoinsPosB[i]['y']))
    CoinsList.add(Moneda)
#Creacion de las manzanas
for i in range(len(ApplesPosB)):
    Manzana = ap.Apple((ApplesPosB[i]['x'],ApplesPosB[i]['y']))
    ApplesList.add(Manzana)
#Creacion de las manzanas
for i in range(len(DiamondsPosB)):
    Diamante = d.Diamond((DiamondsPosB[i]['x'],DiamondsPosB[i]['y']))
    DiamondsList.add(Diamante)
    
#Room information C
#Lectura de archivo json
FileName='Assets\Levels\Level1\Level1c.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

CollisionsC = MapInfo['layers'][10]['objects']
MovingPlatformSC = MapInfo['layers'][11]['objects']
SpikesPosC = MapInfo['layers'][12]['objects']
CoinsPosC = MapInfo['layers'][13]['objects']
DiamondsPosC = MapInfo['layers'][14]['objects']
ApplesPosC = MapInfo['layers'][15]['objects']
PlatformsC= MapInfo['layers'][17]['objects']
CannonsPosC = MapInfo['layers'][16]['objects']

#Creacion de las monedas
for i in range(len(CoinsPosC)):
    Moneda = co.Coin((CoinsPosC[i]['x'],CoinsPosC[i]['y']))
    CoinsList.add(Moneda)
#Creacion de las manzanas
for i in range(len(ApplesPosC)):
    Manzana = ap.Apple((ApplesPosC[i]['x'],ApplesPosC[i]['y']))
    ApplesList.add(Manzana)
#Creacion de las manzanas
for i in range(len(DiamondsPosC)):
    Diamante = d.Diamond((DiamondsPosC[i]['x'],DiamondsPosC[i]['y']))
    DiamondsList.add(Diamante)
#Room information D
#Lectura de archivo json
FileName='Assets\Levels\Level1\Level1d.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

CollisionsD = MapInfo['layers'][15]['objects']
PlatformsD= MapInfo['layers'][13]['objects']
SpikesPosD = MapInfo['layers'][4]['objects']
LeverPosD = MapInfo['layers'][5]['objects']
MovingPlatformSD = MapInfo['layers'][12]['objects']
MovingPlatformED = MapInfo['layers'][14]['objects']
CoinsPosD = MapInfo['layers'][16]['objects']
DiamondsPosD = MapInfo['layers'][17]['objects']
ApplesPosD = MapInfo['layers'][18]['objects']
CannonsPosD = MapInfo['layers'][19]['objects']

#Creacion de las monedas
for i in range(len(CoinsPosD)):
    Moneda = co.Coin((CoinsPosD[i]['x'],CoinsPosD[i]['y']))
    CoinsList.add(Moneda)
#Creacion de las manzanas
for i in range(len(ApplesPosD)):
    Manzana = ap.Apple((ApplesPosD[i]['x'],ApplesPosD[i]['y']))
    ApplesList.add(Manzana)
#Creacion de las manzanas
for i in range(len(DiamondsPosD)):
    Diamante = d.Diamond((DiamondsPosD[i]['x'],DiamondsPosD[i]['y']))
    DiamondsList.add(Diamante)
#Room information E
#Room information F
#Room information G
#Room information H
#Room information I
#Room information J