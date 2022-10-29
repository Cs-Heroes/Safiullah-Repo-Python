def fun():
    print("I am safiullah")

fun()

# printing function as obj using print()
print("printing function using function: ")
print(fun)

#creating new reference to function

nameFun=fun
print("Calling using reference: ")
nameFun()


# pass function as argument

def function(argFun):
    print("argument function: ")
    argFun()

function(fun)


#returning function from a function

print("returnd function from a function: ")
def returnFunc():
    def func():
        print("inner function as return")
    return func


returnedfunction =returnFunc()
returnedfunction()

# lambda function

d=lambda x: x+" jalalzai"

print( "lamada function: "+d("safi"))

stringReverse=lambda x: x[::-1]

print(stringReverse("safiullah"))
