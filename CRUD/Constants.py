#Libraries Import
import pygame
import json
from Classes import Coin as co
from Classes import Minotauro
from Classes import Ciclope
from Classes import KingPig
from Classes import Apple as ap
from Classes import Diamond as d
from Classes import Potion as p
from pygame.locals import *
#CONSTANTS
Width = 800
Height = 608
limitemovimientoX = 795
limitemovimientoY = 595
LifeManager = None
ScoreManager = None
inLadder = False
Subiendo = False
Space = False
Hit = False
Shop1 = None
AppleConsumed = False
AppleTime = 0
MaxCobras = 10
CountCobras = 0
Interact = False
PlataformaMovil = False
MapInfo = None
#Pygame Init
pygame.init()
pygame.display.set_caption('Tittle Game')
Screen = pygame.display.set_mode([Width,Height])
#Clock
Clock = pygame.time.Clock()
ClockStart = None
#Mapa Tutorial
MapaTutorial = pygame.image.load('Assets\Levels\Tutorial\Tutorial2.png')
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
#--------------------------------------Tutorial------------------------------------------------------------------------
Coins01 = pygame.sprite.Group()
Diamonds01 = pygame.sprite.Group()
Apples01 = pygame.sprite.Group()
Potions01 = pygame.sprite.Group()
#Lectura de archivo json
FileName= 'Assets\Levels\Tutorial\Tutorial.json'
with open(FileName) as Information:
    MapInfo=json.load(Information)
Information.close()

WallsTutorial = MapInfo['layers'][8]['objects']
CoinsPosTuto = MapInfo['layers'][9]['objects']
DiamondsPosTuto = MapInfo['layers'][10]['objects']
ApplesPosTuto = MapInfo['layers'][11]['objects']
SpikesPosTutos = MapInfo['layers'][12]['objects']
VMovingPlatformST = MapInfo['layers'][13]['objects']
VMovingPlatformET = MapInfo['layers'][14]['objects']
WaterTutorialPos = MapInfo['layers'][15]['objects']
LavaTutorial = MapInfo['layers'][16]['objects']
PotionsPosTuto =  MapInfo['layers'][17]['objects']
CannonsPosTuto =  MapInfo['layers'][18]['objects']
LaddersPosTuto =  MapInfo['layers'][19]['objects']
DoorPosTuto =  MapInfo['layers'][20]['objects']
EnemysTuto = MapInfo['layers'][21]['objects']

#Creacion de las monedas
for i in range(len(CoinsPosTuto)):
    Temporal = co.Coin((CoinsPosTuto[i]['x'],CoinsPosTuto[i]['y']))
    Coins01.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPosTuto)):
    Temporal = ap.Apple((ApplesPosTuto[i]['x'],ApplesPosTuto[i]['y']))
    Apples01.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondsPosTuto)):
    Temporal = d.Diamond((DiamondsPosTuto[i]['x'],DiamondsPosTuto[i]['y']))
    Diamonds01.add(Temporal)
#Creacion de las posiones
for i in range(len(PotionsPosTuto)):
    Temporal = p.Potion((PotionsPosTuto[i]['x'],PotionsPosTuto[i]['y']))
    Potions01.add(Temporal)

#-------------------------------------------------------Nivel 1--------------------------------------------------------
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
#Cañones
CannonBalls01 = pygame.sprite.Group()
CannonBalls12 = pygame.sprite.Group()
CannonBalls13 = pygame.sprite.Group()
CannonBalls14 = pygame.sprite.Group()
CannonBalls15 = pygame.sprite.Group()
CannonBalls18 = pygame.sprite.Group()
CannonBalls32 = pygame.sprite.Group()

