"""
LESSON: 3.4 - Program Structure
EXERCISE: Water Balloon Drop
"""

#### ---- SETUP ---- ####

# --- Libraries & window --- #

# Import random library
import random

# Import PYGAME
import pygame

# INITialize pygame
pygame.init()

# Open a WINDOW of size [800, 600] and assign to window
w=pygame.display.set_mode([800,600])


# --- Animation variables --- #

# Create variable ball_x and assign it 0
ball_x=0

# Create variable ball_y and assign it 0
ball_y=0

# Create variable targ_x and assign it a randint between
# 100 and 700
targ_x=random.randint(100,625)

# Create variable targ_y and assign it a randint between
# 100 and 500
targ_y=random.randint(100,425)


#### ---- DRAW TARGET ---- ####

# --- Background --- #

# FILL window with WHITE
w.fill([255,255,255])


# --- Target --- #
target_ring_outer=pygame.Rect(targ_x,targ_y,150,150)
target_ring_middle=pygame.Rect(targ_x+25,targ_y+25,100,100)
target_ring_inner=pygame.Rect(targ_x+50,targ_y+50,50,50)
target_ring_bulls=pygame.Rect(targ_x+62.5,targ_y+62.5,25,25)
# Draw a CIRCLE in window with COLOR (255, 0, 0) at
# position (targ_x, targ_y) with radius 75
pygame.draw.ellipse(w,(255,0,0),target_ring_outer)

# Draw a CIRCLE in window with COLOR (255, 255, 255) at
# position (targ_x, targ_y) with radius 50
pygame.draw.ellipse(w,(255,255,255),target_ring_middle,20)

# Draw a CIRCLE in window with COLOR (255, 0, 0) at
# position (targ_x, targ_y) with radius 25
pygame.draw.ellipse(w,(255,0,0),target_ring_inner,20)
pygame.draw.ellipse(w,(255,255,255),target_ring_bulls)

# --- Finish --- #

# FLIP the display
pygame.display.flip()



#### ---- USER GUESS ---- ####

# Get horizontal speed guess as input from user,
# typecast to a float, and assign to x_speed
# ---> TEST AFTER THIS LINE <--- #
x_speed=float(input("Please enter a horizontal speed for the water balloon: "))

# Get vertical speed guess as input from user, typecast
# to a float, and assign to y_speed

y_speed=float(input("Please enter a vertical speed for the water balloon: "))

#### ---- MAIN LOOP ---- ####

# Create variable animating and assign it True
animating=True

# While ball_x is less than 800 and ball_y is less than
# 600 and animating
while ball_x < 800 and ball_y < 600 and animating:


    # --- Event loop --- #

    # Create an EVENT LOOP that gets events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              animating=False

        # If event TYPE is EQUAL TO QUIT


            # assign animating the value False
            # ---> TEST AFTER THIS LINE <--- #



    # --- Move ball --- #

    # Increment ball_x by x_speed
    ball_x+=x_speed

    # Increment ball_y by y_speed
    # ---> TEST AFTER THIS LINE <--- #
    ball_y+=y_speed


    # --- Re-draw background --- #

    # FILL the window with WHITE
    w.fill([255,255,255])


    # --- Re-draw target --- #

    # Draw a CIRCLE in window with COLOR (255, 0, 0) at
    # position (targ_x, targ_y) with radius 75
    pygame.draw.ellipse(w,(255,0,0),target_ring_outer,20)

    # Draw a CIRCLE in window with COLOR (255, 255,
    # 255) at position (targ_x, targ_y) with radius 50
    pygame.draw.ellipse(w,(255,255,255),target_ring_middle,20)


    # Draw a CIRCLE in window with COLOR (255, 0, 0) at
    # position (targ_x, targ_y) with radius 25
    # ---> TEST AFTER THIS LINE <--- #
    pygame.draw.ellipse(w,(255,0,0),target_ring_inner,20)
    pygame.draw.ellipse(w,(255,255,255),target_ring_bulls)
    # --- Draw ball --- #

    # Draw a CIRCLE in window with COLOR (0, 0, 255) at
    # (int(ball_x), int(ball_y)) with radius 25
    # ---> TEST AFTER THIS LINE <--- #
    balloon=pygame.Rect(int(ball_x),int(ball_y),50,50)
    if balloon.colliderect(target_ring_outer):
        print("Pop!")
        print("You barely hit the target!")
        animating=False
    elif balloon.colliderect(target_ring_middle):
        print("Pop!")
        print("You hit the target!")
        animating=False
    elif balloon.colliderect(target_ring_inner):
        print("Pop!")
        print("Almost a bull's eye!")
        animating=False
    elif balloon.colliderect(target_ring_bulls):
        print("Pop!")
        print("BULL'S EYE!")
        animating=False
    else:
        pygame.draw.ellipse(w,(0, 0, 255),balloon)


    # --- Finish drawing --- #

    # FLIP the display
    pygame.display.flip()

    # WAIT 15 milliseconds
    # ---> TEST AFTER THIS LINE <--- #
    pygame.time.wait(15)



# Turn in your Coding Exercise.
