import pygame

class pincho(pygame.sprite.Sprite):
    def __init__(self, pos, anchura, altura):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([anchura, altura])
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.Daño = 10
