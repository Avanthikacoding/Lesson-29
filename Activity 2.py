"""Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!"""
class Employee:
    def __init__(self):
        print("Onject created")
    def __del__(self):
        print("Object destroyed")
def Create_obj():
    print("Making an object...")
    obj = Employee
    print("Deleting the object...")
    return obj
o1 = Create_obj()
