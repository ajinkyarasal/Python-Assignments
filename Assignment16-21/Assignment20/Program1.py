# Design a Python application that creates two separate threads named Even and Odd.
#The Even thread should display the first 10 even numbers.
#The Odd thread should display the first 10 odd numbers.
#Both threads should execute independently using the threading module.
import threading
def first10EvenNum():
    print("printing even")
    for i in range(0,11):
        print(i*2)
def first10OddNum():
    print("printing odd")
    for i in range(1,11):
        print((2*i)+1)


def main():
    t1 = threading.Thread(target=first10EvenNum)
    t2 = threading.Thread(target=first10OddNum)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
