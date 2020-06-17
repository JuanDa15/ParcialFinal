import pygame
clock = pygame.time.Clock()
class Background(pygame.sprite.Sprite):
    def __init__(self,position,Imagen):
        super(Background, self).__init__()
        self.m = Imagen
        self.con = 0
        self.image = self.m[self.con]
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
            
    def update(self):
        self.image = self.m[self.con]
        if self.con >= 190:
            self.con = 0
        else:
            self.con = self.con + 1
        clock.tick(9)