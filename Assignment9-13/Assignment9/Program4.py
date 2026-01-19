#4. Write a program which accepts one number and prints cube of that number.


def CalculateCube(No):
    return No ** 3
def main():
    Result = 0
    Result = CalculateCube(5)
    print(Result)
if __name__ == "__main__":
    main()