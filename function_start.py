
def func1():
    print("i am a function")

def func2(arg1,arg2):
    print(arg1," ",arg2)

def cube(x):
    return x*x*x

def power(num,x=1):
    result=1
    for i in range(x):
        result = result*num
    return result

def multi_arg(*args):
    result=0
    for x in args:
        result = result+x
    return result

print(multi_arg(2,3,4))

#func1()
#print (func1())
#print(func1)

func2(10,20)
print(func2(10,20))
print(cube(3))
print(power(2,3))