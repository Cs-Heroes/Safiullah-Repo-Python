from collections import OrderedDict

dic=OrderedDict()
dic[1]="khan"
dic[2]="karim"
dic[3]="lala"
dic[4]=5
print(dic)

# when we delete an element

dic.pop(2)
print("after deleting:")

print(dic)

dic[2]="new element"
print("new element is added: ")
print(dic)