import random
# List & Dictionary Comprehension
# general format = new_list = [new_item for item in list]

numbers = [1,2,3,4,5]
add_one = [number + 1 for number in numbers]
squared_numbers = [number ** 2 for number in numbers]
print(add_one)
print(squared_numbers)

name = 'Chi'
new_list = [letter for letter in name]
print(new_list)

new = [number * 2 for number in range(1,5)]
print(new)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [n for n in names if len(n) <= 4]
print(short_names)

long_names = [n.upper() for n in names if len(n)>4]
print(long_names)

# CODING EXERCISE - output all numbers in file 1 that are in file 2
# -----------------------------------------------------------------------
# file 1 (string of integers all on separate line)
# 3
# 6
# 5
# 8
# 33
# 12
# 7
# 4
# 72
# 2
# 42
# 13
# file 2 (sting of integers all on separate line)
# 3
# 6
# 13
# 5
# 7
# 89
# 12
# 3
# 33
# 34
# 1
# 344
# 42

# actual code
# with open('file1.txt') as f1:
#     f1_str = f1.readlines()

# with open('file2.txt') as f2:
#     f2_str = f2.readlines()

# results = [int_str for int_str in f1_str if int_str in f2_str]

# result = [int(n) for n in results]

# dictionary comprehension format
# new_dict = {new_key:new_value for item in list if x}
# new_dict  {new_key:new_value for (key,value) in dict.items() if x}

students_scores = {student: random.randint(1,100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 50}
print(passed_students)

# iterate over a pandas data frame
import pandas as pd
student_dict = {
    'student': ["Angela", "James", "Lily"],
    'score' : [56, 76, 88]
}

student_df = pd.DataFrame(student_dict)

# dictionary comprehension to convery df to dict: {row.key:row.value for (index, row) in df.iterrows()}

for (index, row) in student_df.iterrows():
    print(row)

for (index, row) in student_df.iterrows():
    print(row.student)

for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)