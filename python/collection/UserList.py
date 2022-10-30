from collections import UserList

class CustomList(UserList):
    def remove(self,s=None):
        print("removing from this list is desibled")

    def pop(self,s=None):
        print("pop element")


listOf=CustomList([12,23,44,"kahn"])
print(listOf)
listOf.pop()
listOf.remove()