tup=(12,"khan","jan",33)
print(tup)

tup2=12,3,"jalalzai"
print(tup2)

#Tuple unpacking 

a,b,c=tup2
print(a)
print(b)
print(c)
print(tup2)

# if tuple has one element we must us ,  for creationg of tuple 

newTuple=("khan")
print(type(newTuple))
newTuple=("khan",)
print(type(newTuple))

# Tuple elements accessing

print(tup[1])
print(tup[-2])


# scling on Tuple

print(tup[1:3])
print(tup[-4:-1])

# changing value of  imutalbe element in tuple

tTuple=(12,[12,3,2],"khan")
print(tTuple)
print(id(tTuple))
tTuple[1][1]="khan"
print(id(tTuple))
print(tTuple) 

# delete of tuple
print(tup2)
del tup2
# print(tup2) #it will give error becuase tuple is deleted


# mthod is of tuple

print(tup.count(12))
print(tup.index(12))

# membership testing 

print("safi" in tup)
print(222 not in tup)


# iteration on tuple

for i in tup:
    print(i)