#1.Write a program which accepts two numbers and prints addition, subtraction,
#  multiplication and division.

def arithmaticOperations(No1, No2):
    div = 0
    add = No1 + No2
    sub = No1 - No2
    mult = No1 * No2
    if (No2 >0):
        div = No1 / No2
    return add,sub,mult,div

def main():
    add,sub,mult,div = arithmaticOperations(20,10)
    print("Addition is : ",add)
    print("Subtraction is : ",sub)
    print("Multiplication is : ",mult)
    print("Division is : ",div)
    
    
if __name__ == "__main__":
    main()
