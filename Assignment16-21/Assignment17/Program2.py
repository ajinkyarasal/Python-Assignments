#Write a program which accept one number and display below pattern.
# * * * * *
# * * * * *  
# * * * * *  
# * * * * *  
# * * * * * 

def patternPrinting(No):
    for _ in range(No):
        for _ in range(6):
            print("*" , end="   ")
        print()

def main():
    patternPrinting(5)
if __name__ == "__main__":
    main()