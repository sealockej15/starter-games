"""
Fantasy_Football_Pick_Em

Description:
"""
import sys

def is_exit(input_cmd):
    if input_cmd.upper() == "EXIT":
        sys.exit()
        
def make_picks():
    wins_player = 0
    player_game1=input("In game 1 who do you think will win Falcons or Eagles. ")
    if player_game1.lower() == "eagles":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game2=input("In game 2 who do you think will win Bengals or Colts. ")
    if player_game2.lower() == "colts":
        print("Nice pick! Your points are " +str(wins_player) +". ")
        wins_player += 1
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game3=input("In game 3 who do you think will win Bills or Ravens. ")
    if player_game3.lower() == "ravens":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game4=input("In game 4 who do you think will win Buccaneers or Saints. ")
    if player_game4.lower() == "buccaneers":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game5=input("In game 5 who do you think will win Texans or Patriots. ")
    if player_game5.lower() == "patriots":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game6=input("In game 6 who do you think will win 49ers or Vikings. ")
    if player_game6.lower() == "vikings":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game7=input("In game 7 who do you think will win Titans or Dolphins. ")
    if player_game7.lower() == "dolphins":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game8=input("In game 8 who do you think will win Jaguars or Giants. ")
    if player_game8.lower() == "jaguars":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game9=input("In game 9 who do you think will win Steelers or Browns. ")
    if player_game9.lower() == "steelers" or "browns":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game10=input("In game 10 who do you think will win Titans or Cheifs. ")
    if player_game10.lower() == "cheifs":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game11=input("In game 11 who do you think will win Cowboys or Panthers. ")
    if player_game11.lower() == "panthers":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game12=input("In game 12 who do you think will win Redskins or Cardinals. ")
    if player_game12.lower() == "redskins":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game13=input("In game 13 who do you think will win Seahawks or Broncos. ")
    if player_game13.lower() == "broncos":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game14=input("In game 14 who do you think will win Bears or Packers. ")
    if player_game14.lower() == "Packers":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game15=input("In game 15 who do you think will win Jets or Lions. ")
    if player_game15.lower() == "jets":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    player_game16=input("In game 16 who do you think will win Rams or Raiders. ")
    if player_game16.lower() == "rams":
        wins_player += 1
        print("Nice pick! Your points are " +str(wins_player) +". ")
    else:
        print("Awe nice try, your points are " +str(wins_player) +". ")
    return wins_player

# program starts
print("Player 1's turn.")
wins_player1=make_picks()
one = input("To exit type exit. ")
if one.lower() == "exit":
    print("Player 1 Wins!!!")
is_exit(one)
print("Player 2's turn.")
wins_player2=make_picks()
one = input("To exit type exit. ")
if one.lower() == "exit":
    higher=max(wins_player1, wins_player2)
    num_winners=0
    winners = ""
    if higher == wins_player1:
        num_winners +=1
    if num_winners > 1:
        winners +="and player 1 "
    else:
        winners +="player 1 "        
    if higher == wins_player2:
        num_winners +=1
    if num_winners > 1:
        winners +="and player 2 "
    else:
        winners +="player 2 "        
    if num_winners == 1:
        print("The winner is " +winners)
    if num_winners >= 1:
        print("The winners are " +winners)
is_exit(one)
print("Player 3's turn.")
wins_player3=make_picks()
one = input("To exit type exit. ")
if one.lower() == "exit":
    higher=max(wins_player1, wins_player2, wins_player3)
    num_winners=0
    winners = ""
    if higher == wins_player1:
        num_winners +=1
    if num_winners > 1:
        winners +="and player 1 "
    else:
        winners +="player 1 "        
    if higher == wins_player2:
        num_winners +=1
    if num_winners > 1:
        winners +="and player 2 "
    else:
        winners +="player 2 "        
    if higher == wins_player3:
        num_winners +=1
    if num_winners > 1:
        winners +="and player 3 "
    else:
        winners +="player 3 "        
    if num_winners == 1:
        print("The winner is " +winners)
    if num_winners >= 1:
        print("The winners are " +winners)
is_exit(one)
print("Player 4's turn.")
wins_player4=make_picks()
higher=max(wins_player1, wins_player2, wins_player3, wins_player4)
num_winners = 0
winners = ""
if higher == wins_player1:
    num_winners +=1
    winners +="player 1 "
if higher == wins_player2:
    num_winners +=1
    if num_winners > 1:
        winners +="and player 2 "
    else:
        winners +="player 2 "        
if higher == wins_player3:
    num_winners +=1
    if num_winners > 1:
        winners +="and player 3 "
    else:
        winners +="player 3 "        
if higher == wins_player4:
    num_winners +=1
    if num_winners > 1:
        winners +="and player 4 "
    else:
        winners +="player 4 "        
if num_winners == 1:
    print("The winner is " +winners)
if num_winners == 2:
    print("The winners are " +winners)


