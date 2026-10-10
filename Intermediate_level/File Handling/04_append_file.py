#append file

with open("demo.txt", "a") as file: #the file in append mode
    file.write("\nWelcome to Python!")

print("Data added successfully")