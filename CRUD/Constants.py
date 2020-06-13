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
Space = False
#Pygame Init
pygame.init()
pygame.display.set_caption('Tittle Game')
Screen = pygame.display.set_mode([Width,Height])
#Clock
Clock = pygame.time.Clock()
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
#Listas Colecionables Globales Nivel 1
CoinsList = pygame.sprite.Group()
ApplesList = pygame.sprite.Group()
DiamondsList = pygame.sprite.Group()
#Listas Indexadas monedas Nivel 1
Coins11 = pygame.sprite.Group()
Coins12 = pygame.sprite.Group()
Coins13 = pygame.sprite.Group()
Coins14 = pygame.sprite.Group()
Coins15 = pygame.sprite.Group()
Coins16 = pygame.sprite.Group()
Coins17 = pygame.sprite.Group()
Coins18 = pygame.sprite.Group()
Coins19 = pygame.sprite.Group()
Coins110 = pygame.sprite.Group()
#Listas Indexadas Manzanas Nivel 1
Apples11 = pygame.sprite.Group()
Apples12 = pygame.sprite.Group()
Apples13 = pygame.sprite.Group()
Apples14 = pygame.sprite.Group()
Apples15 = pygame.sprite.Group()
Apples16 = pygame.sprite.Group()
Apples17 = pygame.sprite.Group()
Apples18 = pygame.sprite.Group()
Apples19 = pygame.sprite.Group()
Apples110 = pygame.sprite.Group()
#Listas Indexadas Diamantes Nivel 1
Diamonds11 = pygame.sprite.Group()
Diamonds12 = pygame.sprite.Group()
Diamonds13 = pygame.sprite.Group()
Diamonds14 = pygame.sprite.Group()
Diamonds15 = pygame.sprite.Group()
Diamonds16 = pygame.sprite.Group()
Diamonds17 = pygame.sprite.Group()
Diamonds18 = pygame.sprite.Group()
Diamonds19 = pygame.sprite.Group()
Diamonds110 = pygame.sprite.Group()
#--------------------------------------------NIVEL 1-----------------------------
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
    Temporal = co.Coin((CoinsPosA[i]['x'],CoinsPosA[i]['y']))
    CoinsList.add(Temporal)
    Coins11.add(Temporal)
    
#Se agregan las Manzanas cuarto a
for i in range(len(ApplesPosA)):
    Temporal = ap.Apple((ApplesPosA[i]['x'],ApplesPosA[i]['y']))
    ApplesList.add(Temporal)
    Apples11.add(Temporal)

#Se agregan los diamantes cuarto a
for i in range(len(DiamondsPosA)):
    Temporal = d.Diamond((DiamondsPosA[i]['x'],DiamondsPosA[i]['y']))
    DiamondsList.add(Temporal)
    Diamonds11.add(Temporal)

#Room Information B

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
    Temporal = co.Coin((CoinsPosB[i]['x'],CoinsPosB[i]['y']))
    CoinsList.add(Temporal)
    Coins12.add(Temporal)

#Creacion de las manzanas
for i in range(len(ApplesPosB)):
    Temporal = ap.Apple((ApplesPosB[i]['x'],ApplesPosB[i]['y']))
    ApplesList.add(Temporal)
    Apples12.add(Temporal)

#Creacion de los diamantes
for i in range(len(DiamondsPosB)):
    Temporal = d.Diamond((DiamondsPosB[i]['x'],DiamondsPosB[i]['y']))
    DiamondsList.add(Temporal)
    Diamonds12.add(Temporal)
    
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
    Temporal = co.Coin((CoinsPosC[i]['x'],CoinsPosC[i]['y']))
    CoinsList.add(Temporal)
    Coins13.add(Temporal)

#Creacion de las manzanas
for i in range(len(ApplesPosC)):
    Temporal = ap.Apple((ApplesPosC[i]['x'],ApplesPosC[i]['y']))
    ApplesList.add(Temporal)
    Apples13.add(Temporal)

