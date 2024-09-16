import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user_choice = input("\nChoose rock, paper, or scissors (or type 'exit' to quit): ").lower()

    if user_choice == 'exit':
        print(f"Final Score - You: {user_score}, Computer: {computer_score}")
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Please choose again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Current Score - You: {user_score}, Computer: {computer_score}")
