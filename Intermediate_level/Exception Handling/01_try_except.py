#try_excertion


try:  # it can execute the code 
    a = int(input("Enter first number: ")) #take iput from user 
    b = int(input("Enter second number: "))#take input from user

    result = a / b  #perform division 
    print("Result:", result) 

except Exception as e: # it can handle the error which can occures in try block
    print("An error occurred:", e)