import json
import csv

txt_data = "I love Python"
list_data = {"Name": "John", "Age": 25, "City": "New York"}
file_path = "Data/test1.txt"
file_path2 = "Data/test2.json"
file_path3 = "Data/test3.csv"

try:
    with open(file_path, "w") as file:
        file.write(txt_data)
        print("File created successfully")

    with open(file_path2, "w",encoding="utf-8") as file:
        json.dump(list_data,file)
        print("File created successfully")

    with open(file_path3, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age"])
        writer.writerow(["John", 25])
        writer.writerow(["Mary", 22])
except FileExistsError:
    print("File already exists")