#Bombas
Bombs01 = pygame.sprite.Group()
Bombs11 = pygame.sprite.Group()
Bombs12 = pygame.sprite.Group()
Bombs13 = pygame.sprite.Group()
Bombs14 = pygame.sprite.Group()
Bombs15 = pygame.sprite.Group()
Bombs16 = pygame.sprite.Group()
Bombs17 = pygame.sprite.Group()
Bombs18 = pygame.sprite.Group()

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
Enemys1A = MapInfo['layers'][16]['objects']

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
Enemys1B = MapInfo['layers'][17]['objects']

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
Enemys1C = MapInfo['layers'][18]['objects']

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
Enemys1D = MapInfo['layers'][21]['objects']

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
Enemys1E = MapInfo['layers'][19]['objects']

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
Enemys1F = MapInfo['layers'][13]['objects']

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
Enemys1G = MapInfo['layers'][16]['objects']

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
VMovingPlatformSSR = MapInfo['layers'][18]['objects']
VMovingPlatformESR = MapInfo['layers'][19]['objects']
DoorPosH = MapInfo['layers'][20]['objects']
Enemys1H = MapInfo['layers'][21]['objects']

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
LeverPosI = MapInfo['layers'][12]['objects']

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
Jefe1 = Minotauro.Minotauro([MapInfo['layers'][11]['objects'][0]['x'],MapInfo['layers'][11]['objects'][0]['y']])



#Creacion de las manzanas
for i in range(len(ApplesPosJ)):
    Temporal = ap.Apple((ApplesPosJ[i]['x'],ApplesPosJ[i]['y']))
    ApplesList.add(Temporal)
    Apples110.add(Temporal)
    
#------------------------------------------------------Informacion de los json segundo nivel--------------------------------------------------
#Listas Colecionables Globales Nivel 2
CoinsList2 = pygame.sprite.Group()
ApplesList2 = pygame.sprite.Group()
DiamondsList2 = pygame.sprite.Group()
#PotionsList2 = pygame.sprite.Group()
#Listas Indexadas monedas Nivel 2
Coins21 = pygame.sprite.Group()
Coins22 = pygame.sprite.Group()
Coins23 = pygame.sprite.Group()
Coins24 = pygame.sprite.Group()
Coins25 = pygame.sprite.Group()
Coins26 = pygame.sprite.Group()
Coins27 = pygame.sprite.Group()
Coins28 = pygame.sprite.Group()
Coins29 = pygame.sprite.Group()
Coins210 = pygame.sprite.Group()
#Listas Indexadas Manzanas Nivel 2
Apples21 = pygame.sprite.Group()
Apples22 = pygame.sprite.Group()
Apples23 = pygame.sprite.Group()
Apples24 = pygame.sprite.Group()
Apples25 = pygame.sprite.Group()
Apples26 = pygame.sprite.Group()
Apples27 = pygame.sprite.Group()
Apples28 = pygame.sprite.Group()
Apples29 = pygame.sprite.Group()
Apples210 = pygame.sprite.Group()
#Listas Indexadas Diamantes Nivel 2
Diamonds21 = pygame.sprite.Group()
Diamonds22 = pygame.sprite.Group()
Diamonds23 = pygame.sprite.Group()
Diamonds24 = pygame.sprite.Group()
Diamonds25 = pygame.sprite.Group()
Diamonds26 = pygame.sprite.Group()
Diamonds27 = pygame.sprite.Group()
Diamonds28 = pygame.sprite.Group()
Diamonds29 = pygame.sprite.Group()
Diamonds210 = pygame.sprite.Group()
#Listas Indexadas Posiones Nivel 2
"""
Potions21 = pygame.sprite.Group()
Potions22 = pygame.sprite.Group()
Potions23 = pygame.sprite.Group()
Potions24 = pygame.sprite.Group()
Potions25 = pygame.sprite.Group()
Potions26 = pygame.sprite.Group()
Potions27 = pygame.sprite.Group()
Potions28 = pygame.sprite.Group()
Potions29 = pygame.sprite.Group()
Potions210 = pygame.sprite.Group()
"""

#Room information A
#Lectura de archivo json
FileName='Assets\Levels\Level2\Level2a.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

WallsA = MapInfo['layers'][8]['objects']
LaddersPosA = MapInfo['layers'][9]['objects']
LavaPosA = MapInfo['layers'][10]['objects']
CoinsPos2A = MapInfo['layers'][11]['objects']
WaterPosA = MapInfo['layers'][12]['objects']
DiamondPos2A = MapInfo['layers'][13]['objects']
ApplesPos2A = MapInfo['layers'][14]['objects']
DoorPos2A = MapInfo['layers'][15]['objects']
Enemys2A = MapInfo['layers'][16]['objects']

