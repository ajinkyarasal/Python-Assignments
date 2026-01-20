#8.Write a lambda function using filter () which accepts a list of numbers and returns a list of numbers 
# divisible by both 3 and 5.


def main():
    Result = []
    Data = [3,5,15,30,4,50,10,45]
    Result = list(filter(lambda a: a%3 ==0 and a%5 == 0,Data))
    print(Result)
if __name__ == "__main__":
    main()


