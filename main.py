
import random
from art import logo

list = list(range(1,101))
computer_choice = random.choice(list)
game_over = False
attemps = 0

print(logo)
print("Welcome to the Number Guessing Game!")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'hard':
  attemps += 5
  print(f"You have {attemps} attemps remaining to guess the number.")
elif difficulty == 'easy':
  attemps += 10
  print (f"You have {attemps} attemps remaining to guess the number.")


while game_over == False:
  guess = int(input("Make a guess: "))
  if guess > computer_choice:
    print("Too high")
    attemps -= 1
    print (f"You have {attemps} attemps remaining to guess the number.")
    if attemps == 0:
      print("You've run out of guesses, you lose.")
      break
  if guess < computer_choice:
    print("Too low")
    attemps -= 1
    print (f"You have {attemps} attemps remaining to guess the number.")
    if attemps == 0:
      print("You've run out of guesses, you lose.")
      break
  elif guess == computer_choice:
    print("Thats it")
    break
  
    




