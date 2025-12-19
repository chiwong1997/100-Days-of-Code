# Errors and Catching Exceptions

# try - execute something that might catch an exception
# except - do this if there was an exception
# else - do this if there is no exceptions
# finally - do this no matter what happens, exception or not

# Common Errors: FileNotFound, KeyError, IndexError, TypeError

from pathlib import Path
BASE_DIR = Path(__file__).parent
file_path_dir = BASE_DIR / "a_file.txt"

try:
    with open(file_path_dir) as data_file:
        data_file.read()
    a_dictionary = {"key":"value"}
    print(a_dictionary["non-existent-key"])
except FileNotFoundError:
    # This block will only execute if the try block fails with a FileNotFoundError
    with open(file_path_dir, "w") as data_file:
        data_file.write("Created this file 12345")
except KeyError as error_message:
    # This block will only execute if the try block fails with a KeyError
    print(f"The key {error_message} does not exist.")
else:
    # This block will only execute if the try block is successful 
    with open(file_path_dir) as data_file:
        content = data_file.read()
        print(content)
finally:
    # This is not usually used, but can be useful sometimes
    print("This runs no matter what - we can close the file, but since we use with, don't need to")

##### Raising our own exceptions
# use the raise keyword 
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 metres")

bmi = weight/height ** 2
print(bmi)