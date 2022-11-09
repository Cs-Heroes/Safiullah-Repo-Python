import threading


isPrint=[False]

def printFunc():
    if (isPrint[0]==False):
        print("I am safi")
        isPrint[0]=True

        
        

t1=threading.Thread(target=printFunc)
t1.start()

printFunc()




