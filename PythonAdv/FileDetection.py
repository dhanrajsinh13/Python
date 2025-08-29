import os

file_path  = ".Data/test.txt"

if os.path.exists(file_path):
    print(f"The file {file_path} exists")

    if os.path.isfile(file_path):
        print(f"The file {file_path} is a file")
    elif os.path.isdir(file_path):
        print(f"The file {file_path} is a directory")
    else:
        print(f"The file {file_path} is a special file")

else:
    print(f"The file {file_path} does not exist")