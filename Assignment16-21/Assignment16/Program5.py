#Write a program which display 10 to 1 on screen.
#Output : 10 9 8 7 6 5 4 3 1
def printNum():
    for i in range (1,11):
        print(i,end="\t")
    print()

def main():
    printNum()

if __name__ == "__main__":
    main()