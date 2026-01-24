#Design a Python application that creates three threads named Small, Capital, and Digits.
#All threads should accept a string as input.
#  The Small thread should count and display the number of lowercase characters.
#The Capital thread should count and display the number of uppercase characters.
#The Digits thread should count and display the number of numeric digits.Each thread must also display:
#Thread ID
#Thread Name

import threading

def Small(username):
    count = 0
    for c in username:
        if c.islower():
            count +=1
    print("Total lower characters : ",count)

def Capital(username):
    count = 0
    for c in username:
        if c.isupper():
            count +=1
    print("Total upper characters : ",count)
def Digit(username):
    count = 0
    for c in username:
        if c.isdigit():
            count +=1
    print("Total digit characters : ",count)

def main():
    username = "JohnDoe123"

    t1 = threading.Thread(target=Small,args=(username,))
    t2 = threading.Thread(target=Capital,args=(username,))
    t3 = threading.Thread(target=Digit,args=(username,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("End of main")
    

if __name__ == "__main__":
    main()