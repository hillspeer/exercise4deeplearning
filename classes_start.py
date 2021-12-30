
class myClass():
    def method(self):
        print("myClass method1")
    def method2(self, anotherstring):
        print("myClass method2", anotherstring)

class anotheClass(myClass):
    def method(self):
        myClass.method(self)
        print("another Class method1")
    def method2(self, anotherstring):
        print("another Class method2", anotherstring)

def main():
    c=myClass()
    c.method()
    c.method2("test string")

    c2 = anotheClass()
    c2.method()
    c2.method2("another string")

if __name__ == "__main__":
    main()
