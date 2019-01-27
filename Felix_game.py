"""
Felix_game

Description:
"""
import pygame, tsk, random
pygame.init()
window = pygame.display.set_mode([400, 400])
running = True
done = False
rect1y = random.randint(0, 350)
rect2y = random.randint(0, 350)
rect3y = random.randint(0, 350)
rect4y = random.randint(0, 350)
rect5y = random.randint(0, 350)
rect6y = random.randint(0, 350)
rect1x = random.randint(-500, -400)
rect2x = random.randint(-350, -250)
rect3x = random.randint(-200, -100)
rect4x = random.randint(-650, -550)
rect5x = random.randint(-800, -700)
rect6x = random.randint(-950, -850)
rect1 = pygame.Rect(rect1x, rect1y, 50, 50)
rect2 = pygame.Rect(rect2x, rect2y, 50, 50)
rect3 = pygame.Rect(rect3x, rect3y, 50, 50)
rect4 = pygame.Rect(rect4x, rect4y, 50, 50)
rect5 = pygame.Rect(rect5x, rect5y, 50, 50)
rect6 = pygame.Rect(rect6x, rect6y, 50, 50)
spaceship = pygame.Rect(300, 175, 50, 50)
speed1 = 5
speed2 = 5
speed3 = 5
win = 0
while running and not done:
    window.fill((0, 0, 0))
    rect1.x += speed1
    rect2.x += speed2
    rect3.x += speed3
    pygame.draw.rect(window, (122, 122, 122), rect1)
    pygame.draw.rect(window, (122, 122, 122), rect2)
    pygame.draw.rect(window, (122, 122, 122), rect3)
    if tsk.get_key_pressed(pygame.K_UP):
        spaceship.y -= 10
    if tsk.get_key_pressed(pygame.K_DOWN):
        spaceship.y += 10
    if tsk.get_key_pressed(pygame.K_LEFT):
        spaceship.x -= 10
    if tsk.get_key_pressed(pygame.K_RIGHT):
        spaceship.x += 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    if spaceship.y < -30:
        spaceship.y += 380  
    if spaceship.y > 370:
        spaceship.y -= 380
    if rect1.x > 400:
        rect1y = random.randint(0, 350)
        rect1 = pygame.Rect(rect1x, rect1y, 50, 50)
        rect1.x -= 450
        speed1 += 1
    if rect2.x > 400:
        rect2y = random.randint(0, 350)
        rect2 = pygame.Rect(rect2x, rect2y, 50, 50)
        rect2.x -= 450
        speed2 += 1
    if rect3.x > 400:
        rect3y = random.randint(0, 350)
        rect3 = pygame.Rect(rect3x, rect3y, 50, 50)
        rect3.x -= 450
        speed3 += 1
        win += 1
    if spaceship.x > 350:
        spaceship.x = 350
    if spaceship.x < 0:
        spaceship.x = 0
    if rect1.colliderect(spaceship):
        running = False
    if rect2.colliderect(spaceship):
        running = False
    if rect3.colliderect(spaceship):
        running = False
    if speed1 >= 10:
        speed4 = 10
        pygame.draw.rect(window, (122, 122, 122), rect4)
        rect4.x += speed4
        if rect4.colliderect(spaceship):
            running = False
        if rect4.x > 400:
            rect4 = pygame.Rect(rect4x, rect4y, 50, 50)
            win -= 1
            win += 1
        if speed1 >= 20:
            speed5 = 25
            pygame.draw.rect(window, (122, 122, 122), rect5)
            rect5.x += speed5
        if rect5.colliderect(spaceship):
            running = False
        if rect5.x > 400:
            rect5y = random.randint(0, 350)
            rect5x = random.randint(-800, -700)
            rect5 = pygame.Rect(rect5x, rect5y, 50, 50)
            pygame.draw.rect(window, (122, 122, 122), rect5)
            rect5.x += speed5
            win -= 1
            win += 1
        if speed1 >= 30:
            speed6 = 35
            pygame.draw.rect(window, (122, 122, 122), rect6)
            rect6.x += speed6
        if rect6.colliderect(spaceship):
            running = False
        if rect6.x > 400:
            rect6y = random.randint(0, 350)
            rect6x = random.randint(-800, -700)
            rect6 = pygame.Rect(rect6x, rect6y, 50, 50)
            pygame.draw.rect(window, (122, 122, 122), rect6)
            rect6.x += speed6
            win -= 1
            win += 1
    pygame.draw.ellipse(window, (255, 0, 0), spaceship)
    pygame.display.flip()
    pygame.time.wait(2)
print("You won " +str(win) +" times!")    
