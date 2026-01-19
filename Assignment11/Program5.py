#5. Write a program which accepts one number and checks whether it is palindrome or not.
#Input: 121
#Output: Palindrome
from Program4 import reverse

def main():
    No = 1221
    Reverse = reverse(No)
    if No == Reverse:
        print("The number is Pallindrome")
    else:
        print("The number is not a Pallindrome")
    
    
if __name__ == "__main__":
    main()
