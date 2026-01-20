#7.Write a lambda function using filter () which accepts a list of strings and returns a list of strings having length greater than 5

def main():
    Result = []
    Data = ["cat","rat","lion","monkey","cheetah"]
    Result = list(filter(lambda a : len(a)>5 , Data))
    print(Result)

if __name__ == "__main__":
    main()
