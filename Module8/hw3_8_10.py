from datetime import datetime
date='2021-05-27 17:08:34.149Z'

def get_str_date(date):
    date_1 = datetime.strptime(date, '%d-%B-%Y').date()
    #seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
    print(date1.strftime('%A %d %B %Y')) # Tuesday 07 January 2020    



    return date_1


get_str_date(date)
    