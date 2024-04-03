def greet():
    print("Hello")
    print("How do you do?")
    print("Annoyed")

greet()

# Adding parameters to the function 
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Chi")

# Adding a second parameter
def greet_with(name, location):
    print(f"Welcome to {location} wonderful human called {name}")

# Positional Argument
greet_with("Chi", "Hong Kong")

# Keyword Argument
greet_with(location="Hong Kong", name="Chi")

# Prime Number Checker Exercise - From Auditiorium 
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
