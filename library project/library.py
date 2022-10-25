class Person:
    def __init__(self,name,lastName,phoneNumber):
        self.name=name
        self.lastName=lastName
        self.phoneNumber=phoneNumber


class Author(Person):
    def __init__(self,name,lastName,phoneNumber,job):
        Person.__init__(self,name,lastName,phoneNumber)
        self.job=job

    
class reader(Person):
    def __init__(self,name,lastName,phoneNumber):
        Person.__init__(self,name,lastName,phoneNumber)
        self.barrowedBooks=[]
    
    def getBook(self,book):
        self.barrowedBooks.append(book)



class Book:
    
    def __init__(self,name,author,publishYear,pages):
        self.name=name
        self.author=[author]
        self.publishYear=publishYear
        self.pages=pages

    




    

class Library:
    def __init__(self):

        self.books=[]
    def addBook(self):
        bookName=input("Enter Book Name: ")
        authorName=input("Enter author Name: ")
        authorLastName=input("Enter author last name: ")
        authorPhoneNumber=input("Enter author phone number: ")
        authorJob=input("Enter author job: ")
        bookPublishYear=input("Enter book publish Year: ")
        bookPages=int(input("Enter book pages: " ))
        author=Author(authorName,authorLastName,authorPhoneNumber,authorJob)
        book=Book(bookName,author,bookPublishYear,bookPages)
        self.books.append(book)

    def showBooks(self):
        for book in self.books:
            print("Book Name: "+book.name)
            for author in book.author:
                print("Author name: "+author.name)
                print("Author last name: "+author.lastName)
            print("publish year: "+book.publishYear)
            print("Book pages: "+str(book.pages))



library=Library()
library.addBook()
library.addBook()
library.showBooks()
