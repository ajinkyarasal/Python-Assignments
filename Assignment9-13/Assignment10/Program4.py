#4. Write a program which accepts one number and prints all even numbers till that number.
#Input: 10
#Output: 2 4 6 8 10

def EvenNum(No):
    evenList = []
    for i in range(1,No+1):
        if i%2 == 0 :
            evenList.append(i)
    return evenList


def main():
    Result = EvenNum(20)
    print(Result)

if __name__ == "__main__":
    main()