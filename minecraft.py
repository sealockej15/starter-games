"""
Minecraft

Description:
"""
import sys

def is_exit(input_cmd):
    if input_cmd.upper() == "EXIT":
        sys.exit()
def chapter2():
    print("Now that you have a house you try to make a bed.")
    wool=input("Do you fight spiders by typing spider or kill sheep by typing sheep? ")
    if wool.lower() == "spider":
        my_health = 20
        spider_health = 25
        last_move = ""
        spider_damage = 5
        jump_hit_damage = 14
        hit_damage = 7
        print("There is a spider!")
        while spider_health > 0 and my_health > 0: 
            move=input("Attack it! ")
            if move.lower() == "jh":
                if last_move == move:
                    print("Are you trying to cheat!?")
                    print("I will have to kick you out to teach you a lesson. ")
                    sys.exit()
                else:
                    spider_health -= jump_hit_damage
                    print("You did " +str(jump_hit_damage) +" damage!")
                    print("The spider has " + str(spider_health) +" health.")
            elif move.lower() == "h":
                spider_health -= hit_damage
                print("You did " +str(hit_damage) +" damage!")
                print("The spider has " + str(spider_health) +" health.")
            my_health -= spider_damage
            print("The spider bit you and did 5 damage you have " +str(my_health) +" health left.")
            last_move = move
        if spider_health <= 0:
            print("You win!")
        else:
            print("You lost :(")
            sys.exit()
    elif wool.lower() == "sheep":
        my_health = 20
        sheep_health = 15
        last_move = ""
        sheep_damage = 1
        jump_hit_damage = 14
        hit_damage = 7
        print("There is a sheep!")
        while sheep_health > 0 and my_health > 0: 
            move=input("Attack it! ")
            if move.lower() == "jh":
                if last_move == move:
                    print("Are you trying to cheat!?")
                    print("I will have to kick you out to teach you a lesson. ")
                    sys.exit()
                else:
                    sheep_health -= jump_hit_damage
                    print("You did " +str(jump_hit_damage) +" damage!")
                    print("The sheep has " + str(sheep_health) +" health.")
            elif move.lower() == "h":
                sheep_health -= hit_damage
                print("You did " +str(hit_damage) +" damage!")
                print("The sheep has " + str(sheep_health) +" health.")
            my_health -= sheep_damage
            print("The sheep bahed at you and did 1 damage you have " +str(my_health) +" health left.")
            last_move = move
        if sheep_health <= 0:
            print("You win!")
        else:
            print("You lost :(")
    else:
        while wool.lower() != "sheep" and wool.lower() != "spider":
            wool=input("Choose one, Sheep or Spider!")
            if wool.lower() == "spider":
                my_health = 20
                spider_health = 25
                last_move = ""
                spider_damage = 5
                jump_hit_damage = 14
                hit_damage = 7
                print("There is a spider!")
                while spider_health > 0 and my_health > 0: 
                    move=input("Attack it! ")
                    if move.lower() == "jh":
                        if last_move == move:
                            print("Are you trying to cheat!?")
                            print("I will have to kick you out to teach you a lesson. ")
                            sys.exit()
                        else:
                            spider_health -= jump_hit_damage
                            print("You did " +str(jump_hit_damage) +" damage!")
                            print("The spider has " + str(spider_health) +" health.")
                    elif move.lower() == "h":
                        spider_health -= hit_damage
                        print("You did " +str(hit_damage) +" damage!")
                        print("The spider has " + str(spider_health) +" health.")
                    my_health -= spider_damage
                    print("The spider bit you and did 5 damage you have " +str(my_health) +" health left.")
                    last_move = move
                if spider_health <= 0:
                    print("You win!")
                else:
                    print("You lost :(")
                    sys.exit()
            elif wool.lower() == "sheep":
                my_health = 20
                sheep_health = 15
                last_move = ""
                sheep_damage = 1
                jump_hit_damage = 14
                hit_damage = 7
                print("There is a sheep!")
                while sheep_health > 0 and my_health > 0: 
                    move=input("Attack it! ")
                    if move.lower() == "jh":
                        if last_move == move:
                            print("Are you trying to cheat!?")
                            print("I will have to kick you out to teach you a lesson. ")
                            sys.exit()
                        else:
                            sheep_health -= jump_hit_damage
                            print("You did " +str(jump_hit_damage) +" damage!")
                            print("The sheep has " + str(sheep_health) +" health.")
                    elif move.lower() == "h":
                        sheep_health -= hit_damage
                        print("You did " +str(hit_damage) +" damage!")
                        print("The sheep has " + str(sheep_health) +" health.")
                    my_health -= sheep_damage
                    print("The sheep bahed at you and did 1 damage you have " +str(my_health) +" health left.")
                    last_move = move
                if sheep_health <= 0:
                    print("You win!")
                else:
                    print("You lost :(")
    print("Yay now we have enough wool to make a bed!")
    open=input("Open your crafting table. ")
