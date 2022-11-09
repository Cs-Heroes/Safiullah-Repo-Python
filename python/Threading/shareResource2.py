import threading 
money = 100


def addMoney(): 
    global money
    for i in range(100000):
        money = money + 10



def subsMoney(): 
    global money
    for i in range(100000):
        money = money - 10


thread1 = threading.Thread(target = addMoney)
thread2 = threading.Thread(target = subsMoney)


thread1.start() 
thread2.start()


thread1.join()
thread2.join()


print(money)