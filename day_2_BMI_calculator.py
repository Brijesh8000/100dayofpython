# 1st input: enter height in meters e.g: 1.65
height = float(input())
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi=weight/(height*height)
final_bmi=round(bmi)
print(final_bmi)