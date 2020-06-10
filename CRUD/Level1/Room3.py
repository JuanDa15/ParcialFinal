#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Player as P
from Classes import Block
from Classes import VerticalMovingPlatform as VMP
from CRUD.Level1 import Room2
from pygame.locals import *

def Room3(Position):
    MovementLimit = 795