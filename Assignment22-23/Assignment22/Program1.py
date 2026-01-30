#Write a Python program to implement a class named Demo with the following specifications:
# *   The class should contain two instance variables: no 1 and no 2.
# *   The class should contain one class variable named Value.
# Define a constructor (init_ that accepts two parameters and initializes the instance variables.
# *   Implement two instance methods:Fun () - displays the values of instance variables no 1 and no 2.
# Gun () - displays the values of instance variables no 1 and no2.
# Create two objects of the Demo class as follows:
# Objl = Demo (11, 21)
# Obj2 = Demo (51, 101)
# Call the instance methods in the given sequence:
# Objl. Fun ( )
# Obj2 .Fun ()
# Objl. Gun ()
# Obj2. Gun ()

class Demo:
    Value = 10
    
    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2

    def Fun(self):
        print(f"Value of No1 is : {self.No1} and value of No2 is : {self.No2}")

    def Gun(self):
        print(f"Value of No1 is : {self.No1} and value of No2 is : {self.No2}")

Objl = Demo (11, 21)
Obj2 = Demo (51, 101)

Objl. Fun ( )
Obj2 .Fun ()
Objl. Gun ()
Obj2. Gun ()

