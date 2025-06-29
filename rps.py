import random

r = "rock"
p = "paper"
s = "scissors"

user_score = 0
computer_score = 0

while user_score < 3 and computer_score < 3:
    your_choice = input("Enter your choice (Rock, Paper, Scissors):\n").lower()
    if your_choice not in [r, p, s]:
        print("Invalid choice. Please choose one option between Rock, Paper, or Scissors.")
        continue
    if your_choice == r:
        print("You chose Rock.")
    elif your_choice == p:
        print("You chose Paper.")
    elif your_choice == s:
        print("You chose Scissors.")
    computer_choice = random.choice([r, p, s])
    print(f"Computer chose: {computer_choice}")
    print("Let's see who wins!")
    if your_choice == computer_choice:
        print("It's a tie!")
    elif (your_choice == r and computer_choice == s) or \
         (your_choice == p and computer_choice == r) or \
         (your_choice == s and computer_choice == p):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1
    print(f"Your score: {user_score}, Computer score: {computer_score}")

if user_score == 3:
    print("Congratulations! You won the game!")
else:
    print("Sorry, the computer won the game.")