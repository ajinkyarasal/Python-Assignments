# #Write a Python program to implement a class named Numbers with the 
# following specifications:
# The class should contain one instance variable:
#   Value
# Define a constructor (_init_) that accepts a number from the user and initializes Value.
# Implement the following instance methods:
# ChkPrime () - returns True if the number is prime,otherwise returns False
# ChkPerfect () -returns True if the number is perfect,otherwise returns False
# Factors () - displays all factors of the number
# SumFactors () - returns the sum of all factors
# (You may use this method as a helper in ChkPerfect () if required)
# Create multiple objects and call all methods.

class Numbers:
    
    def __init__(self,Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        elif self.Value == 2:
            return True
        else:
            count = 0
            for i in range(2,self.Value):
                if self.Value % i == 0:
                    count += 1
            if count > 0:
                return False
            else:
                return True
            
    def ChkPerfect(self):
        if self.Value<=0:
            return False
        else:
            divisor = 0
            for i in range(1,self.Value):
                if self.Value % i == 0:
                    divisor += i
            if self.Value == divisor:
                return True
            else:
                return False
            
    def Factors(self):
        ListOfFactors = []
        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                ListOfFactors.append(i)
        return ListOfFactors
    
    def SumFactors(self):
        ListOfFactors = self.Factors()
        sumOfFactors = 0
        for f in ListOfFactors:
            sumOfFactors += f
        return sumOfFactors
    
obj1 = Numbers(27)
print("ChkPerfect : ",obj1.ChkPerfect())
print("ChkPrime : ",obj1.ChkPrime())
print("Factors : ",obj1.Factors())
print("SumFactors : ",obj1.SumFactors())




