#Write a Python program to implement a class named Bookstore with the following specifications:

# • The class should contain two instance variables:
# Name (Book Name)
# Author (Book Author)
# * The class should contain one class variable:NoOfBooks (initialize it to 0)
# * Define a constructor (
# _init__ that accepts Name and Author and initializes instance variables.
# * Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
# * Implement an instance method:Display () - should display book details in the format:<BookName> by <Author>. No of books:
# <No0fBooks>
class Bookstore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        Bookstore.NoOfBooks +=1

    def Display(self):
        print(f"{self.Name} by  {self.Author} No. of book {Bookstore.NoOfBooks}")

obj1 = Bookstore("Linux System Programming", "Robert Love")
obj1.Display()
    
obj2 = Bookstore("C Programming", "Dennis Ritchie")
obj2.Display()