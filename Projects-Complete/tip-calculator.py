"""
Tip Calculator 
Concepts: F strings, data type manipulation, F Strings

"""
print("Welcome to the tip calculator")
bill = input("What was the total bill?\n")
tip = input("How much (%) do you want to tip?\n")
num_people = input("How many people are splitting the bill?\n")

pre_tip = float(bill)/int(num_people)
post_tip = round(pre_tip * (1 + float(tip)/100), 2)
print(f"Everyone pays ${post_tip}") 