#Creacion de las monedas
for i in range(len(CoinsPos2A)):
    Temporal = co.Coin((CoinsPos2A[i]['x'],CoinsPos2A[i]['y']))
    CoinsList2.add(Temporal)
    Coins21.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPos2A)):
    Temporal = ap.Apple((ApplesPos2A[i]['x'],ApplesPos2A[i]['y']))
    ApplesList2.add(Temporal)
    Apples21.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondPos2A)):
    Temporal = d.Diamond((DiamondPos2A[i]['x'],DiamondPos2A[i]['y']))
    DiamondsList2.add(Temporal)
    Diamonds21.add(Temporal)
#Creacion de las posiones

#Room information B
#Lectura de archivo json
FileName='Assets\Levels\Level2\Level2b.json'
with open(FileName) as information:
    MapInfo = json.load(information)
information.close()

WallsB = MapInfo['layers'][8]['objects']
LaddersPosB = MapInfo['layers'][9]['objects']
DeepWaterPosB = MapInfo['layers'][10]['objects']
WaterPosB = MapInfo['layers'][11]['objects']
Platforms2B = MapInfo['layers'][12]['objects']
VMovingPlatformS2B = MapInfo['layers'][13]['objects']
CoinsPos2B = MapInfo['layers'][14]['objects']
DiamondPos2B = MapInfo['layers'][15]['objects']
PotionsPos2B = MapInfo['layers'][16]['objects']
ApplesPos2B = MapInfo['layers'][17]['objects']
Enemys2B = MapInfo['layers'][18]['objects']

#Creacion de las monedas
for i in range(len(CoinsPos2B)):
    Temporal = co.Coin((CoinsPos2B[i]['x'],CoinsPos2B[i]['y']))
    CoinsList2.add(Temporal)
    Coins22.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPos2B)):
    Temporal = ap.Apple((ApplesPos2B[i]['x'],ApplesPos2B[i]['y']))
    ApplesList2.add(Temporal)
    Apples22.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondPos2B)):
    Temporal = d.Diamond((DiamondPos2B[i]['x'],DiamondPos2B[i]['y']))
    DiamondsList2.add(Temporal)
    Diamonds22.add(Temporal)
#Creacion de las posiones
"""for i in range(len(PotionsPos2B)):
    Temporal = p.Potion((PotionsPos2B[i]['x'],PotionsPos2B[i]['y']))
    PotionsList2.add(Temporal)
    Potions22.add(Temporal)"""

#Room information C
#Lectura de archivo json
FileName ='Assets\Levels\Level2\Level2c.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

WallsC = MapInfo['layers'][7]['objects']
SpikesPos2C = MapInfo['layers'][8]['objects']
LavaPosC = MapInfo['layers'][9]['objects']
PotionsPos2C = MapInfo['layers'][10]['objects']
VMovingPlatformE2C = MapInfo['layers'][11]['objects']
Platforms2C = MapInfo['layers'][12]['objects']
CoinsPos2C = MapInfo['layers'][13]['objects']
ApplesPos2C = MapInfo['layers'][14]['objects']
DiamondPos2C = MapInfo['layers'][15]['objects']
Enemys2C = MapInfo['layers'][16]['objects']

#Creacion de las monedas
for i in range(len(CoinsPos2C)):
    Temporal = co.Coin((CoinsPos2C[i]['x'],CoinsPos2C[i]['y']))
    CoinsList2.add(Temporal)
    Coins23.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPos2C)):
    Temporal = ap.Apple((ApplesPos2C[i]['x'],ApplesPos2C[i]['y']))
    ApplesList2.add(Temporal)
    Apples23.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondPos2C)):
    Temporal = d.Diamond((DiamondPos2C[i]['x'],DiamondPos2C[i]['y']))
    DiamondsList2.add(Temporal)
    Diamonds23.add(Temporal)
#Creacion de las posiones
"""for i in range(len(PotionsPos2C)):
    Temporal = p.Potion((PotionsPos2C[i]['x'],PotionsPos2C[i]['y']))
    PotionsList2.add(Temporal)
    Potions23.add(Temporal)"""

#Room Information D
#Lectura de archivo json
FileName='Assets\Levels\Level2\Level2d.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

WallsD = MapInfo['layers'][6]['objects']
LavaPosD = MapInfo['layers'][7]['objects']
LaddersPosD = MapInfo['layers'][8]['objects']
CoinsPos2D = MapInfo['layers'][10]['objects']
ApplesPos2D = MapInfo['layers'][11]['objects']
DiamondPos2D = MapInfo['layers'][12]['objects']
PotionsPos2D = MapInfo['layers'][13]['objects']
Enemys2D = MapInfo['layers'][14]['objects']

