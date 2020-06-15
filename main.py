from CRUD.Level2 import Room10 as R1
from CRUD.Tutorial import TutorialRoom as TR
from CRUD.Level2 import Room1 as R2
from CRUD import RoomLoader as RL
from CRUD.FinalBoss import Room2 as R3
from Classes import Vida as V

from CRUD import Constants
import pygame
from Classes import Player as P
#Creacion Jugador
j = P.Jugador([0,0])
Players = pygame.sprite.Group()
Players.add(j)
Constants.LifeManager = V.Vida([0,0],j)
#currentLevel = R3.StartRoom(j,Players,150,200)
#currentLevel = R2.StartRoom(j,Players,100, 0)
#currentLevel = R1.StartRoom(j,Players,300, 280)
currentLevel = R1.StartRoom(j,Players,100,100)
while(True):
    nextLevel = RL.LoadRoom(j,currentLevel[0],currentLevel[1],currentLevel[2],currentLevel[3],currentLevel[4],currentLevel[5],currentLevel[6],currentLevel[7],currentLevel[8],currentLevel[9],currentLevel[10],currentLevel[11],currentLevel[12],currentLevel[13],currentLevel[14],currentLevel[15],currentLevel[16],currentLevel[17],currentLevel[18])
    if nextLevel != None:
        currentLevel = nextLevel.copy()
        nextLevel = None