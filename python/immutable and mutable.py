a=12
print(id(a))
a=1
print(id(a))
b=[3,2]
print(id(b))
b[1]=3
print(id(b))

# set is mutalble

set_S={12,23,5,3}
print(id(set_S))
set_S.add(333)
print(id(set_S))


# imutable Tuple

tup=("khan",2,3,7)
# tup[3]=3 is mutable it will give error
print(id(tup))