#Creacion de las monedas
for i in range(len(CoinsPos2D)):
    Temporal = co.Coin((CoinsPos2D[i]['x'],CoinsPos2D[i]['y']))
    CoinsList2.add(Temporal)
    Coins24.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPos2D)):
    Temporal = ap.Apple((ApplesPos2D[i]['x'],ApplesPos2D[i]['y']))
    ApplesList2.add(Temporal)
    Apples24.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondPos2D)):
    Temporal = d.Diamond((DiamondPos2D[i]['x'],DiamondPos2D[i]['y']))
    DiamondsList2.add(Temporal)
    Diamonds24.add(Temporal)
#Creacion de las posiones
"""for i in range(len(PotionsPos2D)):
    Temporal = p.Potion((PotionsPos2D[i]['x'],PotionsPos2D[i]['y']))
    PotionsList2.add(Temporal)
    Potions24.add(Temporal)"""

#Room Information E
#Lectura de archivo json
FileName='Assets\Levels\Level2\Level2e.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

WallsE = MapInfo['layers'][8]['objects']
WaterPosE = MapInfo['layers'][9]['objects']
LaddersPosE = MapInfo['layers'][10]['objects']
CoinsPos2E = MapInfo['layers'][11]['objects']
ApplesPos2E = MapInfo['layers'][12]['objects']
DiamondPos2E = MapInfo['layers'][13]['objects']
PotionsPos2E = MapInfo['layers'][14]['objects']
Enemys2E = MapInfo['layers'][15]['objects']

#Creacion de las monedas
for i in range(len(CoinsPos2E)):
    Temporal = co.Coin((CoinsPos2E[i]['x'],CoinsPos2E[i]['y']))
    CoinsList2.add(Temporal)
    Coins25.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPos2E)):
    Temporal = ap.Apple((ApplesPos2E[i]['x'],ApplesPos2E[i]['y']))
    ApplesList2.add(Temporal)
    Apples25.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondPos2E)):
    Temporal = d.Diamond((DiamondPos2E[i]['x'],DiamondPos2E[i]['y']))
    DiamondsList2.add(Temporal)
    Diamonds25.add(Temporal)
#Creacion de las posiones
"""for i in range(len(PotionsPos2E)):
    Temporal = p.Potion((PotionsPos2E[i]['x'],PotionsPos2E[i]['y']))
    PotionsList2.add(Temporal)
    Potions25.add(Temporal)"""

#Room information F
#Lectura de archivo json
FileName='Assets\Levels\Level2\Level2f.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

WallsF = MapInfo['layers'][6]['objects']
LavaPosF = MapInfo['layers'][7]['objects']
CoinsPos2F = MapInfo['layers'][8]['objects']
ApplesPos2F = MapInfo['layers'][9]['objects']
PotionsPos2F = MapInfo['layers'][10]['objects']
DiamondPos2F = MapInfo['layers'][11]['objects']
LaddersPosF = MapInfo['layers'][12]['objects']
Enemys2F = MapInfo['layers'][13]['objects']

#Creacion de las monedas
for i in range(len(CoinsPos2F)):
    Temporal = co.Coin((CoinsPos2F[i]['x'],CoinsPos2F[i]['y']))
    CoinsList2.add(Temporal)
    Coins26.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPos2F)):
    Temporal = ap.Apple((ApplesPos2F[i]['x'],ApplesPos2F[i]['y']))
    ApplesList2.add(Temporal)
    Apples26.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondPos2F)):
    Temporal = d.Diamond((DiamondPos2F[i]['x'],DiamondPos2F[i]['y']))
    DiamondsList2.add(Temporal)
    Diamonds26.add(Temporal)
"""#Creacion de las posiones
for i in range(len(PotionsPos2F)):
    Temporal = p.Potion((PotionsPos2F[i]['x'],PotionsPos2F[i]['y']))
    PotionsList2.add(Temporal)
    Potions26.add(Temporal)"""

#Room information G
#Lectura de archivo json
FileName ='Assets\Levels\Level2\Level2g.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

