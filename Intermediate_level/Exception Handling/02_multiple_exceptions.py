#Multiple exceptions handling 

try: # it can exeute the code
    a = int(input("Enter first number: ")) #take input from user
    b = int(input("Enter second number: ")) #take input from user 

    print(a / b)

except ValueError:
    print("Please enter numbers only!")

except ZeroDivisionError: #handles division by zero
    print("You cannot divide by zero!")

print("Program finished") #it can run after when all errors can handle