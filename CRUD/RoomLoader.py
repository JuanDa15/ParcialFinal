
#Import of libraries
import json
import pygame
import sys
#Packages Import
from CRUD import Functions
from CRUD import Constants
from CRUD import ShowHistory
from Classes import Vida
from Classes import HorizontalMovingPlatform as HMP
from Classes import VerticalMovingPlatform as VMP
from Classes import Player as P
from Classes import Block
from Classes import Bomber
from Classes import Bomb
from Classes import Roca
from Classes import Laser
from Classes import pork
from Classes import Brujas
from Classes import Cobra
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
def LoadRoom(Player,Players,Blocks,Enemies,Puas,Cannons,Ladders,Lava,Water,Doors,Moving_platforms,Levers,Instakill,Clock,mapa,level_type,prevRoom,nextRoom,currentLevel,currentRoom):
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
                Player.DireccionHammer = 1
                Player.velx = Player.speeeeeeeeeeed
                if Player.EnLava == True:
                    Player.velx = Player.speeeeeeeeeeed - 1
                if Player.EnAgua == True:
                    Player.velx = Player.speeeeeeeeeeed - 0.5
                Player.frame = 0
                Player.direccion = True
            if event.key == pygame.K_LEFT:
                Player.DireccionHammer = 0
                Player.frame = 0
                Player.velx = -Player.speeeeeeeeeeed
                if Player.EnLava == True:
                    Player.velx = -Player.speeeeeeeeeeed + 1
                if Player.EnAgua == True:
                    Player.velx = -Player.speeeeeeeeeeed + 0.5
                Player.frame = 0
                Player.direccion = False
            if event.key == pygame.K_UP:
                if Constants.inLadder:
                    Constants.Subiendo = True
            if event.key == pygame.K_SPACE:
                Player.frame = 0
                Player.accion = 3
                Constants.SpaceKey = True
                if Player.EnLava == True:
                    Player.vely = -3
                if Player.EnAgua == True:
                    Player.vely = -4
                Player.EnAire = True
            if event.key == pygame.K_e:
                Constants.Interact = True
            if event.key == pygame.K_q:
                Constants.AppleConsumed = True
            if event.key == pygame.K_w:
                Constants.Hit = True
                Player.accion = 4
                Player.frame = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Player.velx = 0
            if event.key == pygame.K_LEFT:
                Player.velx = 0
            if event.key == pygame.K_UP:
                Constants.Subiendo = False
            if event.key == pygame.K_SPACE:
                Constants.SpaceKey = False
            if event.key == pygame.K_e:
                Constants.Interact = False
            if event.key == pygame.K_q:
                Constants.AppleConsumed = False
            if event.key == pygame.K_w:
                Constants.Hit = False
    if Player.EnAire == False:
        if Player.Charge <= 1.3 and Constants.SpaceKey:
            Player.vely = -7 - Player.Charge
            Player.Charge += 0.1
        else:
            Player.Charge = 1.0
            Player.EnAire = True

    if currentLevel + currentRoom == '32':
        collide = pygame.sprite.spritecollide(Constants.BossFinal, Players, False)
        if collide:
            Constants.WinGame = True

    if Constants.AppleConsumed and Player.Apples > 0 and Player.vida < 100:
        if Constants.AppleTime == 0:
            Player.vida += 20
            Player.Apples -= 1
            Constants.AppleTime = 250
            Constants.AppleConsumed = False
    if Constants.AppleTime > 0:
        Constants.AppleTime -= 1

    Constants.CountCobras = 0
    if Enemies != None:
        for b in Enemies:
            if isinstance(b,Cobra.Cobra):
                Constants.CountCobras += 1

    #Colisiones Jugador con Puas
    if Puas != None:
        for Player in Players:
            listaColisionPuas=pygame.sprite.spritecollide(Player,Puas,False)
            for b in listaColisionPuas:
                if ((Player.rect.right >= b.rect.left) and (Player.rect.right <= b.rect.right)):
                    Constants.LifeManager.hitPlayer(10)
                elif ((Player.rect.left <= b.rect.right) and (Player.rect.left >= b.rect.left)):
                    Constants.LifeManager.hitPlayer(10)
                elif ((Player.rect.bottom >= b.rect.top) and (Player.rect.bottom <= b.rect.bottom)):
                    Constants.LifeManager.hitPlayer(10)
                elif ((Player.rect.top <= b.rect.bottom) and (Player.rect.top >= b.rect.top)):
                    Constants.LifeManager.hitPlayer(10)

    #Cañones
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
    if Enemies != None:
        for Player in Players:
            listaColisionEnemy = pygame.sprite.spritecollide(Player,Enemies,False)
            for b in listaColisionEnemy:
                if isinstance(b,pork.cerdo) or isinstance(b,Brujas.Escoba) or isinstance(b,Cobra.Cobra):
                    #El cerdito ataca (b)
                    if b.accion != 1:
                        Constants.LifeManager.hitPlayer(10)
        for Hammer in Player.HammerGroup:
            listaColisionHammer = pygame.sprite.spritecollide(Hammer,Enemies,False)
            for b in listaColisionHammer:
                if Constants.Hit:
                    b.accion = 1
                    b.frame = 0
                    b.velx = 0
        for b in Enemies:
            if isinstance(b,Brujas.Estatica):
                b.timer -= 1
                if b.timer == 0:
                    if Constants.MaxCobras >= Constants.CountCobras:
                        cobraBruja = Cobra.Cobra([b.rect.x,b.rect.y],Player)
                        cobraBruja.Bloques = Blocks
                        Enemies.add(cobraBruja)
                    b.timer = 150
            if b.accion == 1:
                b.muerto = True
                if b.Muerte > 0:
                    b.Muerte -= 1
                else:
                    Enemies.remove(b)
        for Enemy in Enemies:
            if isinstance(Enemy,Bomber.Bomber):
                Enemy.player = Player
                if Enemy.timer == 1:
                    TempBomb = Bomb.bomb([(Enemy.rect.x - 5),Enemy.rect.y],Enemy.direccion)
                    TempBomb.Bloques = Blocks
                    eval('Constants.Bombs'+currentLevel+currentRoom+'.add(TempBomb)')
        if currentLevel == '1' or currentLevel == '0' or currentLevel+currentRoom == '32':
            for TempBomb in eval('Constants.Bombs'+currentLevel+currentRoom+''):
                ListaColision = pygame.sprite.spritecollide(TempBomb, Players, False)
                for b in ListaColision:
                    eval('Constants.Bombs'+currentLevel+currentRoom+'.remove(TempBomb)')
                    Constants.LifeManager.hitPlayer(10)
                if TempBomb.time == 0:
                    eval('Constants.Bombs'+currentLevel+currentRoom+'.remove(TempBomb)')

    #Water
    if Water != None:
        for Player in Players:
            CollisionAgua = pygame.sprite.spritecollide(Player, Water, False)
            if CollisionAgua:
                Player.EnAgua = True
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
    if Player.EnAgua:
        Player.TQuemadura = 0
        Player.gravity = 0.1
    else:
        Player.gravity = 0.5

    if Instakill != None:
        for Player in Players:
            CollisionInstakill = pygame.sprite.spritecollide(Player, Instakill, False)
            if CollisionInstakill:
                Constants.LifeManager.instakill()
                return eval('R' + currentLevel + '1.StartRoom(Player,Players,32,(260-(191*(1%int(currentLevel)))))')

    #Lava
    if Lava != None:
        if Enemies != None:
            for Enemy in Enemies:
                if isinstance(Enemy,Cobra.Cobra):
                    CollisionLava = pygame.sprite.spritecollide(Enemy, Lava, False)
                    if CollisionLava or Enemy.rect.y > Constants.Height + 10:
                        Constants.CountCobras -= 1
                        Enemies.remove(Enemy)
        for Player in Players:
            CollisionLava = pygame.sprite.spritecollide(Player, Lava, False)
            if CollisionLava:
                Player.EnLava = True
            else:
                Player.EnLava = False

        if Player.EnLava == True:
            if Player.InmunidadFuego == False:
                Constants.LifeManager.hitPlayer(10)
                Player.TQuemadura = 250
    if Player.EnLava:
        Player.gravity = 0.1
    else:
        Player.gravity = 0.5

    if Player.TQuemadura > 0:
        if Player.TQuemadura in [250,200,150,100,50]:
            Constants.LifeManager.hitPlayer(10)
        Player.TQuemadura -= 1

    #BOSS 1
    if currentLevel + currentRoom == '110':
        for Player in Players:
            for Hammer in Player.HammerGroup:
                listaColisionHammer = pygame.sprite.spritecollide(Constants.Jefe1,Player.HammerGroup,False)
                for b in listaColisionHammer:
                    if Constants.Hit:
                        if Constants.Jefe1.invisibility == 0:
                            Constants.Jefe1.vida -= 1
                            if Constants.Jefe1.vida == 0:
                                Player.Coins += Constants.Jefe1.premio
                                Player.Diamonds += int(Constants.Jefe1.premio/10)
                                Constants.Jefe1.velx = 0
                                Constants.Jefe1.Dead = True
                                Constants.Jefe1.frame = 0
                                Constants.Jefe1.accion = 1
                            else:
                                Constants.Jefe1.invisibility = 100
                                Constants.Jefe1.Angry = True

    #BOSS 2
    if currentLevel + currentRoom == '210':
        Constants.MaxCobras = 5
        for Player in Players:
            for Hammer in Player.HammerGroup:
                listaColisionHammer = pygame.sprite.spritecollide(Constants.Jefe2,Player.HammerGroup,False)
                for b in listaColisionHammer:
                    if Constants.Hit:
                        if Constants.Jefe2.invisibility == 0:
                            Constants.Jefe2.vida -= 1
                            if Constants.Jefe2.vida == 0:
                                Player.Coins += Constants.Jefe2.premio
                                Player.Diamonds += int(Constants.Jefe2.premio/10)
                                Constants.Jefe2.Dead = True
                                Constants.Jefe2.frame = 0
                                Constants.Jefe2.accion = 1
                            else:
                                Constants.Jefe2.invisibility = 100
                                Constants.Jefe2.Angry = True
        if not Constants.Jefe2.Dead:
            for b in Constants.LasersJefe2:
                if b.time == 0:
                    Constants.LasersJefe2.remove(b)
            if Constants.Jefe2.nextAttack == 0 and Constants.Jefe2.attackFinished:
                for i in range(5):
                    for i in range(5):
                        Constants.Jefe2.frame = 0
                        Constants.Jefe2.accion = 3
                        TempLaser = Laser.Laser([Constants.Jefe2.rect.x,Constants.Jefe2.rect.y],Players,i)
                        Constants.LasersJefe2.add(TempLaser)
                        TempCobra = Cobra.Cobra([Constants.Jefe2.rect.x,Constants.Jefe2.rect.y],Player)
                        TempCobra.Bloques = Blocks
                        Enemies.add(TempCobra)
                    Constants.LasersJefe2.update()
            if Constants.Jefe2.nextAttack == 1 and Constants.Jefe2.attackFinished:
                    Constants.Jefe2.frame = 0
                    Constants.Jefe2.accion = 4
                    TempRock = Roca.Roca([Constants.Jefe2.rect.x,Constants.Jefe2.rect.y],Players,Constants.Jefe2.direccion)
                    Constants.RocaJefe2.add(TempRock)
                    TempCobra = Cobra.Cobra([Constants.Jefe2.rect.x,Constants.Jefe2.rect.y],Player)
                    TempCobra.Bloques = Blocks
                    Enemies.add(TempCobra)



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
                    Constants.LifeManager.hitPlayer(10)
                elif ((Player.rect.left <= b.rect.right) and (Player.rect.left >= b.rect.left)):
                    Constants.LifeManager.hitPlayer(10)
                elif ((Player.rect.bottom >= b.rect.top) and (Player.rect.bottom <= b.rect.bottom)):
                    Constants.LifeManager.hitPlayer(10)
                elif ((Player.rect.top <= b.rect.bottom) and (Player.rect.top >= b.rect.top)):
                    Constants.LifeManager.hitPlayer(10)
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
        Constants.Total_Monedas += 1

    #Recoger Manzanas
    ListaManzanas = eval('pygame.sprite.spritecollide(Player, Constants.Apples'+currentLevel+currentRoom+',True)')
    for i in ListaManzanas:
        Constants.ApplesList.remove(i)
    if ListaManzanas:
        Player.Apples = Player.Apples + 1
        Constants.Total_Manzanas += 1
    #Recoger Diamantes
    ListaDiamantes = eval('pygame.sprite.spritecollide(Player, Constants.Diamonds'+currentLevel+currentRoom+',True)')
    for i in ListaDiamantes:
        Constants.DiamondsList.remove(i)
    if ListaDiamantes:
        Player.Diamonds = Player.Diamonds + 1
        Constants.Total_Diamantes += 1

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
                    if currentLevel + currentRoom == '110':
                        ShowHistory.show_history(2)
                    destiny_doors = eval('R'+b.destiny+'.StartRoom(Player,Players,0,0)')[8]
                    for c in destiny_doors:
                        Constants.Interact = False
                        return eval(b.enterDoor(c.position))

    if level_type == 0:
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                Constants.LifeManager.instakill()
                return eval('R' + currentLevel + '1.StartRoom(Player,Players,32,(260-(191*(1%int(currentLevel)))))')
            #Cambia de Nivel
            if Player.rect.left > Constants.limitemovimientoX:
                if nextRoom != None:
                    if (currentLevel + nextRoom) == '32':
                        return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,10,Player.rect.y - 2)')
                    else:
                        return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,-6,Player.rect.y - 2)')
                        
    if level_type == 1:
        #Muerte por salir de pantalla
        for Player in Players:
            if Player.rect.y >= Constants.Height + 10:
                Constants.LifeManager.instakill()
                return eval('R' + currentLevel + '1.StartRoom(Player,Players,32,(260-(191*(1%int(currentLevel)))))')
        #Cambia de Nivel
            if Player.rect.left > Constants.limitemovimientoX:
                if (currentLevel + nextRoom) == '210':
                    return eval('R' + currentLevel + nextRoom + '.StartRoom(Player,Players,10,Player.rect.y - 2)')
                else:
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
                return eval('R' + currentLevel + '1.StartRoom(Player,Players,32,(260-(191*(1%int(currentLevel)))))')
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
                return eval('R' + currentLevel + '1.StartRoom(Player,Players,32,(260-(191*(1%int(currentLevel)))))')
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
                    return R19.StartRoom(Player,Players,351, 272)
                elif (currentLevel + currentRoom) == '210':
                    Constants.LifeManager.instakill()
                    return R29.StartRoom(Player,Players,384, 400)
                elif (currentLevel + currentRoom) == '32':
                    Constants.LifeManager.instakill()
                    return R31.StartRoom(Player,Players,120, 280)

                    #return R11.StartRoom(Player,Players,100, 280)

    #Tienda
    for Player in Players:
        if (currentLevel + currentRoom) == '19':
            Constants.Shop1.rect.x = 200
            Constants.Shop1.rect.y = 240
            ListaTienda = pygame.sprite.spritecollide(Player,Constants.Shop1.ShopItems,False)
            for b in ListaTienda:
                if Constants.Interact:
                    if b.type == 0:
                        if Player.Coins >= Constants.Shop1.precioPotiLava:
                            Constants.Shop1.potiLava = False
                            Player.Coins -= Constants.Shop1.precioPotiLava
                            Player.InmunidadFuego = True
                    if b.type == 1:
                        if Player.Coins >= Constants.Shop1.precioPotiVel:
                            Constants.Shop1.potiVel = False
                            Player.Coins -= Constants.Shop1.precioPotiVel
                            Player.speeeeeeeeeeed = 5
                    if b.type == 2:
                        if Player.Coins >= Constants.Shop1.precioGapple:
                            Constants.Shop1.Gapple = False
                            Player.Coins -= Constants.Shop1.precioGapple
                            Player.Apples += 10
        if (currentLevel + currentRoom) == '29':
            Constants.Shop1.rect.x = 270
            Constants.Shop1.rect.y = 368
            ListaTienda = pygame.sprite.spritecollide(Player,Constants.Shop1.ShopItems,False)
            for b in ListaTienda:
                if Constants.Interact:
                    if b.type == 0:
                        if Player.Coins >= Constants.Shop1.precioPotiLava:
                            Constants.Shop1.potiLava = False
                            Player.Coins -= Constants.Shop1.precioPotiLava
                            Player.InmunidadFuego = True
                    if b.type == 1:
                        if Player.Coins >= Constants.Shop1.precioPotiVel:
                            Constants.Shop1.potiVel = False
                            Player.Coins -= Constants.Shop1.precioPotiVel
                            Player.speeeeeeeeeeed = 5
                    if b.type == 2:
                        if Player.Coins >= Constants.Shop1.precioGapple:
                            Constants.Shop1.Gapple = False
                            Player.Coins -= Constants.Shop1.precioGapple
                            Player.Apples += 10
        if (currentLevel + currentRoom) == '31':
            Constants.Shop1.rect.x = 123
            Constants.Shop1.rect.y = 305
            ListaTienda = pygame.sprite.spritecollide(Player,Constants.Shop1.ShopItems,False)
            for b in ListaTienda:
                if Constants.Interact:
                    if b.type == 0:
                        if Player.Coins >= Constants.Shop1.precioPotiLava:
                            Constants.Shop1.potiLava = False
                            Player.Coins -= Constants.Shop1.precioPotiLava
                            Player.InmunidadFuego = True
                    if b.type == 1:
                        if Player.Coins >= Constants.Shop1.precioPotiVel:
                            Constants.Shop1.potiVel = False
                            Player.Coins -= Constants.Shop1.precioPotiVel
                            Player.speeeeeeeeeeed = 5
                    if b.type == 2:
                        if Player.Coins >= Constants.Shop1.precioGapple:
                            Constants.Shop1.Gapple = False
                            Player.Coins -= Constants.Shop1.precioGapple
                            Player.Apples += 10



    Constants.Screen.fill([0,0,0])
    Players.update()
    Blocks.update()
    if Lava != None:
        Lava.update()
    if Enemies != None:
        if currentLevel == '1' or currentLevel == '0' or currentLevel+currentRoom == '32':
            eval('Constants.Bombs'+currentLevel+currentRoom+'.update()')
        Enemies.update()
    if Cannons != None:
        Cannons.update()
        eval('Constants.CannonBalls'+currentLevel+currentRoom+'.update()')
    if Moving_platforms != None:
        Moving_platforms.update()
    Constants.Screen.blit(mapa,[0,0])
    #Pos mapa
    if Doors != None:
        Doors.draw(Constants.Screen)
    if ((currentLevel + currentRoom) == '32'):
        Constants.BossFinal.Bloques = Blocks
        Constants.BossFinal.update()
        Constants.Screen.blit(Constants.BossFinal.Animacion.image,[Constants.BossFinal.rect.x,Constants.BossFinal.rect.y])
    if ((currentLevel + currentRoom) == '210'):
        Constants.Jefe2.Bloques = Blocks
        Constants.Jefe2.player = Player
        Constants.Jefe2.update()
        Constants.LasersJefe2.update()
        Constants.RocaJefe2.update()
        Constants.LasersJefe2.draw(Constants.Screen)
        Constants.RocaJefe2.draw(Constants.Screen)
        Constants.Screen.blit(Constants.Jefe2.Animacion.image,[Constants.Jefe2.rect.x,Constants.Jefe2.rect.y])
    if ((currentLevel + currentRoom) == '110'):
        Constants.Jefe1.Bloques = Blocks
        Constants.Jefe1.player = Player
        Constants.Jefe1.update()
        Constants.Screen.blit(Constants.Jefe1.Animacion.image,[Constants.Jefe1.rect.x,Constants.Jefe1.rect.y])
    if ((currentLevel + currentRoom) == '19') or ((currentLevel + currentRoom) == '29') or ((currentLevel + currentRoom) == '31'):
        Constants.Shop1.Tendero.draw(Constants.Screen)
        Constants.Shop1.ShopItems.draw(Constants.Screen)
        Constants.Shop1.update()
    Constants.Screen.blit(Player.Animacion.image,[Player.Animacion.rect.x,Player.Animacion.rect.y])
    if Lava != None:
        pass

    eval('Constants.Coins'+currentLevel+currentRoom+'.draw(Constants.Screen)')
    eval('Constants.Apples'+currentLevel+currentRoom+'.draw(Constants.Screen)')
    eval('Constants.Diamonds'+currentLevel+currentRoom+'.draw(Constants.Screen)')
    if Enemies != None:
        if currentLevel == '1' or currentLevel == '0' or currentLevel+currentRoom == '32':
            eval('Constants.Bombs'+currentLevel+currentRoom+'.draw(Constants.Screen)')
        Enemies.draw(Constants.Screen)
    if Cannons != None:
        Cannons.draw(Constants.Screen)
        eval('Constants.CannonBalls'+currentLevel+currentRoom+'.draw(Constants.Screen)')
    if Moving_platforms != None:
        Moving_platforms.draw(Constants.Screen)
    Constants.LifeManager.update()

    #Mostrar vidas y salud
    Constants.Screen.blit(Constants.LifeManager.image, [20,20])
    Constants.Screen.blit(Constants.LifeManager.vida, [15,80])
    if (currentLevel + currentRoom == '14') or (currentLevel + currentRoom == '17') or (currentLevel + currentRoom == '21') or (currentLevel + currentRoom == '25'):
        Constants.ScoreManager.rect.x = 670
        Constants.ScoreManager.rect.y = 490
    elif (currentLevel + currentRoom == '23') or (currentLevel + currentRoom == '24') or (currentLevel + currentRoom == '26'):
        Constants.ScoreManager.rect.x = 20
        Constants.ScoreManager.rect.y = 490
    else:
        Constants.ScoreManager.rect.x = 670
        Constants.ScoreManager.rect.y = 10
    Constants.ScoreManager.Scores.draw(Constants.Screen)
    Constants.ScoreManager.update()
    if Player.TQuemadura > 0:
        Constants.Screen.blit(Constants.LifeManager.quemadura.image, [100,80])
    if Player.invisibility > 0:
        Constants.Screen.blit(Constants.LifeManager.shield.image, [130,82])

    pygame.display.flip()
    Clock.tick(30)
