#Write a lambda function which accepts one number and returns True if number is even otherwise False.

def main():
    evenNum = lambda No : No % 2 ==0
    print(evenNum(7))

if __name__ == "__main__":
    main()