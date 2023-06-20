from datetime import date

def get_days_in_month(month, year, day=1):
    if month ==12:
            date_1=date(year, month, 1)
            date_2=date(year+1, month-11, 1)
            delta=date_2-date_1
            #print(delta)
            return delta.days
    if month!=0 and month<12:
        month1 = month
        month2= month+1
        date_1=date(year, month1, 1)
        date_2=date(year, month2, 1)
        delta=date_2-date_1

        return delta.days
        
month =12
year = 2021
print(get_days_in_month(month, year))
        