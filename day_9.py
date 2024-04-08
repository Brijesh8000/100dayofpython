''' Dicrionary '''


# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# programming_dictionary["loop"]="The action of doing something over and over again"

# print(programming_dictionary)    
# empty_dictionary={}
# programming_dictionary["Bug"]="A moth in your computer"
# print(programming_dictionary)
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

'''Nested list and Dictionary'''


##Python Dictionaries

# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.", 
#   "Function": "A piece of code that you can easily call over and over again.",
# }

# #Retrieving items from dictionary.
# # print(programming_dictionary["Function"])

# #Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# #Create an empty dictionary.
# empty_dictionary = {}

# #Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# #Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# # print(programming_dictionary)

# #Loop through a dictionary
# # for key in programming_dictionary:
# #   print(key)
# #   print(programming_dictionary[key])

# #######################################

# #Nesting 
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }

# #Nesting a List in a Dictionary

# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# #Nesting Dictionary in a Dictionary

# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

# #Nesting Dictionaries in Lists

# travel_log = [
# {
#   "country": "France", 
#   "cities_visited": ["Paris", "Lille", "Dijon"], 
#   "total_visits": 12,
# },
# {
#   "country": "Germany",
#   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 5,
# },
# ]

'''Task 23 '''

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Your code here 👇
def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")