dic={1:"safiullah", 2: "khan", "ali":5}
print(dic)

# accessing 

print(dic[1])
print(dic.get("ali"))

# adding element to dictionary

dic[2]="jalalzai"
print(dic)
dic["safi"]="jan"
print(dic)

# removing elements from dictionary

dic.pop("ali")
print(dic)
dic.popitem()
print(dic)

# dic.clear()      #it will delete all elements
# print(dic)

# del dic          #it delete dictionary
# print(dic)


# other methods

newDic =dic.copy()
print(newDic)

myDic={}.fromkeys(["safi",2,"jalalzai",6],0)
print(myDic)


for item in dic.items():
    print(item)


print(dic.setdefault(4))


obj=dic.values()
print(obj)

ndic={x:x*x for x in range(5)}
print(ndic)

# element checking is or not in dic

print(2 in dic)
print(3 not in dic)
print(3 in dic)

# other functions
print("_____________")
print(all(dic))
print(any(dic))
print(len(dic))
print(sorted(dic))