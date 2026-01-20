#3.Write a lambda function using filter () which accepts a list of numbers and returns a list of odd numbers.

def main():
    Result = []
    Data = [11,12,13,231,443,222]
    Result = list(filter(lambda a : a%2!=0, Data))
    print(Result)

if __name__ == "__main__":
    main()
