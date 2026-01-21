#Write a program which accept number from user and check whether that number is positive or negative or zero.
#Input : 11
#Input : -8
#Input : 0
#Output : Positive Number
#Output : Negative Number
#Output : Zero

def NumCheck(No):
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else :
        print("Zero")

def main():
    NumCheck(11)
    NumCheck(-8)
    NumCheck(0)

if __name__ == "__main__":
    main()