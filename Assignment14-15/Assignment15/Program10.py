#10.Write a lambda function using filter () which accepts a list of numbers and returns the count of even numbers.
from functools import reduce
def main():
    Result = None
    Data = [2,3,4,5,6,7,8,9,11]
    FList = list(filter(lambda a : a%2==0,Data))
    print (FList)
    print(len(FList))
    
if __name__ == "__main__":
    main()