WallsG = MapInfo['layers'][7]['objects']
LavaPosG = MapInfo['layers'][8]['objects']
CoinsPos2G = MapInfo['layers'][9]['objects']
WaterPosG = MapInfo['layers'][10]['objects']
ApplesPos2G = MapInfo['layers'][11]['objects']
DiamondPos2G = MapInfo['layers'][12]['objects']
DoorPos2G = MapInfo['layers'][13]['objects']
Enemys2G = MapInfo['layers'][14]['objects']

#Creacion de las monedas
for i in range(len(CoinsPos2G)):
    Temporal = co.Coin((CoinsPos2G[i]['x'],CoinsPos2G[i]['y']))
    CoinsList2.add(Temporal)
    Coins27.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPos2G)):
    Temporal = ap.Apple((ApplesPos2G[i]['x'],ApplesPos2G[i]['y']))
    ApplesList2.add(Temporal)
    Apples27.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondPos2G)):
    Temporal = d.Diamond((DiamondPos2G[i]['x'],DiamondPos2G[i]['y']))
    DiamondsList2.add(Temporal)
    Diamonds27.add(Temporal)
#Creacion de las posiones

#Room Information H
#Lectura de archivo json
FileName='Assets\Levels\Level2\Level2h.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()


WallsH = MapInfo['layers'][7]['objects']
DoorPos2H = MapInfo['layers'][8]['objects']
ApplesPos2H = MapInfo['layers'][9]['objects']
PotionsPos2H = MapInfo['layers'][10]['objects']
DiamondPos2H = MapInfo['layers'][11]['objects']
CoinsPos2H = MapInfo['layers'][12]['objects']
LavaPos2H =  MapInfo['layers'][13]['objects']
Enemys2H = MapInfo['layers'][14]['objects']

#Creacion de las monedas
for i in range(len(CoinsPos2H)):
    Temporal = co.Coin((CoinsPos2H[i]['x'],CoinsPos2H[i]['y']))
    CoinsList2.add(Temporal)
    Coins28.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPos2H)):
    Temporal = ap.Apple((ApplesPos2H[i]['x'],ApplesPos2H[i]['y']))
    ApplesList2.add(Temporal)
    Apples28.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondPos2H)):
    Temporal = d.Diamond((DiamondPos2H[i]['x'],DiamondPos2H[i]['y']))
    DiamondsList2.add(Temporal)
    Diamonds28.add(Temporal)
#Creacion de las posiones
"""for i in range(len(PotionsPos2H)):
    Temporal = p.Potion((PotionsPos2H[i]['x'],PotionsPos2H[i]['y']))
    PotionsList2.add(Temporal)
    Potions28.add(Temporal)"""

#Room Information I
#Lectura de archivo json
FileName ='Assets\Levels\Level2\Level2i.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

WallsI = MapInfo['layers'][5]['objects']
WaterPosI = MapInfo['layers'][6]['objects']
CoinsPos2I = MapInfo['layers'][7]['objects']
DiamondPos2I = MapInfo['layers'][8]['objects']
ApplesPos2I = MapInfo['layers'][9]['objects']
PotionsPos2I = MapInfo['layers'][10]['objects']

#Creacion de las monedas
for i in range(len(CoinsPos2I)):
    Temporal = co.Coin((CoinsPos2I[i]['x'],CoinsPos2I[i]['y']))
    CoinsList2.add(Temporal)
    Coins29.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPos2I)):
    Temporal = ap.Apple((ApplesPos2I[i]['x'],ApplesPos2I[i]['y']))
    ApplesList2.add(Temporal)
    Apples29.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondPos2I)):
    Temporal = d.Diamond((DiamondPos2I[i]['x'],DiamondPos2I[i]['y']))
    DiamondsList2.add(Temporal)
    Diamonds29.add(Temporal)
#Creacion de las posiones
"""for i in range(len(PotionsPos2I)):
    Temporal = p.Potion((PotionsPos2I[i]['x'],PotionsPos2I[i]['y']))
    PotionsList2.add(Temporal)
    Potions29.add(Temporal)"""

#Room Information J
#Lectura de archivo json
FileName ='Assets\Levels\Level2\Level2j.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

