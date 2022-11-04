# class Person:
#     def __init__(self,name,lastName,phoneNumber,email):
#         self.name=name
#         self.lastName=lastName
#         self.phoneNumber=phoneNumber
#         self.email=email


# class Author(Person):
#     def __init__(self,name,lastName,phoneNumber,email,job):
#         Person.__init__(self,name,lastName,phoneNumber,email)
#         self.job=job

    
# class reader(Person):
#     def __init__(self,name,lastName,phoneNumber):
#         Person.__init__(self,name,lastName,phoneNumber)
#         self.barrowedBooks=[]
    
#     def getBook(self,book):
#         self.barrowedBooks.append(book)



# class Book:
    
#     def __init__(self,name,author,publishYear,pages):
#         self.name=name
#         self.author=[author]
#         self.publishYear=publishYear
#         self.pages=pages

    




    

# class Library:
#     def __init__(self):

#         self.books=[]
#     def addBook(self):
#         bookName=input("Enter Book Name: ")
#         authorName=input("Enter author Name: ")
#         authorLastName=input("Enter author last name: ")
#         authorPhoneNumber=input("Enter author phone number: ")
#         authorEmail=input("Enter author email: ")
#         authorJob=input("Enter author job: ")
#         bookPublishYear=input("Enter book publish Year: ")
#         bookPages=int(input("Enter book pages: " ))
#         author=Author(authorName,authorLastName,authorPhoneNumber,authorEmail,authorJob)
#         book=Book(bookName,author,bookPublishYear,bookPages)
#         self.books.append(book)

#     def showBooks(self):
#         for book in self.books:
#             print("Book Name: "+book.name)
#             for author in book.author:
#                 print("Author name: "+author.name)
#                 print("Author last name: "+author.lastName)
#             print("publish year: "+book.publishYear)
#             print("Book pages: "+str(book.pages))



# library=Library()


# print("Enter 1 to add the book")
# print("Enter 2 to show the book")
# choice=int(input("Select: "))

# if (choice==1):
#     library.addBook()

# elif(choice==2):
#     library.showBooks()

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if __name__ == "__main__":
    centraLibrary = Library(["JavaScript", "PHP", "C++", "Python", "Java"])
    student = Student()
    
    while(True):
        welcomeMsg = '''\n====== Welcome to Simple Library  System======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing our Library.")
            exit()
        else:
            print("Invalid Choice!")

        