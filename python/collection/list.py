print("\n\n list\n\n")

listItem=[12,"khan","jalalzai",4,12,[12,1,2]]

# list slicing
print(listItem[2:4])
print(listItem[-4:-1])
print(listItem[2:-1])

#adding element to list using index, append and extend

listItem[2]="khan"

listItem.append(555)
print(listItem)
listItem.extend([12,23,11])
print(listItem)

# * and + operators

print(listItem+[12,"khan",2])
print(listItem*2)


#insert() method

listItem.insert(2,"jalalzai")
print(listItem)
listItem[2:4]=["baba","agha","jan"]
print(listItem)

# deleting list elements

del listItem[1]
print(listItem)
del listItem[2:3]
print(listItem)
# del listItem   #for deleting list 

# remove, pop, clear methods

listItem.remove(11)
print(listItem)
listItem.pop()
print(listItem)

# listItem.clear()    # it will remove all elements of list
# print(listItem)

# Ohter Methods index, count, sort, reverse and copy

print("index of four in list:  "+str(listItem.index(4)))
print("sorted list: "+str(listItem))

v=listItem.copy()
print("list copy: "+str(v))
print("12s into list: "+str(listItem.count(12)))


# list comprehension

newList=[2**x for x in range(10) if x<7]
print(newList)


# element exists operations
print(12 in listItem)
print(12 not in listItem)

print(len(listItem))
llist=[12,3,2]
print(sorted(llist))



# listItem.append("ali")
# newList=listItem.copy()
# print("copy of listItem: "+str(newList))
# print(listItem.count(12))
# listItem.extend(newList)
# print(listItem)

# print("index of 4: "+str(listItem.index(4)))
# listItem.remove(4)
# print(listItem)

# print(listItem.reverse())

# print(listItem.sort()) elemet must be from one type