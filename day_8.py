'''paramiter means name of the argumant
 and argumant ment actual values in which is passing in the function
 '''
# 
# def greet_with_name(name,location):
#     print(f"Hello {name} ")
#     print(f"What is it like in {location}?  ")

# greet_with_name("Brijesh","chhatarpur")



'''paint Area calculator'''

# import math

# coverage = 5
# def paint_calc(height, width,cover):
#   no_of_cans=(height*width)/cover
#   print(no_of_cans)
#   print(round(no_of_cans))
  
#   print(f"You'll need {math.ceil(no_of_cans)} cans of paint.")
# i=0
# while True:
#   test_h = int(input()) # Height of wall (m)
#   test_w = int(input()) # Width of wall (m)
#   paint_calc(test_h,test_w,coverage)
#   i+=1

'''prime no'''
def prime_checker(number):
  is_prime = True
  m=number%2
  print(m)
  for i in range(2, number):
    print(i)
    
    
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    
# Your code above this line 👆
n = int(input()) # Check this number
prime_checker(n)