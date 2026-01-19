#Write a program which accepts radius of circle and prints area of circle.
import math

def areaOfCircle(radius):
    return math.pi * (radius ** 2)


def main():
    Result = 0
    Result = areaOfCircle(radius = 12)
    print("Area of circle is : ", Result)
    
 
if __name__ == "__main__":
    main()