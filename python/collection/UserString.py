from collections import UserString

class CustomString(UserString):
    def append(self,s=None):
        print("append is called")

    def remove(self,s=None):
        print("remove is called")


s=CustomString("khan")
print("String is: "+s)
s.append()
s.remove()