#Creacion de los diamantes
for i in range(len(DiamondsPosC)):
    Temporal = d.Diamond((DiamondsPosC[i]['x'],DiamondsPosC[i]['y']))
    DiamondsList.add(Temporal)
    Diamonds13.add(Temporal)

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
    Temporal = co.Coin((CoinsPosD[i]['x'],CoinsPosD[i]['y']))
    CoinsList.add(Temporal)
    Coins14.add(Temporal)

#Creacion de las manzanas
for i in range(len(ApplesPosD)):
    Temporal = ap.Apple((ApplesPosD[i]['x'],ApplesPosD[i]['y']))
    ApplesList.add(Temporal)
    Apples14.add(Temporal)

#Creacion de los diamantes
for i in range(len(DiamondsPosD)):
    Temporal = d.Diamond((DiamondsPosD[i]['x'],DiamondsPosD[i]['y']))
    DiamondsList.add(Temporal)
    Diamonds14.add(Temporal)

#Room information E

#Lectura de archivo json
FileName='Assets\Levels\Level1\Level1e.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

CollisionsE = MapInfo['layers'][2]['objects']
SpikesPosE = MapInfo['layers'][5]['objects']
CoinsPosE = MapInfo['layers'][11]['objects']
DiamondsPosE = MapInfo['layers'][12]['objects']
ApplesPosE = MapInfo['layers'][13]['objects']
VMovingPlatformEE = MapInfo['layers'][14]['objects']
HMovingPlatformEE = MapInfo['layers'][15]['objects']
PlatformsE = MapInfo['layers'][16]['objects']
HMovingPlatformSE = MapInfo['layers'][17]['objects']
CannonsPosE = MapInfo['layers'][18]['objects']

#Creacion de las monedas
for i in range(len(CoinsPosE)):
    Temporal = co.Coin((CoinsPosE[i]['x'],CoinsPosE[i]['y']))
    CoinsList.add(Temporal)
    Coins15.add(Temporal)

#Creacion de las manzanas
for i in range(len(ApplesPosE)):
    Temporal = ap.Apple((ApplesPosE[i]['x'],ApplesPosE[i]['y']))
    ApplesList.add(Temporal)
    Apples15.add(Temporal)

#Creacion de los diamantes
for i in range(len(DiamondsPosE)):
    Temporal = d.Diamond((DiamondsPosE[i]['x'],DiamondsPosE[i]['y']))
    DiamondsList.add(Temporal)
    Diamonds15.add(Temporal)

#Room information F

#Lectura de archivo json
FileName = 'Assets\Levels\Level1\Level1f.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

SpikesPosF= MapInfo['layers'][2]['objects']
CollisionsF = MapInfo['layers'][7]['objects']
PlatformsF = MapInfo['layers'][8]['objects']
CoinsPosF = MapInfo['layers'][9]['objects']
DiamondsPosF = MapInfo['layers'][10]['objects']
ApplesPosF = MapInfo['layers'][11]['objects']
InstakillPosF = MapInfo['layers'][12]['objects']

#Creacion de las monedas
for i in range(len(CoinsPosF)):
    Temporal = co.Coin((CoinsPosF[i]['x'],CoinsPosF[i]['y']))
    CoinsList.add(Temporal)
    Coins16.add(Temporal)

#Creacion de las manzanas
for i in range(len(ApplesPosF)):
    Temporal = ap.Apple((ApplesPosF[i]['x'],ApplesPosF[i]['y']))
    ApplesList.add(Temporal)
    Apples16.add(Temporal)

#Creacion de los diamantes
for i in range(len(DiamondsPosF)):
    Temporal = d.Diamond((DiamondsPosF[i]['x'],DiamondsPosF[i]['y']))
    DiamondsList.add(Temporal)
    Diamonds16.add(Temporal)

#Room information G

#Lectura de archivo json
FileName ='Assets\Levels\Level1\Level1g.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

VMovingPlatformSG = MapInfo['layers'][7]['objects']
CollisionsG = MapInfo['layers'][8]['objects']
PlatformsG = MapInfo['layers'][9]['objects']
InstakillPosG = MapInfo['layers'][10]['objects']
CoinsPosG = MapInfo['layers'][12]['objects']
DiamondsPosG = MapInfo['layers'][13]['objects']
ApplesPosG = MapInfo['layers'][14]['objects']
LeverPosG = MapInfo['layers'][15]['objects']

