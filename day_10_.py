'''peramiterize function '''

# def name(f_name,l_name):
#     f_n=f_name.title()
#     l_n=l_name.title()

#     print(f" {f_n} {l_n} ")

# while True:
#     name1=input("Enter First name ")
#     last=input("Enter the last name : ")
#     name(name1,last)

'''Leap year AND No of day in a month'''

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1] 
# Your code above 
year = int(input("Enter the Year : ")) # Enter a year
month = int(input("Enter the month : ")) # Enter a month
days = days_in_month(year, month)
print(days)