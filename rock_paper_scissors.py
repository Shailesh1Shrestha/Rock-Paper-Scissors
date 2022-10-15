import random

option = ["Rock", "Paper", "Scissors"]
computer = random.choice(option)

user = False
cpu_score = 0
user_score = 0
while True:
    user = input("Rock, Paper or Scissors? ").capitalize()
    if user == computer:
        print("Tie!")
    elif user == "Rock":
        if computer == "Paper":
            print("You lose! ", computer, "covers ", user)
            cpu_score += 1
        else:
            print("You win! ", user, "smashes ", computer)
            user_score += 1

    elif user == "Paper":
        if computer == "Scissors":
            print("You lose! ", computer, "cut ", user)
            cpu_score += 1
        else:
            print("You win! ", user, "covers ", computer)
            user_score += 1

    elif user == "Scissors":
        if computer == "Rock":
            print("You lose! ", computer, "smashes ", user)
            cpu_score += 1
        else:
            print("You win! ", user, "cut ", computer)
            user_score += 1

    elif user == "End":
        print("Final Scores: ")
        print(f"CPU: {cpu_score}")
        print(f"User: {user_score}")
        break
