#Write a lambda function using reduce () which accepts a list of numbers and returns the maximum element.
from functools import reduce

def main():
    Result = None
    Data = [12,13,14,15,16,15]
    Result = reduce(lambda a,b : max(a,b),Data)
    print(Result)


if __name__ == "__main__":
    main()