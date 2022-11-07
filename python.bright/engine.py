from ast import Str
import calendar
#create a plain text calendar
c =calendar.TextCalendar(calendar.THURSDAY)
Str = c.formatmonth(2025,1,0,0)
print(str)

# #create an html formatted calender
# hc=calendar.HTMLCalendar(calendar.THURSDAY)
# Str = hc.formatmonth(2025,1)
# print(str) 
# #loop over the days 0f a month
# # zeroes indicate that the day  of the week is in a next month or overlapping month for i in
# # c. itermonthday(2025,4):
# # print(i)
