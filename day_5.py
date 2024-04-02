'''Day 5 '''

student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height=0
no_of_student=0
for i in student_heights:
    total_height+=i
    no_of_student+=1
print(total_height)
print(no_of_student)

average_height=total_height/no_of_student
print(round(average_height))
# fruits=["Apple","Peeach","Pear"]
# for fruit in fruits:
#     print(fruit)