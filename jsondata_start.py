
import urllib.request
import json

def main():
    printRes('{"name":"test1"}')

def printRes(data):
    thejson = json.loads(data)
    if "name" in thejson:
        print(thejson["name"])

if __name__=="__main__":
    main()