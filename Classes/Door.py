import pygame
from CRUD import Functions

class Door(pygame.sprite.Sprite):
    def __init__(self, position,width,height,destiny):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.destiny = destiny
    
    def enterDoor(self, pos_destiny):
        #Aqui se anima la momda esta
        print("Entrar")
        return ('R' + self.destiny + '.StartRoom(Player,Players,'+ str(pos_destiny[0]) +','+ str(pos_destiny[1]) +')')
        
