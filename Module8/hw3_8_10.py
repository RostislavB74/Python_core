# import collections
# from decimal import Decimal as dc
from datetime import datetime
date = '2021-05-27 17:08:34.149Z'


def get_str_date(date):
    data_list = date.split(" ")
    # data_str = data_list[0]
    print(data_list[0])
    datetime.date_1 = datetime.strptime(data_list[0], '%d %B %Y')
    # seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
    # print(date.strftime('%A %d %B %Y'))  # Tuesday 07 January 2020

    return datetime.date_1


get_str_date(date)
# start_unix = datetime(1970, 2, 2)
# print(start_unix.timestamp())
# print(datetime.fromtimestamp(0))

# for i in range(20):
#     print(datetime.now())
# print(dc(0.1))
