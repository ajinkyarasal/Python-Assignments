#5. Write a program which accepts one number and prints all odd numbers till that number.

def OddNum(No):
    evenList = []
    for i in range(1,No+1):
        if i%2 == 1 :
            evenList.append(i)
    return evenList


def main():
    Result = OddNum(10)
    print(Result)

if __name__ == "__main__":
    main()