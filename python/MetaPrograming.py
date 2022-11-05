def docFunction(func):
    def inner():
        print("decorated")
        func()
    return inner




@docFunction
def function():
    print("my function")



function()