from datetime import date
from datetime import datetime
from datetime import time

def main():
    today = date.today()
    print("Today's date", today)
    print("Date Components: ",today.day,today.month,today.year)

    days = ["mon","tue","wed"]
    print("which day ", days[today.weekday()])

    # time

    print("***Date Time***")
    today = datetime.now()
    print(today)

    print("***Time***")
    today = datetime.now()
    print(datetime.time(today))

if __name__ == "__main__":
    main()
