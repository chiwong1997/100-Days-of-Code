# Concepts: Control Flow (if-else), Conditional Statements
# Nested if-else Statements, Logical Operators 

name1 = "Angela Yu"
name2 = "Jack Bauer"

true_count = 0
true_count += name1.lower().count("t")
true_count += name2.lower().count("t")

true_count += name1.lower().count("r")
true_count += name2.lower().count("r")

true_count += name1.lower().count("u")
true_count += name2.lower().count("u")

true_count += name1.lower().count("e")
true_count += name2.lower().count("e")

love_count = 0
love_count += name1.lower().count("l")
love_count += name2.lower().count("l")

love_count += name1.lower().count("o")
love_count += name2.lower().count("o")

love_count += name1.lower().count("v")
love_count += name2.lower().count("v")

love_count += name1.lower().count("e")
love_count += name2.lower().count("e")

print(true_count)
print(love_count)

love_score = int(str(true_count) + str(love_count))
print(love_score)
print(type(love_score))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

