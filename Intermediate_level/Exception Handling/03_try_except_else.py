# using if else with try exception 

age = int(input("tell your age: ")) #Take input from user 
try: 

    if age < 10 or age >18: # it checks the codition
        raise ValueError("Your age must be between 10 and 18")  # it allow you to deliberately generate an error
    else: # it can run if the condion is false
        print("welcome to the club")

except Exception as err:  # this line can catch the error which can happen in try block
    print(f"an error occured as {err}")
print("the clube will start soon")