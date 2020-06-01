import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill((255,255,255))
        self.rect=self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.velx=0
        self.vely=0
        self.Bloques = None

    def PositionPlayer(self):
        x = self.rect.x
        y = self.rect.y
        coord = [x,y]
        return coord

    def update(self):
        #colision x--------------------------------------------------------------------------------------
        self.rect.x+=self.velx
        listaColision=pygame.sprite.spritecollide(self,self.Bloques,False)
        for b in listaColision:
            if ((self.rect.right >= b.rect.left) and (self.rect.right <= b.rect.right)):
                self.velx=0
                self.rect.right = b.rect.left
            elif ((self.rect.left <= b.rect.right) and (self.rect.left >= b.rect.left)):
                self.velx=0
                self.rect.left = b.rect.right

        #colision y--------------------------------------------------------------------------------------
        self.rect.y+=self.vely
        listaColision=pygame.sprite.spritecollide(self,self.Bloques,False)
        for b in listaColision:
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    self.vely = 0
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                    self.vely = 0
 


class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos, anchura, altura):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([anchura, altura])
        self.image.fill((100,100,100))
        self.rect=self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.VelocidadFondo = 0