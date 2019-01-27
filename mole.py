"""
Whack_a_mole

Description:
"""
def board():
    x=10
    y=10
    w.fill((17, 130, 11))
    hole=pygame.Rect(x,y,80,80)
    while x < 300:
        pygame.draw.ellipse(w,(0,0,0),hole)
        y+=100
        hole=pygame.Rect(x,y,80,80)
        pygame.draw.ellipse(w,(0,0,0),hole)
        y+=100
        hole=pygame.Rect(x,y,80,80)
        pygame.draw.ellipse(w,(0,0,0),hole)
        y-=200
        x+=100
        hole=pygame.Rect(x,y,80,80)
import pygame
import random
pygame.init()
w=pygame.display.set_mode([300,300])
c=pygame.time.Clock()
x_plus=15
y_plus=10
timer=0
spot=0
points=0
time=2000
mole_color=(112, 99, 59)
go=True
game=True
start=pygame.time.get_ticks()
pygame.mouse.set_visible(False)
while game:
    last=pygame.time.get_ticks()
    timer=last-start
    board()
    if timer >= 900 and go:
        spot=random.randint(1,9)
        go=False
    if timer >= 1000:
        if spot == 1:
            mole=pygame.Rect(15,15,70,70)
            pygame.draw.ellipse(w,mole_color,mole)
        if spot == 2:
            mole=pygame.Rect(115,15,70,70)
            pygame.draw.ellipse(w,mole_color,mole)
        if spot == 3:
            mole=pygame.Rect(215,15,70,70)
            pygame.draw.ellipse(w,mole_color,mole)
        if spot == 4:
            mole=pygame.Rect(15,115,70,70)
            pygame.draw.ellipse(w,mole_color,mole)
        if spot == 5:
            mole=pygame.Rect(115,115,70,70)
            pygame.draw.ellipse(w,mole_color,mole)
        if spot == 6:
            mole=pygame.Rect(215,115,70,70)
            pygame.draw.ellipse(w,mole_color,mole)
        if spot == 7:
            mole=pygame.Rect(15,215,70,70)
            pygame.draw.ellipse(w,mole_color,mole)
        if spot == 8:
            mole=pygame.Rect(115,215,70,70)
            pygame.draw.ellipse(w,mole_color,mole)
        if spot == 9:
            mole=pygame.Rect(215,215,70,70)
            pygame.draw.ellipse(w,mole_color,mole)
    if timer >= time:
        game=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hammer_top.colliderect(mole):
                points+=1
                timer=0
                go=True
                start=last
                time-=50
                if time < 250:
                    time+=50
    x,y=pygame.mouse.get_pos()
    hammer_top=pygame.Rect(x-40,y-40,80,40)
    hammer_bottom=pygame.Rect(x-10,y,20,80)
    pygame.draw.rect(w,(73, 55, 16),hammer_top)
    pygame.draw.rect(w,(56, 49, 35),hammer_bottom)
    pygame.display.flip()
    c.tick(60)
    
    
    
    
    
pygame.display.flip()
if points == 1:
    print("You wacked " +str(points) +" mole.")
else:
    print("You wacked " +str(points) +" moles.")