#Design a Python application that creates two threads named EvenList and OddList.
#Both threads should accept a list of integers as input.
#The EvenList thread should:
#Extract all even elements from the list.
#Calculate and display their sum.
#The OddList thread should:
#Extract all odd elements from the list.
#Calculate and display their sum.
#Threads should run concurrently.
import threading
def EvenList(intList):
    print("Inside even list thread")
    sum = 0
    for n in intList:
        if n%2 ==0 :
            sum += n
    print("Even number sum : ",sum)
def OddList(intList):
    print("Inside odd list thread")
    sum = 0
    for n in intList:
        if n%2 !=0 :
            sum += n
    print("Odd number sum :",sum)

def main():
    print("Inside main")
    Data = [2,31,32,4,45,66,78,90,101]
    t1 = threading.Thread(target=EvenList,args=(Data,))
    t2 = threading.Thread(target=OddList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("End of main")

if __name__ == "__main__":
    main()