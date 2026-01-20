#4.Write a lambda function using reduce () which accepts a list of numbers and returns the addition of all elements.
from functools import reduce

def main():
    Result = None
    Data = [10,20,30,40,50]
    Result = reduce(lambda a,b : a+b,Data)
    print(Result)

if __name__ == "__main__":
    main()