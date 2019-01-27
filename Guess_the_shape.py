"""
Shape_Imposter_Supreme

Description:
"""
import random
import pygame
pygame.init()
w=pygame.display.set_mode([1000,300])
w.fill([255,255,255])
wins=0
guess=0
different=0
plus=15
coardinates_plus=200
counter=5
lefter=50
middler=100
righter=150
toper=50
bottomer=250
topest=5
bottomest=1
a=True
b=True
guesser="Is the different color 1, 2, 3, 4, or 5? "
while guess == different:
    left=lefter
    middle=middler
    right=righter
    top=toper
    bottom=bottomer
    count=1
    different=random.randint(1,counter)
    r=random.randint(0,230)
    g=random.randint(0,230)
    b=random.randint(0,230)
    while count <= counter:
        if count == different:
            color=(r+plus,g+plus,b+plus)
        else:
            color=(r,g,b)
        pygame.draw.polygon(w,color,[(left,bottom),(middle,top),(right,bottom)])
        count+=1
        left+=coardinates_plus
        middle+=coardinates_plus
        right+=coardinates_plus
    pygame.display.flip()
    guess=777
    while guess > topest or guess < bottomest:
        guess=int(input(guesser))
    plus-=1
    if plus == 0:
        guesser="Which one was the different color? "
        plus=5
    if plus == 5 and guesser=="Which one was the different color? " and b:
        print("WOW YOU ARE AWESOME AT THIS GAME!!!")
        b=False
    elif wins >= 30:
        Master = wins - 25
        master = "!"*Master
        print("YOU ARE THE ULTIMATE MASTER" +master)
    if guess == different and guesser=="Is the different color 1, 2, 3, 4, or 5? ":
        print("You guessed it! :)")
        wins+=1
        if wins > 1:
            print("You've won " +str(wins) +" times")
        else:
            print("You've won 1 time")
    elif guess == different and guesser=="Which one was the different color? ":
        if a:
            a=False
            wins+=1
            print("You've won " +str(wins) +" times")
        else:
            a=True
    else:
        print("Sorry, that's not right.  It was " +str(different) +".")
if wins > 1:    
    input("You won " +str(wins) +" times!")
elif wins > 0:    
    input("You won 1 time")
else:
    input("Better luck next time :(")
