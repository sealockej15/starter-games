"""
Pokemon_chapter_2

Description:
"""
import sys
import pygame
pygame.init()
def is_exit(input_cmd):
    if input_cmd.upper() == "EXIT":
        sys.exit()
pygame.init()
starter=input("Do you want Charmander, Bulbasaur or Squirtle? ")


print("I hear that the next gym is past route 3,4,5 and 6. Better get going and don't forget to catch pokemon on the way.")
help_person=input("On route 3 you hear someone yelling HELP! If you help the person type help if not type continue. ")
if help_person.upper()=="HELP":
    fight=input("You follow the voice and see a Wobbuffet, Meowth, a woman and a man with an R on their shirts. You go up to them and ask them who they are. And then the they says. Prepare for trouble! And make it double! To protect the world from devastation! To unite all peoples within our nation! To denounce the evils of truth and love! To extend our reach to the stars above! Jessie, said the woman. James, says the man. Then they say Team Rocket blasts off at the speed of light surrender now or prepare to fight! The meowth says Meowth thats right, and the Wobbeffet says Wobbefet. Do you say I'll fight you! Or type run away? ")
is_exit(help_person)
if help_person.upper()=="CONTINUE":
    fight=input("You notice there is a boulder in the way you have no choise but to follow the voice. You follow the voice and see a Wobbuffet, Meowth, a woman and a man with an R on their shirts. You go up to them and ask them who they are. And then the they says. Prepare for trouble! And make it double! To protect the world from devastation! To unite all peoples within our nation! To denounce the evils of truth and love! To extend our reach to the stars above! Jessie, said the woman. James, says the man. Then they say Team Rocket blasts off at the speed of light surrender now or prepare to fight! The meowth says Meowth thats right, and the Wobbeffet says Wobbefet. Do you say I'll fight you! Or type run away? ")
is_exit(fight)
if fight.upper()=="I'LL FIGHT YOU!":
    pokemon=input("I've heard of team rocket they use poison types so try using Diglet. Stop playing with your fancy gadgets! Jessie said then told Ekans to use poison sting to break your pokegear. Choose a Pokemon already! Do you want " +starter +", Poliwrath, Tentacool or Diglet? ")
if fight.upper()=="I'LL FIGHT YOU":
    pokemon=input("The proffesor says I've heard of team rocket they use poison types so try using Diglet. Stop playing with your fancy gadgets! Jessie said then told Ekans to use poison sting to break your pokegear. Choose a Pokemon already! Do you want " +starter +", Poliwrath, Tentacool or Diglet? ")
if fight.upper()=="RUN AWAY":
    pokemon=input("You start running away but James says Oh no you don't! And tells koffing to block your path. The proffesor says I've heard of team rocket they use poison types so try using Diglet. Stop playing with your fancy gadgets! Jessie said then told Ekans to use poison sting to break your pokegear. Choose a Pokemon already! Do you want " +starter +", Poliwrath, Tentacool or Diglet? ")
is_exit(fight)
if pokemon.upper()=="TENTACOOL":
    current_move=input("Choose a move Hydro Pump or Poison Jab. ")
if pokemon.upper()=="CHARMANDER":
    current_move=input("Choose a move Ember, Scratch, or Leer. ")
if pokemon.upper()=="SQUIRTLE":
    current_move=input("Choose a move Water Gun, Tackle, or Growl. ")
if pokemon.upper()=="BULBASAUR":
    current_move=input("Choose a move Absorb, Tackle, or Leer. ")
if pokemon.upper()=="POLIWRATH":
    current_move=input("Choose a move Surf or Thunder punch. ")
if pokemon.upper()=="DIGLET":
    current_move=input("Choose a move Earthquake or Dig. ")
is_exit(current_move)
if current_move.lower()=="ember" or current_move.lower()=="absorb" or current_move.lower()=="leer" or current_move.lower()=="tackle" or current_move.lower()=="water gun" or current_move.lower()=="scratch" or current_move.lower()=="growl":
    print("Koffing jumped in the way so Ekans wasn't hit then Ekans used poison sting and " +starter +" fainted.") +sys.exit()
if current_move.lower()=="surf":
    print("Koffing jumped in the way so Ekans wasn't hit then Ekans used poison sting and Poliwrath fainted.") +sys.exit()
if current_move.lower()=="thunder punch":
    print("Koffing jumped in the way so Ekans wasn't hit then Ekans used poison sting and Poliwrath fainted.") +sys.exit()
