import pygame
pygame.init()
pygame.font.init()


word=input("What is your word? ")
num_letters=len(word)
word_to_draw=" "

draw_len = num_letters
while draw_len > 0:
    word_to_draw +="_ "
    draw_len-=1
my_screen=pygame.display.set_mode([500,500])
my_screen.fill([255,255,255]) 
black=(0,0,0)
#draw the shape of the hangman
pygame.draw.line(my_screen,black,(100,400),(400,400),5)
pygame.draw.line(my_screen,black,(250,400),(250,50),5)
pygame.draw.line(my_screen,black,(250,50),(350,50),5)
pygame.draw.line(my_screen,black,(350,50),(350,125),5)
myfont = pygame.font.SysFont('arial', 75)
textsurface = myfont.render(word_to_draw, False, (0, 0, 0))
my_screen.blit(textsurface,(0,405))
pygame.display.flip()
guess = input("guess a letter ")

print("you guessed " + guess)
guess_len = 0
guessed_pos = -1
while guess_len < num_letters:
    if word[guess_len] == guess:
        guessed_pos = guess_len
        print("letter is in pos " + str(guessed_pos))
        break
    else:
        guess_len+=1
        
draw_len = 0
word_to_draw=""

while draw_len < num_letters:
    if draw_len == guessed_pos:
        word_to_draw+=guess
        word_to_draw+=" "
    else:
        word_to_draw +="_ "
    draw_len+=1

print("I'm trying to print " + word_to_draw)
textsurface = myfont.render(word_to_draw, False, (0, 0, 0))
my_screen.blit(textsurface,(0,405))
pygame.display.flip()
guess = input("guess a letter ")
