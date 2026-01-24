# Design a Python application where multiple threads update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.


import threading

dayCount = 1
lObj = threading.Lock()
def updateDayCount():
    global dayCount
    for _ in range(200000):
        with lObj:
            dayCount += 1
def main():
    t1 = threading.Thread(target=updateDayCount)
    t2 = threading.Thread(target=updateDayCount)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    global dayCount
    print("Value of dayCount : ",dayCount)

if __name__ == "__main__":
    main()
