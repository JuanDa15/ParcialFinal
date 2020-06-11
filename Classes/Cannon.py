import pygame
from CRUD import Functions

class cannon(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
<<<<<<< Updated upstream
        self.image = pygame.image.load('Assets\Sprites\Cannon\Idle.png')
=======
        self.image =  pygame.transform.scale(pygame.image.load('Assets\Sprites\Cannon\Idle.png'),(30,20))
>>>>>>> Stashed changes
        #self.image.fill(Functions.SelectColor('Blue'))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 0
        self.vely = 0
        self.Disparo = 30
        self.Direccion = False
        if self.Direccion == False:
<<<<<<< Updated upstream
            self.image =  pygame.image.load('Assets\Sprites\Cannon\Idle.png')
=======
            self.image =  pygame.transform.scale(pygame.image.load('Assets\Sprites\Cannon\Idle.png'),(30,20))
>>>>>>> Stashed changes
        else:
            self.image =  pygame.transform.flip(pygame.image.load('Assets\Sprites\Cannon\Idle.png'),True,False)
        
    def update(self):
        pass