# List Comprehension
# new_list = [new_item for item in list]

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