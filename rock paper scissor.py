import random

user_hand = None
computer_hand = None
winner = None
result = None

def get_hand(num: int) -> str:
    """Get str representation of the user or the computer's hand."""
    if num == 0:
        return "rock"
    elif num == 1:
        return "paper"
    elif num == 2:
        return "scissors"

def determine_winner() -> str:
    """Get str representation of the winner."""
    user_win_combinations = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    
    if user_hand == computer_hand:
        winner = "Draw"
    elif (user_hand, computer_hand) in user_win_combinations.items():
        winner = "You"
    else:
        winner = "Computer"
    
    return winner

# take in a number 0-2 from the user that represents their choice
print("Rock = 0, paper = 1, scissors = 2")

while True:
    user_input = input("Please enter your choice: ")
    if user_input in ["0", "1", "2"]:
        break
    else:
        print("Incorrect input!")

# get str representations of user's hand and computer's hand.
user_hand = get_hand(int(user_input))
computer_hand = get_hand(random.randint(0,2))

# determine who wins
winner = determine_winner()

# print out the result
print(f"Your choice ({user_hand}) vs Computer's choice ({computer_hand})")

if winner == "Draw":
    result = "It's a draw!"
else:
    result = f"{winner} won!"

print(result)