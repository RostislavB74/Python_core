from datetime import datetime, timedelta
date='2020-10-09'

def get_days_from_today(date):
    date_1 = datetime.strptime(date, '%Y-%m-%d').date()
    print(date_1)
    #date_list=date.split('-')
    #year=date_list[0]
    #month = date_list[1]
    #day= date_list[2]
    
    current_datetime = datetime.now()
    difference = current_datetime.date() - date_1
    return difference.days    
print(get_days_from_today(date))
    
