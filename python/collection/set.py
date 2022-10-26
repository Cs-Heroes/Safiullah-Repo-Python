sets={12,"khan",1,3,12} #set cannt contain mutabe objects

print(type(sets))
print(sets)

#modifing set

sets.add("jalalzai")
print(sets)

sets.update([1,2,3,4])
print(sets)

#removing 

sets.discard(12)
print(sets)
sets.remove(2)
print(sets)
print(sets.pop())
print(sets)

newSet={12,"karim",99,"khan",00,77}

print(sets|newSet)

print(sets.union(newSet))
print(sets)

print(sets&newSet)
print(sets.intersection(newSet))
print(sets-newSet)
print(sets.difference(newSet))

# other functions

s=sets.copy()
print(s)
print(sets.isdisjoint(newSet))




# iteration on sets

for i in sets:
    print(i)


# other methods

print(all(sets))
print(len(sets))
ss={12,2,34,}
print(max(ss)) 
print(sorted(ss))
print(sum(ss))
