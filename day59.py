#Decorators
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx
@greet
def hello():
    print("hello world")
def add(a, b):
    print(a+b)
    

hello()
#add(1,2)
greet(add)(1,2)
