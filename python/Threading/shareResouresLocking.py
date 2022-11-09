import threading

lock=threading.Lock()
money=100

def addToMoney():
    global money
    lock.acquire()
    for i in range(100000):
        money=money + 10
    
    lock.release()


def substructFromMoney():
    global money
    lock.acquire()
    for i in range(100000):
        money= money -10
        
    lock.release()

t1=threading.Thread(target=addToMoney)
t2=threading.Thread(target=substructFromMoney)
t1.start()
t2.start()

t1.join()
t2.join()
print(money)