from collections import deque

li=["khan",20,"jalalzai",55000,100000]
Nqeue=deque(li)
print(Nqeue)

# deque methods

Nqeue.append("safi")
print(Nqeue)

Nqeue.appendleft("karim")
print(Nqeue)

Nqeue.pop()
print(Nqeue)

Nqeue.popleft()
print(Nqeue)