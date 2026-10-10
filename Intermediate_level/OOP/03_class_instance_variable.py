#class and instance varibale

class Student: #class name
    school = "ABC School"  # Class variable

    def __init__(self, name): #creating instance variable
        self.name = name   # Instance variable

s1 = Student("Gaurav")
s2 = Student("Amar")

print(s1.name)
print(s2.name)

print(s1.school)
print(s2.school)