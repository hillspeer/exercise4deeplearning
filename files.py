
def main():

    #f = open("textfilr.txt", "a")

    #for i in range(5,10):
    #    f.write("this is line..."+ str(i) + "\r\n")

    #f.close()

    f = open("textfilr.txt","r")

    #content = f.read()

    #print(content)

    f1 = f.readlines()
    for x in f1:
        print(x)
main()