#Import of libraries
import pygame
import sys

pygame.init()

Screen = pygame.display.set_mode([1080,720])
Container = pygame.Rect(100,50,900,620)
caja = pygame.transform.scale(pygame.image.load('Idle.png'),[32,32])
#------------------------------
def Main_Menu():
    #Definition of variables-----------------
    #music upload
    end = False
    while not end:
        #event managment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        pygame.draw.rect(Screen,[255,255,255],Container)
        Screen.blit(caja,[120,70])
        pygame.display.flip()
    
    
Main_Menu()
