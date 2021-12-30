def main():
    x=0

    while(x<5):
        print(x)
        x=x+1
    
    for x in range(5,10):
        print(x)
    days=["Mon","tue","Wed","thur","Fri","sat","Sun"]
    for x in days:
        if(x=="Fri"): break
        print(x)
    
    # continue in python
    for x in days:
        if(x=="Fri"): continue
        print(x)

    quaterMonths=["Jan","Feb","Mar"]

    for i,m in enumerate(quaterMonths):
        print(i,m)

if __name__ == "__main__":
    main()