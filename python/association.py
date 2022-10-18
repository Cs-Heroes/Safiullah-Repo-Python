print("\n\nassociation\n\n")
print("\n\naggrecation And composition\n\n")
class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name


class Department:
    def __init__(self,name,id):
        self.id=id
        self.name=name

        # composition concept-----------------------------


        self.defualtStudent=Student(0,"everyOne")
        self.student=[self.defualtStudent]
    def addStudent(self,stud):

        # Aggregation concept-----------------------------
        self.student.append(stud)

    def departmentDetails(self):
        print("id: "+str(self.id))
        print("Name:"+self.name)
        for std in self.student:
            print("Id  :  "+str(std.id))
            print("Name:  "+std.name)
            print("______________________\n")







std=Student(1,"safiullah")
std2=Student(2,"khan")
dpt=Department('cs',1)
dpt.addStudent(std)
dpt.addStudent(std2)
dpt.departmentDetails()






