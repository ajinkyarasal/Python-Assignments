#Write a program which display first 10 even numbers on screen.
#Output : 2 4   6   8   10  12  14  16  18  20


def print10EvenNumber():
    for i in range(1,11):
        print(i,end="   ")
    print()
def main():
    print10EvenNumber()
if __name__ == "__main__":
    main()