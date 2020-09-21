import random

money = 100


#Write your game of chance functions here


# Coin Flip function
def coin_flip(guess, bet):

    print("\nFlip a coin!")    
    
    flip = random.randint(1, 2)

    if bet <= 0 or bet > money:
        print("\nYour bet is invalid.")
    elif flip == 1 and guess.lower() == "heads":
        print("\nHeads! You win $" + str(bet))
        return bet
    elif flip == 2 and guess.lower() == "tails":
        print("\nTails! You win $" + str(bet))
        return bet
    else:
        print("\nYour guess was incorrect. You've lost $" + str(bet))
        return -bet


# Chō-han
# The game uses two standard six-sided dice, which are shaken in a bamboo cup or bowl by a dealer. 
# The cup is then overturned onto the floor. Players then place their wagers on whether the sum 
# total of numbers showing on the two dice will be "Chō" (even) or "Han" (odd). The dealer then 
# removes the cup, displaying the dice. The winners collect their money. 

def cho_han(guess, bet):

    print("\nTime to play Cho-han!")

    dice_1 = random.randint (1, 6)
    dice_2 = random.randint (1, 6)

    if bet <= 0 or bet > money:
        print("\nYour bet is invalid.")
    elif (dice_1 + dice_2) % 2 == 0 and guess.lower == "even":
        print("\nEven! You win $" + str(bet))
        return bet
    elif (dice_1 + dice_2) % 2 != 0 and guess.lower == "odd":
        print("\nOdd! You win $" + str(bet))
        return bet
    else:
        print("\nYour guess was incorrect. You've lost $" + str(bet))
        return -bet


# Pick a card

def draw_card(guess, bet):

    print("\nPick a card!")

    card_1 = random.randint (1, 13)
    card_2 = random.randint (1, 13)


    if bet <= 0 or bet > money:
        print("\nYour bet is invalid.")
    elif card_1 > card_2 and guess.lower() == "higher":
        print("\nHigher! You win $" + str(bet))
        return bet
    elif card_1 < card_2 and guess.lower() == "lower":
        print("\nLower! You win $" + str(bet))
        return bet
    elif card_1 == card_2:
        print("\nTie! Nobody wins.")
        return 0
    else:
        print("\nYour guess was incorrect. You've lost $" + str(bet))
        return -bet


# Roulette
# Included bet types: even or odd (0 or 00 loses here), specific number

def spin_wheel(guess, bet):

    print("\nSpin the roulette wheel!")

    roulette_numbers = [00] + list(range(37))
    spin = random.choice (roulette_numbers)

    if bet <= 0 or bet > money:
        print("\nYour bet is invalid.")
    elif spin == 0 or 00 and guess.lower() == "even" or "odd":
        print("\nYour guess was incorrect. You've lost $" + str(bet))
        return -bet
    elif spin % 2 == 0 and guess.lower() == "even":
        print("\nEven! You win $" + str(bet))
        return bet
    elif spin % 2 !=0 and guess.lower() == "odd":
        print("\nEven! You win $" + str(bet))
        return bet
    elif spin == guess:
        print("\nYou guessed the exact number! You win $" + str(bet * 35))
        return bet * 35
    else:
        print("\nYour guess was incorrect. You've lost $" + str(bet))
        return -bet


#Call your game of chance functions here

try:
    money += coin_flip("Heads", 20)
except:
    TypeError
print("\nYour current balance is $" + str(money))

try:
    money += cho_han("Even", 50)
except:
    TypeError
print("\nYour current balance is $" + str(money))

try:
    money += draw_card("Higher", 10)
except:
    TypeError    
print("\nYour current balance is $" + str(money))

try:
    money += spin_wheel("Odd", 25)
except:
    TypeError
print("\nYour current blaance is $" + str(money))