if current_move.lower()=="hydro pump":
    print("Koffing jumped in the way so Ekans wasn't hit then Ekans used poison sting and Tentacool fainted.") +sys.exit()
if current_move.lower()=="poison jab":
    print("Koffing jumped in the way so Ekans wasn't hit then Ekans used poison sting and Tentacool fainted.") +sys.exit()
if current_move.lower()=="dig":
    print("Diglet dug underneath Koffing and hit Ekans. Ekans fainted let's run said Meowth the person who needed help said thank you and gave you HM Rock Smash.")
if current_move.lower()=="earthquake":
    print("Diglet's earthquake went under koffing and hit Ekans. Ekans fainted let's run said Meowth the person who needed help said thank you and gave you HM Rock Smash.")
if current_move.lower()=="dig" or current_move.lower()=="earthquake":
    print("You head back to the proffesor's lab and on route one you see a Tentacool jumping at people because it was trying to avoid team rocket that must be why a Tentacool jumped at you before.")
print("You have the proffesor fix your pokegear and then the proffesor said to you HM rocksmash makes it so you can break the boulder in your way on route 3.")
input("You head to route 3 but then see a boulder. Do you crack the boulder by using rock smash?")
pokemon=input("Crack! When you cracked open the boulder it woke up a wild Pidgeotto you need to chose a pokemon that knows a electric move quick! Do you want " +starter +", Poliwrath, Tentacool or Diglet? ")
if pokemon.upper()=="TENTACOOL":
    current_move=input("Choose a move Hydro Pump or Poison Jab. ")
if pokemon.upper()=="CHARMANDER":
    current_move=input("Choose a move Ember, Scratch, or Leer. ")
if pokemon.upper()=="SQUIRTLE":
    current_move=input("Choose a move Water Gun, Tackle, or Growl. ")
if pokemon.upper()=="BULBASAUR":
    current_move=input("Choose a move Absorb, Tackle, or Leer. ")
if pokemon.upper()=="POLIWRATH":
    current_move=input("Choose a move Surf, Rock Smash or Thunder punch. ")
if pokemon.upper()=="DIGLET":
    current_move=input("Choose a move Earthquake or Dig. ")
if current_move.lower()=="ember" or current_move.lower()=="absorb" or current_move.lower()=="leer" or current_move.lower()=="tackle" or current_move.lower()=="water gun" or current_move.lower()=="scratch" or current_move.lower()=="growl":
    print("Pidgeotto was so fast it dodged the attack then used gust " +starter +" fainted.") +sys.exit()
if current_move.upper()=="SURF" or current_move.lower()=="ROCK SMASH":
    print("Pidgeotto was so fast it dodged the attack then used gust Poliwrath fainted. ") +sys.exit()
if current_move.upper()=="DIG" or current_move.upper=="EARTHQUAKE":
    print("Pidgeotto was so fast it dodged the attack then used peck Diglet fainted") +sys.exit()
if current_move.upper()=="HYDRO PUMP" or current_move.upper=="POISON JAB":
    print("Pidgeotto was so fast it dodged the attack then used peck Tentacool fainted") +sys.exit()
if current_move.upper()=="THUNDER PUNCH":
    catch=input("Pidgeotto got hit so hard he fell out of the sky say Go Pokeball! ")
if catch.lower()=="go pokeball":
    print("Congradulations you caught a Pidgeotto.")
if catch.lower()=="go pokeball!":
    print("Congradulations you caught a Pidgeotto.")
choose=input("You walk farther and see a place where there is supposed to be a bridge but there isn't. But there is a trainer to your left and to your right choose one. If you go right type right if you go left type left.")
if choose.lower()=="right":
    choose=input("To skip to route five you need to fight me or you can go left. Do you fight or go left? ")
if choose.lower()=="fight":
    pokemon=input("choose a pokemon I'll choose Clefable do you want " +starter +", Poliwrath, Tentacool or Diglet? ")
if pokemon.upper()=="TENTACOOL":
    current_move=input("Choose a move Hydro Pump or Poison Jab. ")
if pokemon.upper()=="CHARMANDER":
    current_move=input("Choose a move Ember, Scratch, or Leer. ")
if pokemon.upper()=="SQUIRTLE":
    current_move=input("Choose a move Water Gun, Tackle, or Growl. ")
if pokemon.upper()=="BULBASAUR":
    current_move=input("Choose a move Absorb, Tackle, or Leer. ")
