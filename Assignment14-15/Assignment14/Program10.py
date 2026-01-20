#9.Write a lambda function which accepts three numbers and returns largest number.

def main():
    largestOf3Num = lambda a,b,c : max(a,b,c)
    print(largestOf3Num(3,5,7))
if __name__ == "__main__":
    main()