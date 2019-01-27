"""
twenty_questions

Description:
"""
answer=input("What should the other player try to guess? (lower-case letters only, please) ")
print("\n" * 100)
num_guess=20
while num_guess > 0:
    guess=input("Player 2, what is your guess? (all lower-case letters) ")
    if guess == answer:
        print("You guessed it! Congrats!")
        break
    else:
        num_guess -= 1
        print("Sorry, that's not the right answer.")
        if num_guess > 0:
            print("You have " +str(num_guess) +" guesses remaining")
            print()
            input("Player 2, ask Player 1 a yes-or-no question about their thing. (Hit enter once they've answered.)")
            print()
if num_guess==0:
    print("Sorry, your guesses are up. You didn't get it.")
    print("The object was: " +answer)
