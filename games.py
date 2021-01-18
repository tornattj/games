# Jacob Tornatta 3/7/20

import random

money = 100 # money that the player starts with

print("Games: coinflip, cho han, cards") # initial greetings
print("You start with $100")

def vibe_check(): # function that checks how much money the player has, exits if money <= 0

    global money # money must be a global variable to play with it in a function

    if money <= 0:
        print("You don't have enough money to play! Goodbye.")
        exit() # exits the game if the player doesn't have enough cash
    else:
        print("You have $" + str(money) + " to play with.") # if the player has enough $, prints the amount

def coin_flip(guess, bet): # coin flipping game that checks guess and bet

    global money

    num = random.randint(1,2) # 1 = heads, 2 = tails

    if guess == "heads":
        guess = 1
    elif guess == "tails":
        guess = 2
    else:
        main()

    if num == guess and num == 1:
        print("You flipped heads, you win! $" + str(bet) + " will be added to your money.")
        money += bet
        main()
    elif num == guess and num == 2:
        print("You flipped tails, you win! $" + str(bet) + " will be added to your money.")
        money += bet
        main()
    else:
        print("You guessed incorrectly! $" + str(bet) + " will be subtracted from your money.")
        money += (-bet)
        main()

def cho_han(guess, bet):

    global money

    num1 = random.randint(1,6)
    num2 = random.randint(1,6)

    if guess == "odd" and num1 + num2 % 2 != 0:
        print("You guessed odd, you win! $" + str(bet) + " will be added to your money.")
        money += (bet)
        main()
    elif guess == "odd" and num1 + num2 % 2 == 0:
        print("You guessed incorrectly! $" + str(bet) + " will be subtracted from your money.")
        money += (-bet)
        main()
    elif guess == "even" and num1 + num2 % 2 == 0:
        print("You guessed even, you win! $" + str(bet) + " will be added to your money.")
        money += bet
        main()
    elif guess == "even" and num1 + num2 % 2 != 0:
        print("You guessed incorrectly! $" + str(bet) + " will be subtracted from your money.")
        money += (-bet)
        main()
    else:
        main()

def cards(bet):

    global money

    num1 = random.randint(1,52)
    num2 = random.randint(1,52)
    opp_bet = random.randint(1,100)

    print("Opponent bets $" + str(opp_bet))

    if num1 > num2:
        money += bet
        money += opp_bet
        print("You picked a card higher than your opponent! $" + str(bet) + " and $" + str(opp_bet) + " will be added to your money.")
        main()
    elif num1 < num2:
        money += (-bet)
        money += (-opp_bet)
        print("Your opponent picked a higher card, you lose $" + str(bet) + " and $" + str(opp_bet))
        main()
    else: # if num1 isn't bigger than num2 and visa versa, they must be equal
        print("You and your opponent picked the same card! Tie game!")
        main()

def main():

    input1 = input("Enter a game to play: ")

    if input1 == "exit":
        print("Good game! You ended with $" + str(money) + ".")
        exit()
    elif input1 == "money":
        print("You have $" + str(money))
        main()
    elif input1 == "coinflip":
        input2 = input("Heads or tails: ")
        input3 = int(input("Enter bet: "))
        vibe_check()
        coin_flip(input2, input3)
    elif input1 == "cho han":
        input2 = input("Odd or even: ")
        input3 = int(input("Enter bet: "))
        vibe_check()
        cho_han(input2, input3)
    elif input1 == "cards":
        input2 = int(input("Enter bet: "))
        vibe_check()
        cards(input2)
    else:
        main()
main()

def exit():
    print("")
