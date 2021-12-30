# Declare Variables

#f="1"
#print("this is string "+ f)

f=0
#print("this is a integer" + str(f))

def newFunction():
    global f
    f="def"
    print(f)

newFunction()
print(f)

del f
print(f )