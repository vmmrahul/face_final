import pandas as pd
import datetime
from connections import makeConnections
# """
# 1-5-2021
# 1-10-2021
# """
# # date1 = '5-1-2021'
# # date2 = '10-1-2021'
# # date1 = datetime.datetime.strptime('1-5-2021', '%d-%m-%Y')
# # date2 = datetime.datetime.strptime('1-10-2021', '%d-%m-%Y')
# # mydates = pd.date_range(date1, date2).tolist()
# # for i in mydates:
# #     d = datetime.date.strftime(i, '%d-%m-%Y')
# #     print(d)
#
#
# # d = datetime.date.today()
# # now = datetime.datetime.now()
# # current_time = now.strftime("%H:%M:%S")
#
# # s1 = '6:33:00'
# # s2 = '18:15:00'
# #
# FMT = "%H:%M:%S"
# #
# # deff = datetime.datetime.strptime(s2,FMT) - datetime.datetime.strptime(s1,FMT)
# # print(deff)
# # print()
#
# # nextTime = datetime.datetime.strptime(s2,FMT) - datetime.datetime.strptime(s1,FMT)
#
# query1= "select * from Attendance where employ='{}' ORDER BY id DESC".format(2)
# conn = makeConnections()
# cr = conn.cursor()
# cr.execute(query1)
# result = cr.fetchall()
#
#
#
# last_AttendTime = str(result[0][3]+datetime.timedelta(hours=1))
#
# # last_AttendTime = last_AttendTime.strftime("%H:%M:%S")
#
# date = datetime.date.today()
#
# now = datetime.datetime.now()
# current_time = now.strftime("%H:%M:%S")
#
# print(last_AttendTime)
# print(current_time)
# print(datetime.datetime.strptime(current_time,FMT)>datetime.datetime.strptime(last_AttendTime,FMT))
#
# # d = datetime.datetime.today() +datetime.timedelta(hours=1)
# #
# # current_time = d.strftime("%H:%M:%S")
# # print(current_time)
#
# # if date ==result[0][2]:
# #     if

# select * ,min(Attendance.timeOfRigister), max(Attendance.timeOfRigister) from Attendance GROUP by Attendance.employ , Attendance.dateOfAttendace

query = "SELECT Attendance.id, employ.name ,Attendance.employ, Attendance.dateOfAttendace, Attendance.timeOfRigister ,min(Attendance.timeOfRigister), max(Attendance.timeOfRigister) FROM `Attendance` INNER JOIN employ on employ.id=Attendance.employ GROUP by Attendance.employ , Attendance.dateOfAttendace"
conn = makeConnections()
cr = conn.cursor()
cr.execute(query)
result = cr.fetchall()


for row in result:
    print(row)
