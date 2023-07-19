# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
import calendar

def calender(year,month,date):
    input_date = datetime.date(year, month, date)
    day = calendar.day_name[input_date.weekday()].upper()
    print(day)
    return day


