#Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
#Thread 2 should calculate and display the minimum element from the same list.
#The list should be accepted from the user

import threading
def CalculateMaximum(intList):
    print("Max number is : ",max(intList))
def CalculateMinimum(intList):
    print("Min number is : ",min(intList))
def main():
    ListSize = int(input("Enter list size : "))
    Data = []
    for i in range(ListSize):
        Data.append(int(input()))
    print("User input is : ",Data)

    t1 = threading.Thread(target=CalculateMaximum,args=(Data,))
    t2 = threading.Thread(target=CalculateMinimum,args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("End of main.")


if __name__ == "__main__":
    main()
        