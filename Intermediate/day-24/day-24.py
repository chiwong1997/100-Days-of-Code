from pathlib import Path

BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / "my_file.txt"
file_path_2 = BASE_DIR / "my_second_file.txt"

# read files

with file_path.open(mode="r") as file:
    contents = file.read()
    print(contents)

# write files (overwrite)

with file_path.open(mode="w") as file:
    file.write("New text")

# append files (write without overwrite)

with file_path.open(mode="a") as file:
    file.write("\nmore and more next text.")

# if you open a file in write mode when the file doesn't exist, the file will be created 

with file_path_2.open(mode="w") as file:
    file.write("This file is created for you from scratch." \
    "\nThis is some good stuff.")

# File paths and directories
# Paths are just ways to get to a file
# wd (Working directory) is the folder we are currently working in - we can use the relative file path 
# to access our files eg. 
# absolute file path: /root/Work/Project/talk.ppt 
# relative file path assuming we are in the Project folder: ./talk.ppt
# and then if we want to access a doc in the previous folder: ../report.doc

