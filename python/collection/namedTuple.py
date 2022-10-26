from collections import namedtuple

teacher=namedtuple("Teacher",["name","age","part"])

t1=teacher("khan",22,"cs")

print(t1.name)
print(t1.age)
print(t1.part)

# methods

li=["khan",21,"WHO"]
l=teacher._make(li)
print(l.name)
print(l.age)
print(l.part)



print(t1._asdict())
