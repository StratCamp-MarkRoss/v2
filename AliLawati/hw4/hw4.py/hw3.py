# 1: User Defined Functions
# 1. Create a function that accepts a string and returns a list containing four items. 
# The items in the list should be: [the original string, 
# an integer which is a count of the amount of vowels contained within that string, 
# the vowels from the string (e.g. ‘aoi’),  the original string with the vowels removed]

def try_string(input):
    # counting vowels
    vowels_total=sum(1 for char in input if char.lower() in 'aeiou')
    # collecting vowels
    vowels=''.join(char for char in input if char.lower()in 'aeiou')
    # Original with no vowels
    string_no_vowels=''.join(char for char in input if char.lower()not in 'aeiou')
    return(input,vowels_total,vowels,string_no_vowels)

try_string("Hello World")
# or
result=try_string("Hello World")
print(result)


# 2. Create a fixed-coupon bond pricer function.
# Please see the attached Excel sheet for the math logic behind achieving the bond price.
# Function Inputs: Notional Value, Period Size ,Rate, Coupon (as a percent of Notional Value), 
# Term (amount of years – for example, if there are 3 years and period size is ½ there will be 6 periods)

# USER INPUTS
import math

Notional = float(input("Enter Notional Amount: "))
Rate = float(input("Enter Rate: ")) / 100
Expiration = float(input("Enter Years Until Expiry: "))
PeriodsPerYear = int(input("How Many Payments in Each Year?: "))

Increment = (1 / PeriodsPerYear)
Price = 0

# SUMS THE PVS OF THE COUPONS
for i in range(1, int(PeriodsPerYear * Expiration) + 1):
    Price += Coupon * (math.exp(-Rate * Increment * i))

Price += Notional * (math.exp(-Rate * Expiration))

# Function Output: “Bond Price: $X.XX”

print("Bond Price: $", round(Price, 2))


# 2: Modules
# 1. Use the built-in python random module, to create a game of dice where there are two user inputs. 
# Each user gets to enter their name and then two numbers between 1 and 6 are randomly generated. 
# The total of both die are added up and the user with the highest total number wins. 
# The output of the function/game should be each user’s name on a separate line with their results followed by:
# a final winner output such as:
# Jim’s score: 7
# Sam’s score: 3
# Jim wins!

from random import randint
def dice_game():

# players names & their random scores:

    player1=input("Enter the player1 name:")
    player2=input("Enter the player2 name:")


    score1=randint(1, 6)+randint(1,6)
    score2=randint(1, 6)+randint(1,6)

    print(f"{player1}'s score: {score1}")
    print(f"{player2}'s score: {score2}")

# check if total of both die are added up and the user with the highest total number wins.

    if score1>score2:
        print(f"{player1} wins")
    elif score2>score1:
        print(f"{player2} wins!")
    else:
        print("it's a tie")
    
        

# Run the game
dice_game()
