import pygame, random
pygame.init()
def set_up():
    #draw grass
    pygame.draw.line(w,(0,0,0),(0,475),(550,475))
    pygame.draw.line(w,(0,0,0),(0,335),(550,335))
    pygame.draw.line(w,(0,0,0),(0,310),(550,310))
    pygame.draw.line(w,grass_color,(10,465),(10,410),5)
    pygame.draw.line(w,grass_color,(17,465),(17,403),5)
    pygame.draw.line(w,grass_color,(24,465),(24,386),5)
    pygame.draw.line(w,grass_color,(31,465),(31,405),5)
    pygame.draw.line(w,grass_color,(38,465),(38,408),5)
    pygame.draw.line(w,grass_color,(45,465),(45,423),5)
    pygame.draw.line(w,grass_color,(52,465),(52,396),5)
    pygame.draw.line(w,grass_color,(59,465),(59,403),5)
    pygame.draw.line(w,grass_color,(66,465),(66,380),5)
    pygame.draw.line(w,grass_color,(73,465),(73,414),5)
    pygame.draw.line(w,grass_color,(82,465),(82,406),5)
    pygame.draw.line(w,grass_color,(90,465),(90,384),5)
    pygame.draw.line(w,grass_color,(10,466),(90,466),3)
    #boxes
    pygame.draw.rect(w,(0,0,0),mushroom_box,5)
    pygame.draw.rect(w,(0,0,0),podzol_box,5)
    pygame.draw.rect(w,(0,0,0),dirt_box,5)
    pygame.draw.rect(w,(0,0,0),seed_box,5)
    pygame.draw.rect(w,(0,0,0),mycelium_box,5)
    #say names
    say_dirt = myfont.render("dirt", False, (0, 0, 0))
    w.blit(say_dirt,(425,335))
    say_podzol = myfont.render("podzol", False, (0, 0, 0))
    w.blit(say_podzol,(290,335))
    say_grass = myfont.render("grass", False, (0, 0, 0))
    w.blit(say_grass,(2.5,335))
    say_mushroom = myfont.render("mushroom block", False, (0, 0, 0))
    w.blit(say_mushroom,(122.5,335))
    say_mycelium = myfont.render("mycelium", False, (0, 0, 0))
    w.blit(say_mycelium,(0,170))
    #draw blocks
    pygame.draw.rect(w,(193, 165, 133),mushroom_block)
    pygame.draw.rect(w,(104, 83, 59),podzol_dirt)
    pygame.draw.rect(w,(94, 53, 7),podzol_top)
    pygame.draw.rect(w,(104, 83, 59),dirt_block)
    pygame.draw.rect(w,(104, 83, 59),mycelium_dirt)
    pygame.draw.rect(w,(120, 113, 130),mycelium_top)
#set up
w=pygame.display.set_mode([550,500])
w.fill((255,255,255))
myfont = pygame.font.SysFont('arial', 25)
#variables
mushroom_amount=0
podzol_amount=0
seed_amount=0
dirt_amount=0
mycelium_amount=0
grass_color=(67, 132, 29)
pygame.display.flip()
running=True
#rects
mycelium_top=pygame.Rect(10,215,80,20)
mycelium_box=pygame.Rect(0,205,100,100)
mycelium_dirt=pygame.Rect(10,215,80,80)
dirt_block=pygame.Rect(435,382.5,80,80)
dirt_box=pygame.Rect(425,372.5,100,100)
podzol_top=pygame.Rect(285,382.5,80,20)
podzol_dirt=pygame.Rect(285,382.5,80,80)
podzol_box=pygame.Rect(275,372.5,100,100)
mushroom_box=pygame.Rect(125,372.5,100,100)
mushroom_block=pygame.Rect(135,382.5,80,80)
seed_box=pygame.Rect(0,372.5,100,100)
#main loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            #check if you get item
            if x >= 0 and x <= 100 and y >= 372.5 and y <= 475:
                yes_or_no=random.randint(1,8)
                if yes_or_no == 1:
                    seed_amount+=1
            if x >= 125 and x <= 225 and y >= 372.5 and y <= 475:
                yes_or_no=random.randint(1,8)
                if yes_or_no == 1:
                    mushroom_plus=random.randint(0,2)
                    mushroom_amount+=mushroom_plus
            if x >= 425 and x <= 525 and y >= 372.5 and y <= 475:
                if podzol_amount >= 1:
                    dirt_amount+=1
                    podzol_amount-=1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x,y=pygame.mouse.get_pos()
                if x >= 275 and x <= 375 and y >= 372.5 and y <= 475:
                    if seed_amount >= 1 and mushroom_amount >= 1:
                        seed_amount-=1
                        mushroom_amount-=1
                        podzol_amount+=1
                if x >= 0 and x <= 100 and y >= 205 and y <= 305:
                    if mushroom_amount >= 1 and dirt_amount >= 1:
                        dirt_amount-=1
                        mushroom_amount-=1
                        mycelium_amount+=1
    #printing out how much
    mushroom="mushrooms: " +str(mushroom_amount)
    seed="seeds: " +str(seed_amount)
    podzol="podzol: " +str(podzol_amount)
    dirt="dirt: " +str(dirt_amount)
    mycelium="mycelium: " +str(mycelium_amount)
    w.fill((255,255,255))
    set_up()
    seed_draw = myfont.render(seed, False, (0, 0, 0))
    podzol_draw = myfont.render(podzol, False, (0, 0, 0))
    mushroom_draw = myfont.render(mushroom, False, (0, 0, 0))
    dirt_draw = myfont.render(dirt, False, (0, 0, 0))
    mycelium_draw = myfont.render(mycelium, False, (0, 0, 0))
    w.blit(mycelium_draw,(0,310))
    w.blit(mushroom_draw,(125,475))
    w.blit(podzol_draw,(285,475))
    w.blit(dirt_draw,(425,475))
    w.blit(seed_draw,(0,475))
    pygame.display.flip()

    