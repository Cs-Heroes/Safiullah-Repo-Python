import math
class Books:
    def addBook(self):
        print("---- BOOK REGISTRATION ----")
        self.name=input("Enter book name: ")
        self.pages=int(input("Enter book pages: "))
        self.author=input("Enter author name: ")
        self.publishYear=input("Enter publish year: ")
        bookFile=open("books.txt",'a')
        bookFile.write(self.name+"\n")
        bookFile.write(str(self.pages)+"\n")
        bookFile.write(self.author+"\n")
        bookFile.write(self.publishYear+"\n")
        bookFile.close()

    def booksDetails(self):
        bookFile=open("books.txt",'r')
        allBooks=bookFile.readlines()
        bookFile.close()
        d=0
        number=1
        print("---- BOOKS DETAILS ----")
        print("=====================")
        print("Book Number ("+str(number)+")")
        print("=====================")
        for i in range(math.floor(len(allBooks)/4)):
            print("book name: "+allBooks[d])
            print("+++++++++++++++++++++\n")
            print("pages: "+allBooks[d+1])
            print("+++++++++++++++++++++\n")
            print("author: "+allBooks[d+2])
            print("+++++++++++++++++++++\n")
            print("publish year: "+allBooks[d+3])
            number+=1
            print("=======================")
            print("Book Number ("+str(number)+")")
            print("=======================\n")
            d+=4


    def booksList(self):
        bookFile=open("books.txt",'r')
        allBooks=bookFile.readlines()
        bookFile.close()
        d=0
        print("=======================")
        print("Books in libarary")
        print("=======================")
        for i in range(math.floor(len(allBooks)/4)):
            print("\nbook name: "+allBooks[d])
            print("++++++++++++++++++++++")
            d+=4
        print("=======================")
        print("libarary books end")
        print("=======================")

    def removeBook(self):
        bookFile=open("books.txt",'r')
        allBooks=bookFile.readlines()
        bookFile.close()
        removeBook=input("Enter name of book to remove: ")
        removeBook=removeBook+"\n"
        try:
            removeBookIndex=allBooks.index(removeBook)
            allBooks.remove(removeBook)
            allBooks.pop(removeBookIndex)
            allBooks.pop(removeBookIndex)
            allBooks.pop(removeBookIndex)
            bookFile=open("books.txt",'w')
            for i in allBooks:
                bookFile.write(i)
        except ValueError:
            print("we haven't such book\npleace try agian")
    
    def 

        

class Student:
    def addStudent(self):
        self.id=int(input("Enter student id: "))
        self.name=input("Enter student name: ")
        self.lastName=input("Enter student last name: ")
        self.phone=input("phone number:")
        students=open("students.txt",'a')
        students.write(str(self.id)+"\n")
        students.write(self.name+"\n")
        students.write(self.lastName+"\n")
        students.write(self.phone+"\n")
        students.close()

    def allStudentsDetials(self):
        studentFile=open("students.txt",'r')
        allStudents=studentFile.readlines()
        d=0
        print("\n\n========================")
        print("+++ students details +++")
        print("========================\n")

        for i in range(math.floor(len(allStudents)/4)):
            print("student id: "+allStudents[d])
            print("student name: "+allStudents[d+1])
            print("studebt last name "+allStudents[d+2])
            print("phone number "+allStudents[d+3])
            
            print("=======================")
            d+=4



    def removestudent(self):

        studentFile=open("students.txt",'r')
        allStudents=studentFile.readlines()
        studentFile.close()
        removeStudent=input("Enter name of Student to remove: ")
        removeStudent=removeStudent+"\n"
        try:


            removeStudentIndex=allStudents.index(removeStudent)
       
            allStudents.remove(removeStudent)
            allStudents.pop(removeStudentIndex-1)
            allStudents.pop(removeStudentIndex)
            allStudents.pop(removeStudentIndex)
            studentsFile=open("students.txt",'w')
            for i in allStudents:
                studentsFile.write(i)
        except ValueError:
            print("we haven't student by this name\npleace try agian")





# std=Student()
# # std.addStudent()
# std.allStudentsDetials()
# std.removestudent()
        
# # book=Books()
# # book.booksDetails()


def library():
    book=Books()
    student=Student()
    print("============================")
    print("++++will come to library++++")
    print("============================")
    
    
    while True:
        print("=======================")
        print("+++Library Main Page+++")
        print("=======================")
        print("1. Books: ")
        print("2. Students: ")
        print("0. Exit")
        chooice=int(input("Select:"))
        if(chooice==1):
             while True:

                print("\n\n\nWhat do you want:\n1. add book:\n2. Books details:\n3. Books list:\n4. Remove book: \n0. for exit")
                select=int(input("select: "))
                print("\n\n")

                if select==1:
                    book.addBook()
                elif select==2:
                    book.booksDetails()
                elif select==3:
                    book.booksList()
                elif select==4:
                    book.removeBook()
                else:
                    break
        elif chooice==2:
            while True:
                print("\n\n\nWhat do you want:\n1. add Student:\n2. Students details:\n4. Remove Students: \n0. for exit: ")
                select=int(input("select: "))
                print("\n\n")
                if(select==1):
                    student.addStudent()
                elif select==2:
                    student.allStudentsDetials
                elif select==3:
                    student.removestudent()
                elif select==0:
                    break




        elif chooice==0:
            exit()



   

 
library()