WallsJ = MapInfo['layers'][6]['objects']
LavaPosJ = MapInfo['layers'][7]['objects']
WaterPosJ = MapInfo['layers'][8]['objects']
ApplesPos2J = MapInfo['layers'][9]['objects']
DiamondPos2J = MapInfo['layers'][10]['objects']
PotionsPos2J = MapInfo['layers'][11]['objects']
CoinsPos2J = MapInfo['layers'][12]['objects']
Limit2J = MapInfo['layers'][13]['objects']
Door2j = MapInfo['layers'][14]['objects']
Jefe2 = Ciclope.Ciclope([MapInfo['layers'][15]['objects'][0]['x'],MapInfo['layers'][15]['objects'][0]['y']])
LasersJefe2 = pygame.sprite.Group()
RocaJefe2 = pygame.sprite.Group()

#Creacion de las monedas
for i in range(len(CoinsPos2J)):
    Temporal = co.Coin((CoinsPos2J[i]['x'],CoinsPos2J[i]['y']))
    CoinsList2.add(Temporal)
    Coins210.add(Temporal)
#Creacion de las manzanas
for i in range(len(ApplesPos2J)):
    Temporal = ap.Apple((ApplesPos2J[i]['x'],ApplesPos2J[i]['y']))
    ApplesList2.add(Temporal)
    Apples210.add(Temporal)
#Creacion de los diamantes
for i in range(len(DiamondPos2J)):
    Temporal = d.Diamond((DiamondPos2J[i]['x'],DiamondPos2J[i]['y']))
    DiamondsList2.add(Temporal)
    Diamonds210.add(Temporal)
"""#Creacion de las posiones
for i in range(len(PotionsPos2J)):
    Temporal = p.Potion((PotionsPos2J[i]['x'],PotionsPos2J[i]['y']))
    PotionsList2.add(Temporal)
    Potions210.add(Temporal)"""

#---------------------------------------------------- Nivel 3 (Boss)--------------------------------------------------------
Coins31 = pygame.sprite.Group()
Apples31 = pygame.sprite.Group()
Potions31 = pygame.sprite.Group()
Diamonds31 = pygame.sprite.Group()

Coins32 = pygame.sprite.Group()
Apples32 = pygame.sprite.Group()
Potions32 = pygame.sprite.Group()
Diamonds32 = pygame.sprite.Group()

#Room A Final Boss
FileName ='Assets\Levels\Final Boss\FinalBossA.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

WallsFinalBoss = MapInfo['layers'][8]['objects']
LaddersFinalBoss = MapInfo['layers'][9]['objects']
DoorFinalBoss = MapInfo['layers'][10]['objects']

#Room B Final Boss
FileName ='Assets\Levels\Final Boss\FinalBossB.json'
with open(FileName) as information:
    MapInfo=json.load(information)
information.close()

WallsFinalBossB = MapInfo['layers'][6]['objects']
LavaPosFB = MapInfo['layers'][7]['objects']
ApplesPosFB = MapInfo['layers'][8]['objects']
PotionsPosFB = MapInfo['layers'][9]['objects']
CannonsPosFB = MapInfo['layers'][10]['objects']
LaddersPosFB = MapInfo['layers'][11]['objects']
WaterPosFB =  MapInfo['layers'][12]['objects']
DoorPosFB =  MapInfo['layers'][13]['objects']
EnemysPosFB =  MapInfo['layers'][14]['objects']
BossFinal = KingPig.King([MapInfo['layers'][15]['objects'][0]['x'],MapInfo['layers'][15]['objects'][0]['y']])


#Creacion de las manzanas
for i in range(len(ApplesPosFB)):
    Temporal = ap.Apple((ApplesPosFB[i]['x'],ApplesPosFB[i]['y']))
    Apples32.add(Temporal)
"""#Creacion de las posiones
for i in range(len(PotionsPosFB)):
    Temporal = p.Potion((PotionsPosFB[i]['x'],PotionsPosFB[i]['y']))
    Potions32.add(Temporal)"""


#-------------------------------------------------------Sprites-----------------------------#
SmallPlatform = pygame.image.load('Assets\Images\Sprites\Platforms\SmallPlatform.png')
LongPlatform = pygame.image.load('Assets\Images\Sprites\Platforms\LongPlatform.png')
CannonIDLEL = pygame.image.load('Assets\Images\Sprites\Cannon\Idle.png')
CannonIDLER = pygame.transform.flip(pygame.image.load('Assets\Images\Sprites\Cannon\Idle.png'),True,False)
Bomber = pygame.image.load('Assets\Images\Sprites\Pork\Bomber.png')