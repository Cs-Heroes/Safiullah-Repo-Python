import sys
lin=[12,2,'a']
try:
    s='k'
    d=int(s)

except (ZeroDivisionError,NameError):
    print("sdd",sys.exc_info()[0])
except ValueError:
    print("value error")



# raise keyword
a=0
try:
    if(a<=0):
        raise ZeroDivisionError("value is zero or small then zero")

except ZeroDivisionError as va:
    print(va)


# else  in Eception handling
b=0
try:
    10/2
except:
    print("value is zero")
else:
    if(b==0):
        b=b+1
    else:
        b=-(b)
    print("else block result: "+str(b))



# finaly in exceptions
print("\n\nfinally\n\n")

try:
    file=open("k.txt")
except:
    print("file is note found")
finally:
    print("finally block is executed")


# user define exeptions

print("\n\nuser define exceptions\n\n")

class myExe(Exception):
    def ExeptionDetails(self):
        print("My Exception")


try:
    if(int(value)):
        raise myExe
except myExe as a:
    a.ExeptionDetails()





