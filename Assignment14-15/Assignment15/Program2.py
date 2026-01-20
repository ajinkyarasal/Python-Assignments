#2.Write a lambda function using filter () which accepts a list of numbers and returns a list of even numbers.


def main():
    Result = []
    Data = [12,13,14,15,16]
    Result = list(filter(lambda a : a%2 ==0 ,Data))
    print(Result)


if __name__ == "__main__":
    main()
