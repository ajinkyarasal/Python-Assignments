#Create on module named as Arithmetic which contains 4 functions as Add() 
# for addition, Sub) for subtraction, Mult) for multiplication and Div) 
# for division. All functions accepts two parameters as number and 
# perform the operation. Write on python program which call all the 
# functions from Arithmetic module by accepting the parameters from user.

from Arithmetic import add
from Arithmetic import sub
from Arithmetic import mult
from Arithmetic import div


def main():
    Addition = add(10,2)
    print("Addition is : ",Addition)

    Subtraction = sub(10,2)
    print("Subtraction is : ",Subtraction)

    Multiplication = mult(10,2)
    print("Multiplication is : ",Multiplication)

    Division = div(10,2)
    print("Division is : ",Division)
if __name__ == "__main__":
    main()