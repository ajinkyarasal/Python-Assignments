#9.Write a lambda function using reduce () which accepts a list of numbers and 
# returns the product of all elements.

from functools import reduce

def main():
    Result = None
    Data = [23,32,34,35,66]
    Result = reduce(lambda a,b : a*b,Data)
    print(Result)
if __name__ == "__main__":
    main()
