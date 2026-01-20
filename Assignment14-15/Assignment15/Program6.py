#6.Write a lambda function using reduce () which accepts a list of numbers and returns the minimum element.
from functools import reduce
def main():
    Result = None
    Data = [23,34,54,56,11]
    Result = reduce(lambda a,b : min(a,b),Data)
    print(Result)

if __name__ == "__main__":
    main()
