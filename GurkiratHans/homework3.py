# Question 1a of homework 3
def four_item_string(input_string):
    
    # Initialize variables to store results
    original_string = input_string
    vowel_count = 0
    vowels = ""
    string_without_vowels = ""

    # Define the set of vowels
    vowel_set = set("aeiouAEIOU")

    # Iterate through each character in the input string
    for letter in input_string:
        # Check if the character is a vowel
        if letter in vowel_set:
            vowel_count += 1
            vowels += letter
        else:
            string_without_vowels += letter

    # Create a list with the desired items
    result_list = [original_string, vowel_count, vowels, string_without_vowels]

    return result_list

# Example usage:
input_str = "Hello, World!"
result = four_item_string(input_str)
print(result)


# Question 1b of homework 3
def bond_pricer(notional_value, period_size, rate, coupon, term):
    # Calculate the number of periods
    num_periods = int(term / period_size)

    # Calculate the discount factor for each period
    discount_factors = [(1 + rate * period_size) ** -n for n in range(1, num_periods + 1)]

    # Calculate the present value of future cash flows
    present_value = sum([coupon * notional_value * period_size * df for df in discount_factors])

    # Add the present value of the notional value at maturity
    present_value += notional_value * discount_factors[-1]

    # Format the output string
    bond_price = f"Bond Price: ${present_value:.2f}"

    return bond_price

# Example usage:
notional = 1000
period_size = 0.5
rate = 0.05
coupon = 0.04  # 4% as a decimal
term = 3

result = bond_pricer(notional, period_size, rate, coupon, term)
print(result)


#Question 2 of homework 3

import random

def dice_game():
    # Get user names
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    # Roll dice for each player
    player1_score = random.randint(1, 6) + random.randint(1, 6)
    player2_score = random.randint(1, 6) + random.randint(1, 6)

    # Display each player's score
    print(f"{player1_name}'s score: {player1_score}")
    print(f"{player2_name}'s score: {player2_score}")

    # Determine the winner
    if player1_score > player2_score:
        print(f"{player1_name} wins!")
    elif player1_score < player2_score:
        print(f"{player2_name} wins!")
    else:
        print("It's a tie!")

# Run the dice game
dice_game()
