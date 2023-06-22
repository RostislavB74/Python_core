from datetime import datetime
date='2021-05-27 17:08:34.149Z'


def get_str_date(date):

    data= date.split(' ')
    
    date_1 = datetime.strptime(data[0], '%Y-%m-%d').date()
    
    #print(date_1.strftime('%A %d %B %Y')) # Tuesday 07 January 2020    


    return date_1.strftime('%A %d %B %Y')


get_str_date(date)
    
    
    
