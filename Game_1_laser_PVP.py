"""
Game_1_laser_PVP

Description:
"""
#setup
import tsk
import pygame
pygame.init()
w=pygame.display.set_mode([1000,1000])
#variables
game=True
P1_wins=0
P2_wins=0
P1=pygame.Rect(0,475,50,50)
P2=pygame.Rect(950,475,50,50)
P1_plus="forward"
P2_plus="backward"

#main loop
while game:
    
    w.fill([255,255,255])
    pygame.draw.rect(w,(255,0,0),P1)
    pygame.draw.ellipse(w,(0,0,255),P2)
    pygame.display.flip()
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
            print("You forfeited :(")
    # CHANGING ANGLE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_CAPSLOCK:
                if P1_plus == "forward":
                    P1_plus="down"
                elif P1_plus == "down":
                    P1_plus="backward"
                elif P1_plus == "backward":
                    P1_plus="up"
                elif P1_plus == "up":
                    P1_plus="forward"
            if event.key ==pygame.K_SLASH:
                if P2_plus == "forward":
                    P2_plus="down"
                elif P2_plus == "down":
                    P2_plus="backward"
                elif P2_plus == "backward":
                    P2_plus="up"
                elif P2_plus == "up":
                    P2_plus="forward"
    # MOVING
    if tsk.get_key_pressed(pygame.K_d):
        P1.x+=10
        if P1.x > 950:
            P1.x=950
    if tsk.get_key_pressed(pygame.K_a):
        P1.x-=10
        if P1.x < 0:
            P1.x=0
    if tsk.get_key_pressed(pygame.K_w):
        P1.y-=10
        if P1.y < 0:
            P1.y=0
    if tsk.get_key_pressed(pygame.K_s):
        P1.y+=10
        if P1.y > 950:
            P1.y=950
    if tsk.get_key_pressed(pygame.K_RIGHT):
        P2.x+=10
        if P2.x > 950:
            P2.x=950
    if tsk.get_key_pressed(pygame.K_LEFT):
        P2.x-=10
        if P2.x < 0:
            P2.x=0
    if tsk.get_key_pressed(pygame.K_UP):
        P2.y-=10
        if P2.y < 0:
            P2.y=0
    if tsk.get_key_pressed(pygame.K_DOWN):
        P2.y+=10
        if P2.y > 950:
            P2.y=950
    # SHOOTING
    if tsk.get_key_pressed(pygame.K_RSHIFT):
        if P1_plus == "forward":
            forward=125
            down=3
            center_y=25
            center_x=25
        if P1_plus == "backward":
            forward=125
            down=3
            center_y=25
            center_x=-100
        if P1_plus == "up":
            forward=3
            down=125
            center_y=-100
            center_x=25
        if P1_plus == "down":
            forward=3
            down=125
            center_y=25
            center_x=25
        shoot=pygame.Rect(P1.x+center_x,P1.y+center_y,forward,down)
        pygame.draw.rect(w,(255,0,0),shoot)
        pygame.display.flip()
        if shoot.colliderect(P2):
            P1_wins+=1
            P2=pygame.Rect(950,475,50,50)
            P1=pygame.Rect(0,475,50,50)
            print("P1 has " +str(P1_wins) +" points!")
    if tsk.get_key_pressed(pygame.K_PERIOD):
        if P2_plus == "forward":
            forward=125
            down=3
            center_y=25
            center_x=25
        if P2_plus == "backward":
            forward=125
            down=3
            center_y=25
            center_x=-100
        if P2_plus == "up":
            forward=3
            down=125
            center_y=-100
            center_x=25
        if P2_plus == "down":
            forward=3
            down=125
            center_y=25
            center_x=25
        shoot=pygame.Rect(P2.x+center_x,P2.y+center_y,forward,down)
        pygame.draw.rect(w,(0,0,255),shoot)
        pygame.display.flip()
        if shoot.colliderect(P1):
            P2_wins+=1
            P1=pygame.Rect(0,475,50,50)
            P2=pygame.Rect(950,475,50,50)
            print("P2 has " +str(P2_wins) +" points!")
    if P2_wins == 10:
        print("P2 wins!")
        game=False
    if P1_wins == 10:
        print("P1 wins!")
        game=False