#Creacion de las monedas
for i in range(len(CoinsPosG)):
    Temporal = co.Coin((CoinsPosG[i]['x'],CoinsPosG[i]['y']))
    CoinsList.add(Temporal)
    Coins17.add(Temporal)

#Creacion de las manzanas
for i in range(len(ApplesPosG)):
    Temporal = ap.Apple((ApplesPosG[i]['x'],ApplesPosG[i]['y']))
    ApplesList.add(Temporal)
    Apples17.add(Temporal)

#Creacion de los diamantes
for i in range(len(DiamondsPosG)):
    Temporal = d.Diamond((DiamondsPosG[i]['x'],DiamondsPosG[i]['y']))
    DiamondsList.add(Temporal)
    Diamonds17.add(Temporal)

#Room information H

#Lectura de archivo json
FileName='Assets\Levels\Level1\Level1h.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

InstakillPosH = MapInfo['layers'][2]['objects']
CollisionsH = MapInfo['layers'][11]['objects']
PlatformsH = MapInfo['layers'][12]['objects']
CoinsPosH = MapInfo['layers'][13]['objects']
DiamondsPosH = MapInfo['layers'][14]['objects']
ApplesPosH = MapInfo['layers'][15]['objects']
LeverPosH = MapInfo['layers'][16]['objects']
CannonsPosH = MapInfo['layers'][17]['objects']
VMovingPlatformEH = MapInfo['layers'][18]['objects']
VMovingPlatformSSR = MapInfo['layers'][19]['objects']
VMovingPlatformESR = MapInfo['layers'][20]['objects']
VMovingPlatformE2H = MapInfo['layers'][21]['objects']

#Creacion de las monedas
for i in range(len(CoinsPosH)):
    Temporal = co.Coin((CoinsPosH[i]['x'],CoinsPosH[i]['y']))
    CoinsList.add(Temporal)
    Coins18.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPosH)):
    Temporal = ap.Apple((ApplesPosH[i]['x'],ApplesPosH[i]['y']))
    ApplesList.add(Temporal)
    Apples18.add(Temporal)

#Creacion de los diamantes
for i in range(len(DiamondsPosH)):
    Temporal = d.Diamond((DiamondsPosH[i]['x'],DiamondsPosH[i]['y']))
    DiamondsList.add(Temporal)
    Diamonds18.add(Temporal)

#Room information I

#Lectura de archivo json
FileName='Assets\Levels\Level1\Level1i.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

CollisionsI = MapInfo['layers'][7]['objects']
CoinsPosI = MapInfo['layers'][8]['objects']
ApplesPosI = MapInfo['layers'][9]['objects']
DiamondsPosI = MapInfo['layers'][10]['objects']
PlatformsI= MapInfo['layers'][11]['objects']
VMovingPlatformEI = MapInfo['layers'][12]['objects']
LeverPosI = MapInfo['layers'][13]['objects']

#Creacion de las monedas
for i in range(len(CoinsPosI)):
    Temporal = co.Coin((CoinsPosI[i]['x'],CoinsPosI[i]['y']))
    CoinsList.add(Temporal)
    Coins19.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPosI)):
    Temporal = ap.Apple((ApplesPosI[i]['x'],ApplesPosI[i]['y']))
    ApplesList.add(Temporal)
    Apples19.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondsPosI)):
    Temporal = d.Diamond((DiamondsPosI[i]['x'],DiamondsPosI[i]['y']))
    DiamondsList.add(Temporal)
    Diamonds19.add(Temporal)

#Room information J

#Lectura de archivo json
FileName='Assets\Levels\Level1\Level1j.json'
with open(FileName) as information:
    MapInfo = json.load(information)
information.close()

CollisionsJ = MapInfo['layers'][7]['objects']
ApplesPosJ = MapInfo['layers'][8]['objects']
DoorPosJ = MapInfo['layers'][9]['objects']
SpikesPosJ= MapInfo['layers'][10]['objects']

#Creacion de las manzanas
for i in range(len(ApplesPosJ)):
    Temporal = ap.Apple((ApplesPosJ[i]['x'],ApplesPosJ[i]['y']))
    ApplesList.add(Temporal)
    Apples110.add(Temporal)
