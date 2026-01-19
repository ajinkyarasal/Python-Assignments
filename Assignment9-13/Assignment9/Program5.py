#5. Write a program which accepts one number and checks whether it is divisible by 3 and 5

def DivisibilityTest3And5(No):
    if No == 0:
        return True
    elif No % 3 == 0 and No % 5 == 0:
        return True
    else:
        return False


def main():
    Result = False
    Result = DivisibilityTest3And5(105)
    if Result:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")
if __name__ == "__main__":
    main()
