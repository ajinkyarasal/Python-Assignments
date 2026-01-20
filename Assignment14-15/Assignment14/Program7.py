#6.Write a lambda function which accepts one number and returns True if divisible by 5.

def main():
    DivisibilityTestOf5 = lambda No : No % 5 == 0
    print(DivisibilityTestOf5(55))
if __name__ == "__main__":
    main()
