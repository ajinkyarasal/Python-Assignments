#Design a Python application that creates two threads named EvenFactor and OddFactor.
#Both threads should accept one integer number as a parameter.
#The EvenFactor thread should:Identify all even factors of the given number.
# Calculate and display the sum of even factors.
#The OddFactor thread should:Identify all odd factors of the given number.
# Calculate and display the sum of odd factors.
#After both threads complete execution, the main thread should display the message:"Exit from main"
import threading
def EvenFactors(No):
    sum = 0
    for i in range(1,No+1):
        if No % i == 0 and i%2 ==0:
            sum += i
    print("Sum of even factors : ",sum)

def OddFactors(No):
    sum = 0
    for i in range(1,No+1):
        if No % i == 0 and i%2 !=0:
            sum += i
    print("Sum of odd factors : ",sum)

def main():
    t1 = threading.Thread(target=EvenFactors, args=(26,))
    t2 = threading.Thread(target=OddFactors,args=(26,))

    

    t1.start()
    t2.start()
    print("Exit form main")

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()