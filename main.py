"""from CRUD import Game as G
1
G.StarGame()
"""
from CRUD.Level1 import Room1 as R1
from CRUD.Level1 import Room2 as R2
from CRUD.Level1 import Room3 as R3
from CRUD.Level1 import Room4 as R4
from CRUD.Level1 import Room6 as R6





from Classes import Player as P
#Creacion Jugador
j = P.Jugador([0,0])
R6.StartGame(j,5, 380)