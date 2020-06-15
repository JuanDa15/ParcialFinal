
#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from Classes import Vida
from Classes import HorizontalMovingPlatform as HMP
from Classes import VerticalMovingPlatform as VMP
from Classes import Player as P
from Classes import Block
from Classes import pork
from Classes import Score as Sc
from Classes import Cannon as ca
from Classes import Lava
from Classes import CannonBall as cb
from CRUD.Tutorial import TutorialRoom as R0
from Classes import VerticalMovingPlatform as VMP
from Classes import HorizontalMovingPlatform as HMP
from CRUD.Level1 import Room1 as R11
from CRUD.Level1 import Room2 as R12
from CRUD.Level1 import Room3 as R13
from CRUD.Level1 import Room4 as R14
from CRUD.Level1 import Room5 as R15
from CRUD.Level1 import Room6 as R16
from CRUD.Level1 import Room7 as R17
from CRUD.Level1 import Room8 as R18
from CRUD.Level1 import Room9 as R19
from CRUD.Level1 import Room10 as R110
from CRUD.Level2 import Room1 as R21
from CRUD.Level2 import Room2 as R22
from CRUD.Level2 import Room3 as R23
from CRUD.Level2 import Room4 as R24
from CRUD.Level2 import Room5 as R25
from CRUD.Level2 import Room6 as R26
from CRUD.Level2 import Room7 as R27
from CRUD.Level2 import Room8 as R28
from CRUD.Level2 import Room9 as R29
from CRUD.Level2 import Room10 as R210
from CRUD.FinalBoss import Room1 as R31
from CRUD.FinalBoss import Room2 as R32
from pygame.locals import *

