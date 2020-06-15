from CRUD.Level1 import Room4 as R1
from CRUD.Tutorial import TutorialRoom as TR
from CRUD.Level1 import Room1 as R2
from CRUD import RoomLoader as RL
from CRUD.FinalBoss import Room2 as R3
from CRUD.Menus import MainMenu as MM
from CRUD.Menus import LostScreen as LS
from CRUD.Menus import VictoryScreen as VS
from CRUD import Constants
from Classes import Vida as V
from Classes import Score as Sc


from CRUD import Constants
import importlib
import pygame
from Classes import Player as P

def load_game():
    #Creacion Jugador
    j = P.Jugador([0,0])
    Players = pygame.sprite.Group()
    Players.add(j)
    Constants.LifeManager = V.Vida([0,0],j)
    Constants.ScoreManager = Sc.Score([670,10],j)
    #currentLevel = R3.StartRoom(j,Players,150,200)
    #currentLevel = R2.StartRoom(j,Players,400, 300)
    #currentLevel = R1.StartRoom(j,Players,300, 280)
    currentLevel = R1.StartRoom(j,Players,100,100)
    Constants.ClockStart = pygame.time.get_ticks()
    return [j,Players,currentLevel]

MM.Main_Menu()
currentGame = load_game()
j = currentGame[0]
Players = currentGame[1]
currentLevel = currentGame[2]


while(True):
    nextLevel = RL.LoadRoom(j,currentLevel[0],currentLevel[1],currentLevel[2],currentLevel[3],currentLevel[4],currentLevel[5],currentLevel[6],currentLevel[7],currentLevel[8],currentLevel[9],currentLevel[10],currentLevel[11],currentLevel[12],currentLevel[13],currentLevel[14],currentLevel[15],currentLevel[16],currentLevel[17],currentLevel[18])
    if nextLevel != None:
        currentLevel = nextLevel.copy()
        nextLevel = None
    if Constants.LifeManager.vidas == 0:
        response = LS.lostMenu(Constants.Screen)
        if response == 1:  
            importlib.reload(Constants)
            MM.Main_Menu()
            currentGame = load_game()
            j = currentGame[0]
            Players = currentGame[1]
            currentLevel = currentGame[2]
        elif response == 2: 
            importlib.reload(Constants)
            currentGame = load_game()
            j = currentGame[0]
            Players = currentGame[1]
            currentLevel = R1.StartRoom(j,Players,400, 300)
#VS.Victory_Menu(Constants.Screen)
