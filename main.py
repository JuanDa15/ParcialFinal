
from CRUD.Level1 import Room1 as R1
from CRUD import RoomLoader as RL

import pygame
from Classes import Player as P
#Creacion Jugador
j = P.Jugador([0,0])
Players = pygame.sprite.Group()
Players.add(j)
currentLevel = R1.StartRoom(j,Players,100, 280)
while(True):
    nextLevel = RL.LoadRoom(j,currentLevel[0],currentLevel[1],currentLevel[2],currentLevel[3],currentLevel[4],currentLevel[5],currentLevel[6],currentLevel[7],currentLevel[8],currentLevel[9],currentLevel[10],currentLevel[11],currentLevel[12],currentLevel[13],currentLevel[14],currentLevel[15],currentLevel[16],currentLevel[17],currentLevel[18])
    if nextLevel != None:
        currentLevel = nextLevel.copy()
        nextLevel = None