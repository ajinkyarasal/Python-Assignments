#Write a program which accepts length and width of rectangle and prints area.


def areaOfRectagle(length,width):
    return length * width

def main():
    Result = 0.0
    Result = areaOfRectagle(length=30,width = 20)
    print("Length of rectangle is : ",Result)
 
if __name__ == "__main__":
    main()