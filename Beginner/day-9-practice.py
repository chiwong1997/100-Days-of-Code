# Auditorium exercise

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  if student_scores[student] > 90:
    student_grades[student] = "Outstanding"
  elif student_scores[student] > 80:
    student_grades[student] = "Exceeds Expectations"
  elif student_scores[student] > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

# Dictionary

capitals = {

    "France": "Paris",

    "Germany": "Berlin"

}

 

# Nesting a List/Dictionary in a Dictionary

travel_log = {

    "France": {"cities_visited": ["Paris", "Lille", "Dihon"], "total_visits": 12},

    "Indonesia": {"Bali": "Ubud"}

}

 

# Nesting a Dictionary in a List

new_log = [

    {

        "country":"France",

        "cities_visited": ["Paris", "Lille", "Dijon"],

       "total_visits": 12

    },

    {

        "country": "Germany",

        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],

        "total_visits": 5

    }]

 

print(new_log[1])

print(new_log[0]["country"])

 

# Auditorium Day 9 Exercise

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

# Do NOT change the code above 👆

 

# TODO: Write the function that will allow new countries

# to be added to the travel_log.

def add_new_country(country, visits, list_of_cities):

  travel_log.append({"country": country,

                     "visits": visits,

                     "cities": list_of_cities

                    }

                   )

 

# Do not change the code below 👇

add_new_country(country, visits, list_of_cities)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")

print(f"My favourite city was {travel_log[2]['cities'][0]}.")