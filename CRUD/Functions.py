import pygame

def draw_text(text, font, color,surface, x, y):
    TittleText = font.render(text,True,color)
    TTrect = TittleText.get_rect()
    print (TTrect)
    TTrect.topleft = (x,y)
    surface.blit(TittleText,TTrect)

def SelectColor(ColorName):
    if ColorName == 'Yellow':
        return [255,255,0]
    if ColorName == 'Blue':
        return [0,0,255]
    if ColorName == 'Red':
        return [255,0,0]
    if ColorName == 'Green':
        return [0,255,0]
    if ColorName == 'White':
        return [255,255,255]
    if ColorName == 'Purple':
        return [255,0,255]
    if ColorName == 'Light Blue':
        return [0,255,255]
    if ColorName == 'Gray1':
        return [100,100,100]
    if ColorName == 'Gray2':
        return [200,200,200]
    if ColorName == 'Gray3':
        return [50,50,50]
    if ColorName == 'Black':
        return [0,0,0]
    if ColorName == 'Orange':
        return [227,113,36]

def MakeImage(X,Y,surface,image):
    ButtonRect = image.get_rect()
    ButtonRect.topleft = (X,Y)
    surface.blit(image,ButtonRect)

def getSpecifications():
    #Specifications [width,height]
    Specifications = [800,608]
    return Specifications     