#(Jugador, Jugadores, Blocks, Enemigos, Puas, Cannons, Ladders, Lava, Water, Doors, Moving_platforms, Levers, Clock, Mapa, level_type, prevRoom, nextRoom, currentLevel, currentRoom)
def LoadRoom(Player,Players,Blocks,Cerdos,Puas,Cannons,Ladders,Lava,Water,Doors,Moving_platforms,Levers,Instakill,Clock,mapa,level_type,prevRoom,nextRoom,currentLevel,currentRoom):
    #Movimiento Jugador
    # --type
    # 0 - StartLevel ->  [=
    # 1 - normal corridor -> = + =
    # 2 - Corridor + downfall ->  = + ╗
    # 3 - downfall corridor -> ║ + ║
    # 4 - downfall + corridor -> ╗ + =
    # 5 - Corridor + Climb
    # 6 - Climb corridor
    # 7 - Climb + Corridor
    #event managment
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Player.velx = 3
                if Player.EnLava == True:
                    Player.velx = 2
                if Player.EnAgua == True:
                    Player.velx = 2.5
            if event.key == pygame.K_LEFT:
                Player.velx = -3
                if Player.EnLava == True:
                    Player.velx = -2
                if Player.EnAgua == True:
                    Player.velx = -2.5
            if event.key == pygame.K_UP:
                if Constants.inLadder:
                    Constants.Subiendo = True
            if event.key == pygame.K_SPACE:
                Constants.Space = True
                if Player.EnLava == True:
                    Player.vely = -3
                if Player.EnAgua == True:
                    Player.vely = -4
            if event.key == pygame.K_e:
                Constants.Interact = True
            if event.key == pygame.K_q:
                Constants.AppleConsumed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Player.velx = 0
            if event.key == pygame.K_LEFT:
                Player.velx = 0
            if event.key == pygame.K_UP:
                Constants.Subiendo = False
            if event.key == pygame.K_SPACE:
                Constants.Space = False
            if event.key == pygame.K_e:
                Constants.Interact = False
            if event.key == pygame.K_q:
                Constants.AppleConsumed = False

    if Player.EnAire == False:
        if Player.Charge <= 1.3 and Constants.Space:
            Player.vely = -7 - Player.Charge
            Player.Charge += 0.1
        else:
            Player.Charge = 1.0
            Player.EnAire = True

    if Constants.AppleConsumed and Player.Apples > 0 and Player.vida < 100:
        if Constants.AppleTime == 0:
            Player.vida += 20
            Player.Apples -= 1
            Constants.AppleTime = 250
            Constants.AppleConsumed = False
    if Constants.AppleTime > 0:
        Constants.AppleTime -= 1


    #Colisiones Jugador con Puas
    if Puas != None:
        for Player in Players:
            listaColisionPuas=pygame.sprite.spritecollide(Player,Puas,False)
            for b in listaColisionPuas:
                if ((Player.rect.right >= b.rect.left) and (Player.rect.right <= b.rect.right)):
                    print("chuzao pai")
                    Constants.LifeManager.hitPlayer(10)
                elif ((Player.rect.left <= b.rect.right) and (Player.rect.left >= b.rect.left)):
                    print("chuzao pai")
                    Constants.LifeManager.hitPlayer(10)
                elif ((Player.rect.bottom >= b.rect.top) and (Player.rect.bottom <= b.rect.bottom)):
                    print("chuzao pai")
                    Constants.LifeManager.hitPlayer(10)
                elif ((Player.rect.top <= b.rect.bottom) and (Player.rect.top >= b.rect.top)):
                    print("chuzao pai")
                    Constants.LifeManager.hitPlayer(10)

    if Cannons != None:
        for Cannon in Cannons:
            if Cannon.direccion == 1:
                if Cannon.timer < 0:
                    position = Cannon.returnPos()
                    CannonBall = cb.cannonball([(Cannon.rect.x - 12),Cannon.rect.y],-5)
                    CannonBall.bloques = Blocks
                    eval('Constants.CannonBalls'+currentLevel+currentRoom+'.add(CannonBall)')
                    Cannon.timer = 60
            elif Cannon.direccion == 0:
                if Cannon.timer < 0:
                    position = Cannon.returnPos()
                    CannonBall = cb.cannonball([(Cannon.rect.x + 25),Cannon.rect.y],5)
                    CannonBall.bloques = Blocks
                    eval('Constants.CannonBalls'+currentLevel+currentRoom+'.add(CannonBall)')
                    Cannon.timer = 60

        for ball in eval('Constants.CannonBalls'+currentLevel+currentRoom+''):
            ListaColision = pygame.sprite.spritecollide(ball, Blocks, False)
            for b in ListaColision:
                if ((ball.rect.right >= b.rect.left) and (ball.rect.right <= b.rect.right)):
                    eval('Constants.CannonBalls'+currentLevel+currentRoom+'.remove(ball)')
                elif ((ball.rect.left <= b.rect.right) and (ball.rect.left >= b.rect.left)):
                    eval('Constants.CannonBalls'+currentLevel+currentRoom+'.remove(ball)')

            if ball.getDistance() == 50:
                eval('Constants.CannonBalls'+currentLevel+currentRoom+'.remove(ball)')
    #Enemigos
    if Cerdos != None:
        for Player in Players:
            listaColisionCerdos=pygame.sprite.spritecollide(Player,Cerdos,False)
            for b in listaColisionCerdos:
                if ((Player.rect.right >= b.rect.left) and (Player.rect.right <= b.rect.right)):
                    print("Encerdado pai")
                    Constants.LifeManager.hitPlayer(20)
                elif ((Player.rect.left <= b.rect.right) and (Player.rect.left >= b.rect.left)):
                    print("Encerdado pai")
                    Constants.LifeManager.hitPlayer(20)
                elif ((Player.rect.bottom >= b.rect.top) and (Player.rect.bottom <= b.rect.bottom)):
                    print("Encerdado pai")
                    Constants.LifeManager.hitPlayer(20)
                elif ((Player.rect.top <= b.rect.bottom) and (Player.rect.top >= b.rect.top)):
                    print("Encerdado pai")
                    Constants.LifeManager.hitPlayer(20)
    #Water
    if Water != None:
        for Player in Players:
            CollisionAgua = pygame.sprite.spritecollide(Player, Water, False)
            if CollisionAgua:
                Player.EnAgua = True
                print('Mojado Pai')
            else:
                Player.EnAgua = False
                Player.respiracion = 0
            
            for b in CollisionAgua:
                if Player.rect.top <= b.rect.top:
                    Player.respiracion = 0

                if Player.rect.top  >= b.rect.top:
                    if Player.EnAgua == True:
                        Player.UpdateRespiration()
                        if Player.getRespiracion() == 35:
                            Constants.LifeManager.hitPlayer(10)
                            Player.respiracion = 0
        
    #Lava
    if Lava != None:
        for Player in Players:
            CollisionLava = pygame.sprite.spritecollide(Player, Lava, False)
            if CollisionLava:
                Player.EnLava = True
                print('Quemado Pai')  
            else:
                Player.EnLava = False
            
        if Player.EnLava == True:
            if Player.InmunidadFuego == False:
                Constants.LifeManager.hitPlayer(15)

    #PLATAFORMAS MOVILES
    if Moving_platforms != None:
        for i in Moving_platforms:
            currentPlatform = pygame.sprite.Group()
            currentPlatform.add(i)
            #PLATAFORMAS MOVIMIENTO VERTICAL
            if isinstance(i,VMP.PlataformaMovil):
                # PLATAFORMAS Y - Y
                listaColisionPla = pygame.sprite.spritecollide(Player, currentPlatform, False)
                for b in listaColisionPla:
                    if ((Player.rect.bottom >= b.rect.top) and (Player.rect.bottom <= b.rect.bottom)):
                        Player.rect.bottom = b.rect.top
                        Player.EnAire = False
                        Player.vely = b.vely
                    elif ((Player.rect.top <= b.rect.bottom) and (Player.rect.top >= b.rect.top)):
                        Player.vely = 0
                        Player.rect.top = b.rect.bottom
                    #PLATAFORMAS Y - X
                    if currentPlatform != None:
                        listaColisionPla = pygame.sprite.spritecollide(Player, currentPlatform, False)
                        for b in listaColisionPla:
                            if ((Player.rect.right >= b.rect.left) and (Player.rect.right <= b.rect.right)):
                                Player.rect.right = b.rect.left
                            elif ((Player.rect.left <= b.rect.right) and (Player.rect.left >= b.rect.left)):
                                Player.rect.left = b.rect.right
            #PLATAFORMAS MOVIMIENTO HORIZONTAL
            if isinstance(i,HMP.PlataformaMovil):
                #PLATAFORMAS X - Y
                listaColisionPla = pygame.sprite.spritecollide(Player, currentPlatform, False)
                for b in listaColisionPla:
                    if currentPlatform != None:
                        listaColisionPla = pygame.sprite.spritecollide(Player, currentPlatform, False)
                        for b in listaColisionPla:
                            if ((Player.rect.bottom >= b.rect.top) and (Player.rect.bottom <= b.rect.bottom)):
                                Player.rect.bottom = b.rect.top
                                Player.EnAire = False
                                Player.vely = b.vely
                                Player.velx = b.velx
                            elif ((Player.rect.top <= b.rect.bottom) and (Player.rect.top >= b.rect.top)):
                                Player.vely = 0
                                Player.rect.top = b.rect.bottom
                    #PLATAFORMAS X - X
                    if currentPlatform != None:
                        listaColisionPla = pygame.sprite.spritecollide(Player, currentPlatform, False)
                        for b in listaColisionPla:
                            if ((Player.rect.right >= b.rect.left) and (Player.rect.right <= b.rect.right)):
                                Player.rect.right = b.rect.left
                            elif ((Player.rect.left <= b.rect.right) and (Player.rect.left >= b.rect.left)):
                                Player.rect.left = b.rect.right
    for Player in Players:
        if Cannons != None:
            ListaBolasCañon = pygame.sprite.spritecollide(Player, eval('Constants.CannonBalls'+currentLevel+currentRoom+''),True)
            for b in ListaBolasCañon:
                if ((Player.rect.right >= b.rect.left) and (Player.rect.right <= b.rect.right)):
                    print("balazo pai")
                    Constants.LifeManager.hitPlayer(20)
                elif ((Player.rect.left <= b.rect.right) and (Player.rect.left >= b.rect.left)):
                    print("balazo pai")
                    Constants.LifeManager.hitPlayer(20)
                elif ((Player.rect.bottom >= b.rect.top) and (Player.rect.bottom <= b.rect.bottom)):
                    print("balazo pai")
                    Constants.LifeManager.hitPlayer(20)
                elif ((Player.rect.top <= b.rect.bottom) and (Player.rect.top >= b.rect.top)):
                    print("balazo pai")
                    Constants.LifeManager.hitPlayer(20)
    #Escaleras
    for Player in Players:
        if Ladders != None:
            ListaLadders = pygame.sprite.spritecollide(Player,Ladders,False)
            if ListaLadders:
                Constants.inLadder = True
            else:
                Constants.inLadder = False

    if Constants.Subiendo and Constants.inLadder:
        Player.vely = -1.4

    #Recoger Monedas
    ListaMonedas = eval('pygame.sprite.spritecollide(Player, Constants.Coins'+currentLevel+currentRoom+',True)')
    for i in ListaMonedas:
        Constants.CoinsList.remove(i)
    if ListaMonedas:
        Player.Coins = Player.Coins + 1

    #Recoger Manzanas
    ListaManzanas = eval('pygame.sprite.spritecollide(Player, Constants.Apples'+currentLevel+currentRoom+',True)')
    for i in ListaManzanas:
        Constants.ApplesList.remove(i)
    if ListaManzanas:
        Player.Apples = Player.Apples + 1
    #Recoger Diamantes
    ListaDiamantes = eval('pygame.sprite.spritecollide(Player, Constants.Diamonds'+currentLevel+currentRoom+',True)')
    for i in ListaDiamantes:
        Constants.DiamondsList.remove(i)
    if ListaDiamantes:
        Player.Diamonds = Player.Diamonds + 1

    #Puertas
    if Doors != None:
        if len(Doors) == 2:
            ListaDoors = pygame.sprite.spritecollide(Player,Doors,False)
            for b in ListaDoors:
                if Constants.Interact:
                    for c in Doors:
                        if b != c:
                            nextDoor = c
                    Constants.Interact = False
                    return eval(b.enterDoor(nextDoor.position))
        if len(Doors) == 1:
            ListaDoors = pygame.sprite.spritecollide(Player,Doors,False)
            for b in ListaDoors:
                if Constants.Interact:
                    destiny_doors = eval('R'+b.destiny+'.StartRoom(Player,Players,0,0)')[8]
                    for c in destiny_doors:
                        Constants.Interact = False
                        return eval(b.enterDoor(c.position))

    if level_type == 0:
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                Constants.LifeManager.instakill()
                return R11.StartRoom(Player,Players,100, 280)
            #Cambia de Nivel
            if Player.rect.left > Constants.limitemovimientoX:
                if nextRoom != None:
                    return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,-6,Player.rect.y - 2)')
    if level_type == 1:
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                Constants.LifeManager.instakill()
                return R11.StartRoom(Player,Players,100, 280)
        #Cambia de Nivel
            if Player.rect.left > Constants.limitemovimientoX:
                return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,-6,Player.rect.y - 2)')
            if Player.rect.right < 5:
                return eval('R' + currentLevel + prevRoom + '.StartRoom(Player,Players,779,Player.rect.y - 2)')

    if level_type == 2:
        #Cambia de Nivel
            if Player.rect.top > Constants.limitemovimientoY:
                return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,Player.rect.x,-6)')
            if Player.rect.right < 5:
                return eval('R' + currentLevel + prevRoom + '.StartRoom(Player,Players,779,Player.rect.y - 2)')

    if level_type == 3:
        #Cambia de Nivel
            if Player.rect.top > Constants.limitemovimientoY:
                return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,Player.rect.x,-6)')
            if Player.rect.bottom < 5:
                return eval('R' + currentLevel + prevRoom + '.StartRoom(Player,Players,Player.rect.x,594)')

    if level_type == 4:
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                Constants.LifeManager.instakill()
                return R11.StartRoom(Player,Players,100, 280)
        #Cambia de Nivel
            if Player.rect.left > Constants.limitemovimientoX:
                return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,-6,Player.rect.y - 2)')
            if Player.rect.bottom < 5:
                return eval('R' + currentLevel + prevRoom + '.StartRoom(Player,Players,Player.rect.x,594)')

    if level_type == 5:
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                Constants.LifeManager.instakill()
                return R11.StartRoom(Player,Players,100, 280)
        #Cambia de Nivel
            if Player.rect.bottom < 5:
                return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,Player.rect.x,594)')
            if Player.rect.right < 5:
                return eval('R' + currentLevel + prevRoom + '.StartRoom(Player,Players,779,Player.rect.y - 2)')

    if level_type == 6:
        #Cambia de Nivel
            if Player.rect.bottom < 5:
                return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,Player.rect.x,594)')
            if Player.rect.top > Constants.limitemovimientoY:
                return eval('R' + currentLevel + prevRoom + '.StartRoom(Player,Players,Player.rect.x,-6)')

    if level_type == 7:
        #Cambia de Nivel
            if Player.rect.left > Constants.limitemovimientoX:
                if (currentLevel + nextRoom) == '110':
                    return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,10,Player.rect.y - 2)')
                else:
                    return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,-6,Player.rect.y - 2)')
            if Player.rect.top > Constants.limitemovimientoY:
                return eval('R' + currentLevel + prevRoom + '.StartRoom(Player,Players,Player.rect.x,-6)')

    if level_type == 8:
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                if (currentLevel + currentRoom) == '110':
                    Constants.LifeManager.instakill()
                    return R19.StartRoom(Player,Players,100, 280)
                else:
                    Constants.LifeManager.instakill()
                    return R11.StartRoom(Player,Players,100, 280)

    Constants.Screen.fill([0,0,0])
    Players.update()
    print (Player.quemadura)
    print (Player.TQuemadura)
    Blocks.update()
    if Lava != None:
        Lava.update()
    if Cerdos != None:
        Cerdos.update()
    if Cannons != None:
        Cannons.update()
        eval('Constants.CannonBalls'+currentLevel+currentRoom+'.update()')
    if Moving_platforms != None:
        Moving_platforms.update()
    Constants.Screen.blit(mapa,[0,0])
    Players.draw(Constants.Screen)
    if Lava != None:
        pass
    if Cerdos != None:
        Cerdos.draw(Constants.Screen)
    eval('Constants.Coins'+currentLevel+currentRoom+'.draw(Constants.Screen)')
    eval('Constants.Apples'+currentLevel+currentRoom+'.draw(Constants.Screen)')
    eval('Constants.Diamonds'+currentLevel+currentRoom+'.draw(Constants.Screen)')
    if Cannons != None:
        Cannons.draw(Constants.Screen)
        eval('Constants.CannonBalls'+currentLevel+currentRoom+'.draw(Constants.Screen)')
    if Moving_platforms != None:
        Moving_platforms.draw(Constants.Screen)
    Constants.LifeManager.update()
    if Doors != None:
        Doors.draw(Constants.Screen)

    Constants.Screen.blit(Constants.LifeManager.image, [20,20])
    Constants.Screen.blit(Constants.LifeManager.vida, [15,80])
    if (currentLevel + currentRoom == '14') or (currentLevel + currentRoom == '17'):
        Constants.ScoreManager.rect.y = 500
    else:
        Constants.ScoreManager.rect.y = 20
    Constants.ScoreManager.Scores.draw(Constants.Screen)
    Constants.ScoreManager.update()

    pygame.display.flip()
    Clock.tick(30)
