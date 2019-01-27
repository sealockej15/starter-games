"""
Pokemon_cards_2

Description:
"""
import random

pokemon=""
Boosters_bought=0
Rainbow = 0
Mega=0
EX=0
Stage_2=0
Stage_1=0
Common=0
money=50
exit="no"
while money > 0 and exit.lower() != "yes":
    print("You have " +str(money) +" dollars.")
    buy=input("Do you want 1 guaranteed Mega and Ex and 6 booster packs for 50 dollars(To get this answer mega) or 1 guarenteed Ex and 1 guaranteed stage 2 and 3 booster packs for 18 dollars (To get this answer Ex) or 1 guaranteed stage 2 and 1 guaranteed stage 1 and 1 booster pack for 10 dollars(To get this enter 2) (if you don't want any press enter) ").lower()
    if buy == "mega":
        if money < 50:
            print("You don't have enough money.")
        else:
            EX += 1
            Mega += 1
            Boosters_bought += 6
            money -= 50
    elif buy == "ex":
        if money < 18:
            print("You don't have enough money.")
        else:
            EX += 1
            Stage_2 += 1
            Boosters_bought += 3
            money -= 18
    elif buy == "2":
        if money < 10:
            print("You don't have enough money.")
        else:
            Stage_2 += 1
            Stage_1 += 1
            money -= 10
            Boosters_bought += 1
    if money >= 3:
        booster=input("Do you want a 10 card booster pack for 3 dollars? ")
        if booster == "yes":
            Boosters=int(input("How many? "))
            while money < Boosters * 3:
                print("You don't have enough money. ")
                Boosters=int(input("How many? "))
            Boosters_bought += Boosters
            money -= 3 * Boosters
    if Boosters_bought > 0:
        count = 10 * Boosters_bought
        while count > 0:
            Booster_pokemon=random.randint(0,1001)
            if Booster_pokemon == 0:
                Rainbow += 1
                count = 0
                print("OH MY GOD I GOT A RAINBOW RARE!!!!!")
            elif Booster_pokemon == 2 or Booster_pokemon == 250 or Booster_pokemon == 500 or Booster_pokemon == 750 or Booster_pokemon == 1000:
                Mega += 1
                count -= 1
                print("Mega!!!")
            elif Booster_pokemon >= 100 and Booster_pokemon < 250:
                Stage_1 += 1
                count -= 1
                print("Stage 1")
            elif Booster_pokemon >= 15 and Booster_pokemon < 100:
                Stage_2 += 1
                count -= 1
                print("Stage 2")
            elif Booster_pokemon >= 2 and Booster_pokemon <= 14:
                EX += 1
                count -= 1
                print("EX")
            elif Booster_pokemon == 1001:
                print("OH MY GOD I GOT A RAINBOW RARE!!!!!")
                Boosters_bought=0
                Rainbow = 0
                Mega=0
                EX=0
                Stage_2=0
                Stage_1=0
                Common=0              
                money=0
                count=0
                pokemon += "TROLLED!!!"
            else:
                Common += 1
                count-=1
                print("Common")
        Boosters_bought = 0
    while Rainbow > 0:
        Which_Rainbow_Pokemon=random.randint(1,16)
        if Which_Rainbow_Pokemon == 1:
            pokemon +=", RAINBOW RARE MEGA CHARIZARD X!!!"
        if Which_Rainbow_Pokemon == 2:
            pokemon +=", RAINBOW RARE MEGA Charizard Y!!!"
        if Which_Rainbow_Pokemon == 3:
            pokemon +=", RAINBOW RARE MEGA VENASAUR!!!"
        if Which_Rainbow_Pokemon == 4:
            pokemon +=", RAINBOW RARE MEGA BLASTOISE!!!"
        if Which_Rainbow_Pokemon == 5:
            pokemon +=", RAINBOW RARE MEGA BLAZIKEN!!!"
        if Which_Rainbow_Pokemon == 6:
            pokemon +=", RAINBOW RARE MEGA SWAMPERT!!!"
        if Which_Rainbow_Pokemon == 7:
            pokemon +=", RAINBOW RARE MEGA SCEPTILE!!!"
        if Which_Rainbow_Pokemon == 8:
            pokemon +=", RAINBOW RARE MEGA TYRANITAR!!!"
        if Which_Rainbow_Pokemon == 9:
            pokemon +=", RAINBOW RARE MEGA SALAMENCE!!!"
        if Which_Rainbow_Pokemon == 10:
            pokemon +=", RAINBOW RARE MEGA GARCHOMP!!!"
        if Which_Rainbow_Pokemon == 11:
            pokemon +=", RAINBOW RARE MEGA LUCARIO!!!"
        if Which_Rainbow_Pokemon == 12:
            pokemon +=", RAINBOW RARE MEGA METAGROSS!!!"
        if Which_Rainbow_Pokemon == 13:
            pokemon +=", RAINBOW RARE MEGA AGRON!!!"
        if Which_Rainbow_Pokemon == 14:
            pokemon +=", RAINBOW RARE MEGA GENGAR!!!"
        if Which_Rainbow_Pokemon == 15:
            pokemon +=", RAINBOW RARE MEGA GALADE!!!"
        if Which_Rainbow_Pokemon == 16:
            pokemon +=", RAINBOW RARE SUPER WOOPER DUPER"
        Rainbow -= 1
    while Mega > 0:
        Which_Mega_pokemon=random.randint(1,15)
        if Which_Mega_pokemon == 1:
            pokemon +=", Mega Charizard X"
        if Which_Mega_pokemon == 2:
            pokemon +=", Mega Charizard Y"
        if Which_Mega_pokemon == 3:
            pokemon +=", Mega Venasaur"
        if Which_Mega_pokemon == 4:
            pokemon +=", Mega Blastoise"
        if Which_Mega_pokemon == 5:
            pokemon +=", Mega Blaziken"
        if Which_Mega_pokemon == 6:
            pokemon +=", Mega Swampert"
        if Which_Mega_pokemon == 7:
            pokemon +=", Mega Sceptile"
        if Which_Mega_pokemon == 8:
            pokemon +=", Mega Tyranitar"
        if Which_Mega_pokemon == 9:
            pokemon +=", Mega Salamence"
        if Which_Mega_pokemon == 10:
            pokemon +=", Mega Garchomp"
        if Which_Mega_pokemon == 11:
            pokemon +=", Mega Lucario"
        if Which_Mega_pokemon == 12:
            pokemon +=", Mega Metagross"
        if Which_Mega_pokemon == 13:
            pokemon +=", Mega Agron"
        if Which_Mega_pokemon == 14:
            pokemon +=", Mega Gengar"
        if Which_Mega_pokemon == 15:
            pokemon +=", Mega Galade"
        Mega -= 1
    while EX > 0:
        Which_EX_pokemon=random.randint(1,15)
        if Which_EX_pokemon == 1:
          pokemon +=", Charizard EX"
        if Which_EX_pokemon == 2:
          pokemon +=", Charizard EX"
        if Which_EX_pokemon == 3:
          pokemon +=", Venasaur EX"
        if Which_EX_pokemon == 4:
          pokemon +=", Blastoise EX"
        if Which_EX_pokemon == 5:
          pokemon +=", Blaziken EX"
        if Which_EX_pokemon == 6:
          pokemon +=", Swampert EX"
        if Which_EX_pokemon == 7:
          pokemon +=", Sceptile EX"
        if Which_EX_pokemon == 8:
          pokemon +=", Tyranitar EX"
        if Which_EX_pokemon == 9:
          pokemon +=", Salamence EX"
        if Which_EX_pokemon == 10:
          pokemon +=", Garchomp EX"
        if Which_EX_pokemon == 11:
          pokemon +=", Lucario EX"
        if Which_EX_pokemon == 12:
          pokemon +=", Metagross EX"
        if Which_EX_pokemon == 13:
          pokemon +=", Agron EX"
        if Which_EX_pokemon == 14:
          pokemon +=", Gengar EX"
        if Which_EX_pokemon == 15:
          pokemon +=", Galade EX"
        EX -= 1
    while Stage_2 > 0:
        Which_Stage_2_pokemon=random.randint(1,15)
        if Which_Stage_2_pokemon == 1:
          pokemon +=", Charizard"
        if Which_Stage_2_pokemon == 2:
          pokemon +=", Charizard"
        if Which_Stage_2_pokemon == 3:
          pokemon +=", Venasaur"
        if Which_Stage_2_pokemon == 4:
          pokemon +=", Blastoise"
        if Which_Stage_2_pokemon == 5:
          pokemon +=", Blaziken"
        if Which_Stage_2_pokemon == 6:
          pokemon +=", Swampert"
        if Which_Stage_2_pokemon == 7:
          pokemon +=", Sceptile"
        if Which_Stage_2_pokemon == 8:
          pokemon +=", Tyranitar"
        if Which_Stage_2_pokemon == 9:
          pokemon +=", Salamence"
        if Which_Stage_2_pokemon == 10:
          pokemon +=", Garchomp"
        if Which_Stage_2_pokemon == 11:
          pokemon +=", Machamp"
        if Which_Stage_2_pokemon == 12:
          pokemon +=", Metagross"
        if Which_Stage_2_pokemon == 13:
          pokemon +=", Agron"
        if Which_Stage_2_pokemon == 14:
          pokemon +=", Gengar"
        if Which_Stage_2_pokemon == 15:
          pokemon +=", Galade"
        Stage_2 -= 1
    while Stage_1 > 0:
        Which_Stage_1_pokemon=random.randint(1,15)
        if Which_Stage_1_pokemon == 1:
          pokemon +=", Charmeleon"
        if Which_Stage_1_pokemon == 2:
          pokemon +=", Charmeleon"
        if Which_Stage_1_pokemon == 3:
          pokemon +=", Ivysaur"
        if Which_Stage_1_pokemon == 4:
          pokemon +=", Wartortle"
        if Which_Stage_1_pokemon == 5:
          pokemon +=", Combusken"
        if Which_Stage_1_pokemon == 6:
          pokemon +=", Marshtomp"
        if Which_Stage_1_pokemon == 7:
          pokemon +=", Grovyle"
        if Which_Stage_1_pokemon == 8:
          pokemon +=", Pupitar"
        if Which_Stage_1_pokemon == 9:
          pokemon +=", Shelgon"
        if Which_Stage_1_pokemon == 10:
          pokemon +=", Gabite"
        if Which_Stage_1_pokemon == 11:
          pokemon +=", Machoke"
        if Which_Stage_1_pokemon == 12:
          pokemon +=", Metang"
        if Which_Stage_1_pokemon == 13:
          pokemon +=", Lairon"
        if Which_Stage_1_pokemon == 14:
          pokemon +=", Haunter"
        if Which_Stage_1_pokemon == 15:
          pokemon +=", Kirlia"
        Stage_1 -= 1
    while Common > 0:
        Which_Common_pokemon=random.randint(1,15)
        if Which_Common_pokemon == 1:
          pokemon +=", Charmander"
        if Which_Common_pokemon == 2:
          pokemon +=", Charmander"
        if Which_Common_pokemon == 3:
          pokemon +=", Bulbasaur"
        if Which_Common_pokemon == 4:
          pokemon +=", Squirtle"
        if Which_Common_pokemon == 5:
          pokemon +=", Torchic"
        if Which_Common_pokemon == 6:
          pokemon +=", Mudkip"
        if Which_Common_pokemon == 7:
          pokemon +=", Treeko"
        if Which_Common_pokemon == 8:
          pokemon +=", Larvitar"
        if Which_Common_pokemon == 9:
          pokemon +=", Bagon"
        if Which_Common_pokemon == 10:
          pokemon +=", Gible"
        if Which_Common_pokemon == 11:
          pokemon +=", Machop"
        if Which_Common_pokemon == 12:
          pokemon +=", Beldum"
        if Which_Common_pokemon == 13:
          pokemon +=", Aron"
        if Which_Common_pokemon == 14:
          pokemon +=", Gastly"
        if Which_Common_pokemon == 15:
          pokemon +=", Ralts"
        Common -= 1
    exit=input("Do you want to exit yes or no? ")
    if exit.lower() == "yes":
        break
print("You got:" +pokemon)  









