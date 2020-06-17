#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Block
from Classes import Lava
from Classes import pork
from Classes import Bomber
from Classes import Door as Do
from Classes import Ladder as La
from Classes import Cannon as ca
from Classes import Water
from Classes import Spikes
from Classes import VerticalMovingPlatform as VMP
from pygame.locals import *

def StartRoom(Player, Players ,PositionX ,PositionY):

    pygame.mixer.init()
    pygame.mixer.music.load("Assets\Sounds\Tutorial.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    mapa = Constants.MapaTutorial

    #Definicion de Grupos
    Blocks = pygame.sprite.Group()
    Cannons = pygame.sprite.Group()
    Platforms = pygame.sprite.Group()
    Puas = pygame.sprite.Group()
    Ladders = pygame.sprite.Group()
    Doors = pygame.sprite.Group()
    LavaG = pygame.sprite.Group()
    WaterG = pygame.sprite.Group()

    #Definicion Posicion Inicial
    for Player in Players:
        Player.rect.x = PositionX
        Player.rect.y = PositionY

    #Water
    for i in range(len(Constants.WaterTutorialPos)):
        Temporal = Water.Water([(Constants.WaterTutorialPos[i]['x']),(Constants.WaterTutorialPos[i]['y'])], Constants.WaterTutorialPos[i]['width'],Constants.WaterTutorialPos[i]['height'])
        WaterG.add(Temporal)

    #Creacion de spykes
    for i in range(len(Constants.SpikesPosTutos)):
        Temporal = Spikes.spikes([(Constants.SpikesPosTutos[i]['x']),(Constants.SpikesPosTutos[i]['y'])],Constants.SpikesPosTutos[i]['width'],Constants.SpikesPosTutos[i]['height'])
        Puas.add(Temporal)

    #Creacion de las paredes
    for i in range(len(Constants.WallsTutorial)):
        Temporal = Block.Bloque([(Constants.WallsTutorial[i]['x']),(Constants.WallsTutorial[i]['y'])],Constants.WallsTutorial[i]['width'],Constants.WallsTutorial[i]['height'])
        Blocks.add(Temporal)

    #Creacion Lava
    for i in range(len(Constants.LavaTutorial)):
        Temporal = Lava.Lava([(Constants.LavaTutorial[i]['x']),(Constants.LavaTutorial[i]['y'])], Constants.LavaTutorial[i]['width'], Constants.LavaTutorial[i]['height'])
        LavaG.add(Temporal)

    #Creacion de cañones
    for i in range(len(Constants.CannonsPosTuto)):
        if Constants.CannonsPosTuto[i]['name'] == 'False':
            Temporal = Block.Bloque([(Constants.CannonsPosTuto[i]['x']),(Constants.CannonsPosTuto[i]['y'])],Constants.CannonsPosTuto[i]['width'],Constants.CannonsPosTuto[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosTuto[i]['x']),(Constants.CannonsPosTuto[i]['y'])],Constants.CannonIDLEL,1)
            Blocks.add(Temporal)
            Cannons.add(Temp)
        else:
            Temporal = Block.Bloque([(Constants.CannonsPosTuto[i]['x']),(Constants.CannonsPosTuto[i]['y'])],Constants.CannonsPosTuto[i]['width'],Constants.CannonsPosTuto[i]['height'])
            Temp = ca.cannon([(Constants.CannonsPosTuto[i]['x']),(Constants.CannonsPosTuto[i]['y'])],Constants.CannonIDLER,0)
            Blocks.add(Temporal)
            Cannons.add(Temp)
    
    for i in range(len(Constants.LaddersPosTuto)):
        Temporal = La.Ladder([(Constants.LaddersPosTuto[i]['x']),(Constants.LaddersPosTuto[i]['y'])],Constants.LaddersPosTuto[i]['width'],Constants.LaddersPosTuto[i]['height'])
        Ladders.add(Temporal)
    
    Distance = (Constants.VMovingPlatformET[0]['y'])-(Constants.VMovingPlatformST[0]['y'])
    for i in range(len(Constants.VMovingPlatformST)):
        if Constants.VMovingPlatformST[i]['width'] > 33:
            pass
        else:
            Temporal = VMP.PlataformaMovil([(Constants.VMovingPlatformST[i]['x']),(Constants.VMovingPlatformST[i]['y'])],Distance,Constants.SmallPlatform,1)
            Platforms.add(Temporal)
    
    for i in range(len(Constants.DoorPosTuto)):
        Temporal = Do.Door([(Constants.DoorPosTuto[i]['x']),(Constants.DoorPosTuto[i]['y'])],Constants.DoorPosTuto[i]['width'],Constants.DoorPosTuto[i]['height'],'11')
        Doors.add(Temporal)

    #Asignacion de lista de coliciones a las entidades
    for Player in Players:
        Player.Bloques = Blocks
        Player.PlataformasY = Platforms
    
    EnemysG = pygame.sprite.Group()
    for i in range(len(Constants.EnemysTuto)):
        if Constants.EnemysTuto[i]['name'] == 'CerdoC':
            Temp = pork.cerdo([(Constants.EnemysTuto[i]['x']),(Constants.EnemysTuto[i]['y'])-12],(Constants.EnemysTuto[i]['properties'][0]['value']))
            EnemysG.add(Temp)
        elif Constants.EnemysTuto[i]['name'] == 'CerdoB':
            Temp = Bomber.Bomber([(Constants.EnemysTuto[i]['x']),(Constants.EnemysTuto[i]['y'])],Constants.Bomber,1)
            EnemysG.add(Temp)
    
    for e in EnemysG:
        e.Bloques = Blocks
    
        #(Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, instakill, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
    return [Players, Blocks, EnemysG, Puas, Cannons, Ladders, LavaG, WaterG, Doors, Platforms, None, None, Constants.Clock, mapa, 0, None,None,'0','1']