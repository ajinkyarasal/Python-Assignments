#Write a program which accept one number and display below pattern.
#Input :5
#Output :   *   *   *   *   *
#           *   *   *   *
#           *   *   *
#           *   *
#           *
def printPattern(No):
    for i in range(1,No+1):
        for j in range(i,No + 1):
            print("*",end=" ")
            i += 1
        print()

def main():
    No = int(input("Enter a number : "))
    printPattern(No)

if __name__ == "__main__":
    main()