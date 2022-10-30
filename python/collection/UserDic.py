from collections import UserDict

class CustomDic(UserDict):
    def pop(self,s=None):
        print("pop is disabled")
    
    def popitem(self,s=None):
        print("popitem is not allow")

d=CustomDic({1:1212,2:"khan"})
print(d)

d.popitem()
d.pop()