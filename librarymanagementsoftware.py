#Library Management Software=Write a library class with no. of books and books as two instance variables.Write a program to create a library class and show how you can print all books and get the no of books using different methods.
class Library:
    def __init__(self):
        self.noofBooks=0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noofBooks=len(self.books)
    def showInfo(self):
        print(f"The library has listed books that are {self.books} \n and \nTotal are {self.noofBooks} no. of books")
        for book in self.books:
            print(book)
l1=Library()
l1.addBook("Harry Potter")
l1.addBook("Twilight")
l1.addBook("Ever have I ever")
l1.addBook("Mary go round")
l1.showInfo()