if pokemon.upper()=="POLIWRATH":
    current_move=input("Choose a move Surf, Rock Smash or Thunder punch. ")
if pokemon.upper()=="DIGLET":
    current_move=input("Choose a move Earthquake or Dig. ")
if current_move.lower()=="ember" or current_move.lower()=="absorb" or current_move.lower()=="leer" or current_move.lower()=="tackle" or current_move.lower()=="water gun" or current_move.lower()=="scratch" or current_move.lower()=="growl":
    print("Clefables was faster then you and used Moon Blast " +starter +" fainted.") +sys.exit()
if current_move.upper=="SURF" or current_move.lower()=="ROCK SMASH" or current_move.lower()=="THUNDER PUNCH":
    print("Clefables was faster then you and used Moon Blast Poliwrath fainted.") +sys.exit()
if current_move.upper=="DIG" or current_move.upper=="EARTHQUAKE":
    print("Clefables was faster then you and used Moon Blast Diglet fainted.") +sys.exit()
if current_move.upper=="HYDRO PUMP":
    print("Clefables was faster then you and used Moon Blast Tentacool fainted.") +sys.exit()
if current_move.upper=="POISON JAB":
    print("WOW! How did you know poison was good on fairy! I will tell my Pidgeot to fly you to route five.")
if choose.lower()=="left":
    choose=input("Do you go right to earn a skip to route five or let me tell you a tip? For a tip type tip to go right type right. ")
if choose.lower()=="tip":
    fly=input("Tell your Pidgeotto to use fly by saying fly.")
if fly.lower()=="fly":
    pokemon=input("Congradulations! You are now on route 4. You walk along the path and see a Bellsprout in the way choose a pokemon do you want " +starter +", Poliwrath, Tentacool, Diglet or Pidgeotto? ")
if pokemon.upper()=="TENTACOOL":
    current_move=input("Choose a move Hydro Pump or Poison Jab. ")
if pokemon.upper()=="CHARMANDER":
    current_move=input("Choose a move Ember, Scratch, or Leer. ")
if pokemon.upper()=="SQUIRTLE":
    current_move=input("Choose a move Water Gun, Tackle, or Growl. ")
if pokemon.upper()=="BULBASAUR":
    current_move=input("Choose a move Absorb, Tackle, or Leer. ")
if pokemon.upper()=="POLIWRATH":
    current_move=input("Choose a move Surf, Rock Smash or Thunder punch. ")
if pokemon.upper()=="DIGLET":
    current_move=input("Choose a move Earthquake or Dig. ")
if pokemon.upper()=="PIDGEOTTO":
    current_move=input("Choose a move Peck or gust or fly. ")
if current_move.lower()=="absorb" or current_move.lower()=="leer" or current_move.lower()=="tackle" or current_move.lower()=="water gun" or current_move.lower()=="scratch" or current_move.lower()=="growl":
    print("Bellsprout used growth it raised it's attack then used vine whip " +starter +" fainted.") +sys.exit()
if current_move.lower()=="ember":
    catch=input("Bellsprout is on fire so he is distracted quick say Go Pokeball!")
if current_move.lower()=="fly" or current_move.lower()=="gust" or current_move.lower()=="peck":
    catch=input("Bellsprout tried to grow but Pidgeotto soared in and hit him hard quick say Go Pokeball!")
if current_move.upper=="DIG" or current_move.upper=="EARTHQUAKE":        
    print("Bellsprout used growth and was so tall that diglet was so surprised he jumped off a cliff Diglet fainted") +sys.exit()
if current_move.upper=="HYDRO PUMP" or current_move.upper=="POISON JAB":
    print("Bellsprout used growth and was so tall that diglet was so surprised he jumped off a cliff Tentacool fainted") +sys.exit()
if current_move.upper=="SURF" or current_move.upper()=="ROCK SMASH" or current_move.upper=="THUNDER PUNCH":
    print("Bellsprout used growth and was so tall that diglet was so surprised he jumped off a cliff Poliwrath fainted") +sys.exit()
if catch.lower()=="go pokeball":
    print("Congradulations you caught a Bellsprout.")
if catch.lower()=="go pokeball!":
    print("Congradulations you caught a Bellsprout.")
if catch.lower()=="go pokeball!" or catch.lower()=="go pokeball":
    print("You walk farther and see you finally made it to route five.")
    
    
    is_exit(catch)
    is_exit(current_move)
    is_exit(pokemon)
    is_exit(fly)
    is_exit(choose)
    is_exit(left)
    
