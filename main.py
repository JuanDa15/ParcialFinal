from CRUD.Level1 import Room1 as R1
from CRUD import Constants

from Classes import Player as P
#Creacion Jugador
print (len(Constants.CoinsList))

j = P.Jugador([0,0])
R1.StartRoom1(j,100, 280)
