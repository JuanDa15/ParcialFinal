import pygame
from CRUD import Functions

class Door(pygame.sprite.Sprite):
    def __init__(self, position,width,height,destiny):
        pygame.sprite.Sprite.__init__(self)
        self.recortes = (pygame.image.load('Assets\Images\Sprites\Door\Idle.png'),pygame.image.load('Assets\Images\Sprites\Door\Closiong (46x56).png'),pygame.image.load('Assets\Images\Sprites\Door\Opening (46x56).png')) 
        self.image = self.recortes[0].subsurface(0,0,46,56)
        #self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.destiny = destiny

        #animacion
        self.frame = 0
        self.accion = 0
        self.espera = 2
        self.animacion = ((0,0,46,56), (0,0,46,56,46,0,46,56,92,0,46,56), (0,0,46,56,46,0,46,56,92,0,46,56,138,0,46,56,184,0,46,56))
    
    def enterDoor(self, pos_destiny):
        while (self.frame < len(self.animacion[self.accion])-1):
            self.image = self.recortes[self.accion].subsurface(self.animacion[self.accion][self.frame],self.animacion[self.accion][self.frame+1],self.animacion[self.accion][self.frame+2],self.animacion[self.accion][self.frame+3])
            if self.espera == 0: 
                self.frame += 4
                self.espera = 2
            else:
                self.espera -= 1
        print("Entrar")
        return ('R' + self.destiny + '.StartRoom(Player,Players,'+ str(pos_destiny[0]) +','+ str(pos_destiny[1]) +')')

    defExitRoom(self, pos_destiny):
        while (self.frame < len(self.animacion[self.accion])-1):
            self.image = self.recortes[self.accion].subsurface(self.animacion[self.accion][self.frame],self.animacion[self.accion][self.frame+1],self.animacion[self.accion][self.frame+2],self.animacion[self.accion][self.frame+3])
            if self.espera == 0: 
                self.frame += 4
                self.espera = 2
            else:
                self.espera -= 1
        print("Entrar")
        return ('R' + self.destiny + '.StartRoom(Player,Players,'+ str(pos_destiny[0]) +','+ str(pos_destiny[1]) +')')
        
