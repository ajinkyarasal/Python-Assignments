#Write a lambda function which accepts one number and returns True if number is odd otherwise False.
def main():
    oddNum = lambda No : No % 2 != 0
    print(oddNum(31))

if __name__ == "__main__":
    main()