def game():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    
    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    
    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    
    #Write your code below this line 👇
    import random
    user_choice=input("Enter your choice (Rock / paper /scissor : ")
    user_choice_lower=user_choice.lower()
    print(user_choice_lower)
    
    computer_choice=random.randint(0,2)  
    if computer_choice==0 and user_choice_lower=="paper":
      print(f"computer choice is {rock} and user choice is {paper} \n user won")
    elif computer_choice==0 and user_choice_lower=="scissor":
      print(f"computer choice is {rock} and user choice is {scissors} \n computer won")
    elif computer_choice==1 and user_choice_lower=="rock":
      print(f"computer choice is {paper} and user choice is {rock} \n computer won")
    elif computer_choice==1 and user_choice_lower=="scissor":
      print(f"computer choice is {paper} and user choice is {scissors} \n user won")
    elif computer_choice==2 and user_choice_lower=="rock":
      print(f"computer choice is {scissors} and user choice is {rock} \n user won")
    elif computer_choice==2 and user_choice_lower=="paper":
      print(f"computer choice is {scissors} and user choice is {paper} \n computer won")
    else:
      print("draw")
    

while True:
  game()