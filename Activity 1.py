"""Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented."""
class IOString:
    def __init__(self):
        self.str1 = ""

    def getstring(self):
        self.str1 = input("Enter the string")

    def details(self):
        print("The entered string in uppercase is " , self.str1.upper())
obj = IOString()
obj.getstring()
obj.details()
