import pygame
pygame.init()
pygame.font.init()
wrong_answers=0

word=input("What is your word? ").lower()
print("\n"*100)
num_letters=len(word)
word_to_draw=[" "]

draw_len = num_letters
while draw_len > 0:
    word_to_draw.append("_ ")
    draw_len-=1
pos_add=0
printable_word_to_draw=""
while pos_add < len(word_to_draw):
    printable_word_to_draw+=word_to_draw[pos_add]
    pos_add+=1
my_screen=pygame.display.set_mode([500,500])
my_screen.fill([255,255,255]) 
black=(0,0,0)
#draw the shape of the hangman
pygame.draw.line(my_screen,black,(100,400),(400,400),5)
pygame.draw.line(my_screen,black,(250,400),(250,50),5)
pygame.draw.line(my_screen,black,(250,50),(350,50),5)
pygame.draw.line(my_screen,black,(350,50),(350,125),5)
myfont = pygame.font.SysFont('arial', 75)
textsurface = myfont.render(printable_word_to_draw, False, (0, 0, 0))
my_screen.blit(textsurface,(0,405))
pygame.display.flip()
game=True
difficulty=""
while difficulty != "hard" and difficulty != "medium" and difficulty != "easy":
    difficulty=input("Choose a dificulty: easy, medium, hard. ").lower()
while game:
    my_screen.fill((255,255,255))
    pygame.draw.line(my_screen,black,(100,400),(400,400),5)
    pygame.draw.line(my_screen,black,(250,400),(250,50),5)
    pygame.draw.line(my_screen,black,(250,50),(350,50),5)
    pygame.draw.line(my_screen,black,(350,50),(350,125),5)
    textsurface = myfont.render(printable_word_to_draw, False, (0, 0, 0))
    if difficulty == "hard":
        if wrong_answers >= 1:
            pygame.draw.circle(my_screen,(0,0,0),(350,160),40,5)
        if wrong_answers >= 2:
            pygame.draw.line(my_screen,(0,0,0),(350,195),(350,255),5)
        if wrong_answers >= 3:
            pygame.draw.line(my_screen,(0,0,0),(320,215),(380,215),5)
        if wrong_answers >= 4:
            pygame.draw.line(my_screen,(0,0,0),(350,255),(325,275),5)
        if wrong_answers >= 5:
            pygame.draw.line(my_screen,(0,0,0),(350,255),(375,275),5)
            print("You Lose!")
            my_screen.blit(textsurface,(0,405))
            pygame.display.flip()
            input()
            break
    if difficulty == "medium":
        if wrong_answers >= 1:
            pygame.draw.circle(my_screen,(0,0,0),(350,160),40,5)
        if wrong_answers >= 2:
            pygame.draw.line(my_screen,(0,0,0),(350,195),(350,225),5)
        if wrong_answers >= 3:
            pygame.draw.line(my_screen,(0,0,0),(320,215),(350,215),5)
        if wrong_answers >= 4:
            pygame.draw.line(my_screen,(0,0,0),(350,215),(385,215),5)
        if wrong_answers >= 5:
            pygame.draw.line(my_screen,(0,0,0),(350,215),(350,255),5)
        if wrong_answers >= 6:
            pygame.draw.line(my_screen,(0,0,0),(350,255),(325,275),5)
        if wrong_answers >= 7:
            pygame.draw.line(my_screen,(0,0,0),(350,255),(375,275),5)
            print("You Lose!")
            my_screen.blit(textsurface,(0,405))
            pygame.display.flip()
            input()
            break
    if difficulty == "easy":
        if wrong_answers >= 1:
            pygame.draw.circle(my_screen,(0,0,0),(350,160),40,5)
        if wrong_answers >= 2:
            pygame.draw.line(my_screen,(0,0,0),(350,195),(350,225),5)
        if wrong_answers >= 3:
            pygame.draw.line(my_screen,(0,0,0),(320,215),(350,215),5)
        if wrong_answers >= 4:
            pygame.draw.line(my_screen,(0,0,0),(350,215),(385,215),5)
        if wrong_answers >= 5:
            pygame.draw.line(my_screen,(0,0,0),(350,215),(350,255),5)
        if wrong_answers >= 6:
            pygame.draw.line(my_screen,(0,0,0),(350,255),(325,275),5)
        if wrong_answers >= 7:
            pygame.draw.line(my_screen,(0,0,0),(350,255),(375,275),5)
        if wrong_answers >= 8:
            pygame.draw.circle(my_screen,(0,0,0),(335,150),5,5)
        if wrong_answers >= 9:
            pygame.draw.circle(my_screen,(0,0,0),(365,150),5,5)
        if wrong_answers >= 10:
            smile=pygame.Rect(330,170,40,20)
            smile_cover=(330,170,40,10)
            pygame.draw.ellipse(my_screen,(0,0,0),smile,5)
            pygame.draw.rect(my_screen,(255,255,255),smile_cover)
            print("You Lose!")
            my_screen.blit(textsurface,(0,405))
            pygame.display.flip()
            input()
            break
    my_screen.blit(textsurface,(0,405))
    pygame.display.flip()
    guess = input("guess a letter ").lower()
    pos=0
    word_to_draw=[" "]
    while guess in word and pos < len(word):
        if guess == word[pos].lower():
            word_to_draw.append(guess)
        else:
            if word[pos] in printable_word_to_draw:
                word_to_draw.append(str(word[pos]))
            else:
                word_to_draw.append("_")
        word_to_draw.append(" ")
        pos+=1
    if guess not in word:
        draw_len = num_letters
        pos=0
        word_to_draw.append("")
        while draw_len > 0:
            if word[pos] in printable_word_to_draw:
                word_to_draw.append(str(word[pos]))
                word_to_draw.append(" ")
            else:
                word_to_draw.append("_ ")
            draw_len-=1
            pos+=1
        wrong_answers+=1
    pos_add=0
    printable_word_to_draw=""
    while pos_add < len(word_to_draw):
        printable_word_to_draw+=word_to_draw[pos_add]
        pos_add+=1
    textsurface = myfont.render(printable_word_to_draw, False, (0, 0, 0))
    my_screen.blit(textsurface,(0,405))
    pygame.display.flip()
    spaced_word=" "
    pos=0
    while len(spaced_word) < num_letters*2:
        spaced_word+=word[pos]
        spaced_word+=" "
        pos+=1
    if printable_word_to_draw == spaced_word:
        print("You Won!")
        break 
