#Design a Python application that creates two threads named Thread1 and Thread2.
#Threadl should display numbers from 1 to 50.
#Thread2 should display numbers from 50 to 1 in reverse order.
#Ensure that:Thread2 starts execution only after Thread1 has completed.
#Use appropriate thread synchronization
import threading
def print1To50():
    for i in range(1,51):
        print(i)
    print("end of print1To50 with thread : ",threading.current_thread().name)

def print50To1():
    for i in range(50,0,-1):
        print(i)
    print("end of print50To1 with thread : ",threading.current_thread().name)
def main():
    
    Thread1 = threading.Thread(target=print1To50)
    Thread2 = threading.Thread(target=print50To1)
    Thread1.start()
    Thread1.join()
    Thread2.start()

    
    Thread2.join()

    print("End of main")

if __name__ == "__main__":
    main()