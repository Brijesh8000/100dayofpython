# Enter your height in meters e.g., 1.55
print("Enter your height and weight :  ")
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = float(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi1=float(weight/(height*height))
bmi=round(bmi1,15)
if(bmi<18.5):
  print(f"Your BMI is {bmi}, you are underweight.")
elif(25>bmi>=18.5):
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif(30>bmi>=25):
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif(35>bmi>=30):
  print(f"Your BMI is {bmi}, you are obese.")
elif(bmi>=35):
  print(f"Your BMI is {bmi}, you are clinically obese.")
  