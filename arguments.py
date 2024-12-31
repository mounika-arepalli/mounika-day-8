def pw(x,y):
    z=x**y
    print(z)
pw(5,2)
#keyword arguments
def show(name,age):
    print(name,age)
show(name="kumar",age=62)
#default arguments
def show(name,age=27):
    print(name,age)
show(name="raam",age=62)