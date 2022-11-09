import threading

def print33():
    for i in "aaaaaaaaaa":
        print(i)

def print44():
    for i in "bbbbbbbbbbb":
        print(i)



t1=threading.Thread(target=print33)
t2=threading.Thread(target=print44)
t1.start()
t2.start()