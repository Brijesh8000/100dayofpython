'''No gaddi program '''
# import random

# def number_gassig(): 
#     computer=random.randint(1,50)
#     print(computer)
#     condition=0
#     while condition<5:
#         user=int(input("Chose the no : "))
#         if computer==user:
#             print("you wine ")
#             return
#         elif 40<=computer<50:
#             print("Your Gassing No is False : chose inbetween 40 to 50")
#         elif 30<=computer<40 and 0<=user<50:
#             print("Your Gassing No is False : chose inbetween 30 to 40")

#         elif 20<=computer<30 and 0<=user<50:
#             print("Your Gassing No is False : chose inbetween 20 to 30")
#         elif 10<=computer<20 and 0<=user<50:
#             print("Your Gassing No is False : chose inbetween 10 to 20")
#         elif 0<=computer<10 and 0<=user<50:
#             print("Your Gassing No is False : chose inbetween 0 to 10")
#         else:
#             print("Invalid no : ")
#         condition+=1
# number_gassig()



from random import randint
from day_12_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

