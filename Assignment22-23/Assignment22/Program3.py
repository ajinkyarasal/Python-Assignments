#Write a Python program to implement a class named Arithmetic with the following characteristics:
# • The class should contain two instance variables: Valuel and Value2.
# * Define a constructor (_init_ that initializes all instance variables to O.
# * Implement the following instance methods:Accept () - accepts values for Valuel and Value2 from the user.
# * Addition () - returns the addition of Valuel and Value2.
# * Subtraction () - returns the subtraction of Value1 and Value2.
# * Multiplication () - returns the multiplication of Value1 and Value2.Division () - returns the division of Valuel and Value2 (handle division by zero properly).
# * Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic():
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self,No1,No2):
        self.Value1 = No1
        self.Value2 = No2
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return 0
        
obj1 = Arithmetic()
obj1.Accept(12,4)
print("Addition is : ",obj1.Addition())
print("Subtraction is : ",obj1.Subtraction())
print("Multiplication is : ",obj1.Multiplication())
print("Division is : ",obj1.Division())

obj2 = Arithmetic()
obj2.Accept(16,3)
print("Addition is : ",obj2.Addition())
print("Subtraction is : ",obj2.Subtraction())
print("Multiplication is : ",obj2.Multiplication())
print("Division is : ",obj2.Division())


    