def chapter1():
    print("You finally are in a new world YAY!!!")
    walk=input("The tree is 5 blocks forward and 3 blocks left and 1 jump. ")
    if walk.lower() == "w 5,a 3,j":
        wood=input("Break the amount of wood you need. ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if wood.lower() == "b 3":
        open=input("Glad you remembered how much wood to break now open your inventory. ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if open.lower() == "e":
        craft=input("What do you want to make? ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if craft.lower() == "wood planks":
        much=input("How many? ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if much.lower() == "12":
        craft=input("What do you want to make? ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if craft.lower() == "sticks 8,crafting table":
        place=input("Place your crafting table. ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if place.lower() == "p crafting table":
        open=input("Open your crafting table. ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if open.lower() == "e":
        craft=input("What do you want to make? ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if craft.lower() == "pickaxe":
        walk=input("There is a group of 10 stone 5 blocks to the right, jump once and 4 blocks forward. ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if walk.lower() == "d 5,j,w 4":
        breaka=input("Break all of the stone. ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if breaka.lower() == "b 10":
        walk=input("There is 100 stone 5 blocks forward 2 blocks left and 2 jumps. ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if walk.lower() == "w 5,a 2,j 2":
        breaka=input("Break all the stone. ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if breaka.lower() == "b 100":
        open=input("Open your crafting table. ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if open.lower() == "e":
        craft=input("What do you want to make? (Do it in alphabetical order) ")
    else:
        print("You should probably do the tutorial again.")
        sys.exit()
    if craft.lower() == "furnace,stone axe,stone pickaxe,stone sword":
        build=input("How much stone to make a 5 x 5 x 3 house. ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if build.lower() == "57":
        place=input("Place your crafting table in the house by for example: typing p house,wood. ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if place.lower() == "p house,crafting table":
        place=input("Place your furnace. ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if place.lower() == "p house, furnace":
        print("type skip 2 to go to chapter 2.")
        print("Remember skip 2.")
        print("skip 2.")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
def build():
    print("Welcome to the last tutorial. Where we will teach you how to build.")
    print("(There will be a test at the end)")
    print("To make a 3 x 3 x 3 house you would first calculate 3 x 3 x 3 in your head then hollow it out so a normal minecraft person can fit.")
    input("How many blocks do you need? ")
    print("The answer is 25 blocks.")
    test=input("How many blocks for a 8 x 8 x 3? ")
    if test.lower() == "120":
        print("Yay to make a new world with out any tutorials type skip.")
def fight():
    # starting health
    my_health = 20
    zombie_health = 22
    last_move = ""
    
    #damage
    zombie_damage = 3
    jump_hit_damage = 14
    hit_damage = 7
    
    #instructions
    print("In this tutorial I will teach you to fight.")
    print("To hit something type h.")
    print("Your stone sword does 7 damage.")
    print("Type jh to jump and hit which does 14 damage but can only be used every other hit. ")
    print("A zombie is walking by it has " + str(zombie_health) +" health.")
    
    while zombie_health > 0 and my_health > 0: 
        move=input("Attack it! ")
        if move.lower() == "jh":
            if last_move == move:
                print("Are you trying to cheat!?")
                print("I will have to kick you out to teach you a lesson. ")
                sys.exit()
            else:
                zombie_health -= jump_hit_damage
                print("You did " +str(jump_hit_damage) +" damage!")
                print("The zombie has " + str(zombie_health) +" health.")
        elif move.lower() == "h":
            zombie_health -= hit_damage
            print("You did " +str(hit_damage) +" damage!")
            print("The zombie has " + str(zombie_health) +" health.")
        my_health -= zombie_damage
        print("The zombie punched you and did 3 damage you have " +str(my_health) +" health left.")
        last_move = move
    if zombie_health <= 0:
        print("You win!")
        print("The next password is build.")
    else:
        print("You lost :(")
        sys.exit()
#Tutoral-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def new_world():
    print("In this game w is forward a is left s is back d is right and j is jump. To do that command more than once put a number behind it like d 3. To make the player move left twice then forward one you would do a 2,w. ")
    far=input("There is a tree 3 blocks in front of you type w 3 to move to it. ")
    if far.lower() == "w 3":
        current_button=input("Type b to break a block, there are 5 blocks of wood you need 3 so break 3 wood. ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if current_button.lower() == "b 3":
        print("You have 3 blocks of oak wood now. ")
        current_button=input("Enter your inventory by typing e. ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if current_button.lower() == "e":
        create=input("What do you want to make? Wood planks or nothing? ")
    if create.lower() == "wood planks":
        print("Make 12 wood planks. ")
        many=input("How many wood planks do you want? ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if many.lower() == "12":
        print("Crafting 12 wood planks...")
        print("To craft muliple items for example: b 2,e to make 2 b's and 1 e")
        print("We need 8 sticks and 1 crafting table.")
        print("When crafting stuff you don't need the 1.")
        create=input("Stuff you can make is sticks, buttons or crafting table. What would you like to make? ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if create.lower() == "sticks 8,crafting table":
        print("Good job!")
        print("To place an object on the ground press p, than the thing you want to place.")
        print("For example: p Oak wood.")
        place=input("Place the crafting table. ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if place.lower() == "p crafting table":
        current_button=input("Open the crafting table by typing e")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if current_button.lower() == "e":
        print("Now make a Pickaxe")
        item=input("What do you want to make? ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if item.lower() == "pickaxe":
        print("Crafting Pickaxe...")
        print("OK now that you have a pickaxe you can break stone.")
        walk=input("You need to get to the stone that is 2 right and 3 back away. ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if walk.lower() == "d 2,s 3":
        print("We need 16 pieces of stone")
        print("You walked to the stone and see 10 pieces of stone.")
        destroy=input("Break the stone. ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if destroy.lower() == "b 10":
        print("You now have 10 pieces of stone.")
        walk=input("You are 5 blocks left and 4 blocks forward away from more stone walk to it. ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if walk.lower() == "a 5,w 4":
        print("You walked to the stone and see 100 pieces of stone.")
        destroy=input("Break the stone you need. ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if destroy.lower() == "b 6":
        e=input("Open your Crafting table.")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if e.lower() == "e":
        print("Make 1 Stone Pickaxe, 1 Stone Axe, 1 Stone Sword, and 1 furnace. ")
        make=input("What do you want to make? ")
    else:
        print("The game doesn't understand so it kicked you out.")
        sys.exit()
    if make.lower() == "stone pickaxe,stone axe,stone sword,furnace":
        print("Here is a secret if you type fight when creating a new world you can skip the tutorial.")
        print(skip())
world=input("Do you want a new world? ")
if world.lower() == "fight":
    print(fight())
elif world.lower() == "build":
    print(build())
elif world.lower() == "skip 2":
    print(chapter2())
elif world.lower() == "skip":
    print(chapter1())
else:
    print(new_world())








