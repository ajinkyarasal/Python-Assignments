#Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display
import threading

def sumOfElements(intList):
    sum = 0
    for n in intList:
        sum += n
    print("sum of elements is : ",sum)

def productOfElements(intList):
    product = 1
    for n in intList:
        product *= n
    print("product of element is : ",product)
def main():
    Data = [3,4,3,2,5]
    t1 = threading.Thread(target=sumOfElements,args=(Data,))
    t2 = threading.Thread(target=productOfElements,args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()