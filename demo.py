import pandas as pd
import datetime

"""
1-5-2021
1-10-2021
"""
# date1 = '5-1-2021'
# date2 = '10-1-2021'
# date1 = datetime.datetime.strptime('1-5-2021', '%d-%m-%Y')
# date2 = datetime.datetime.strptime('1-10-2021', '%d-%m-%Y')
# mydates = pd.date_range(date1, date2).tolist()
# for i in mydates:
#     d = datetime.date.strftime(i, '%d-%m-%Y')
#     print(d)


d = datetime.date.today()
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
