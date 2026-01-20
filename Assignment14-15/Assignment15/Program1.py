#1.Write a lambda function using map () which accepts a list of numbers and returns a list of squares of each number.


def main():
    Result = []
    Data = [10,20,30,40]
    Result = list(map(lambda a : a**2,Data))
    print(Result)


if __name__ == "__main__":
    main()
