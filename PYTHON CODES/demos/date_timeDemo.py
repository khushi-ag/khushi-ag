import time 

'''
epoch = time.time()
print (epoch)

dt = time.localtime(epoch) #converts the epoch time into time_structs object dt
print (dt)


#retrieve date time from structure dt
d = dt.tm_mday
m= dt.tm_mon
y= dt.tm_year
print("Date is : %d - %d - %d" %(d,m,y))

h = dt.tm_hour
m= dt.tm_min
s= dt.tm_sec
print("Time is : %d - %d - %d" %(h,m,s))


t = time.ctime(epoch) #convert epoch time into date and time using ctime()
print(t)


#another way to retrieve current date
t = time.ctime()
print(t)

'''

from datetime import *
#another way to retrieve current date and time
now = datetime.now()
print(now)

print("Date now: {}/{}/{}".format(now.day, now.month, now.year))
print("Time now: {}:{}:{}".format(now.hour, now.minute, now.second))

#to know today's date and time
tdm = datetime.today()
print("Today's date and time is", tdm)

td = date.today()
print ("Today's date = ", td)


#combining date and time
d =date(2012,11,8)
t = time(15,30)
dt = datetime.combine(d,t)
print(dt)

#another way creating datetime instance
dt1 = datetime(year=2019, month = 6, day =24 , hour = 15, minute = 30, second = 15)
print(dt1)

dt2 = dt1.replace(year=2017, hour = 20, month = 10)
print(dt2)	



#formatting date

td = date.today()
print(td)

str1 = td.strftime("%d, %B, %Y")
print(str1)

str2= td.strftime("%j")  #extracting day of the year
print(str2)

str3 = d.strftime("%A") #show weeday as full name
print(str3)


#differences between two dates
d1,m1,y1 = [int(x) for x in input("Enter first date: ").split("/")]

d2,m2,y2 = [int(x) for x in input("Enter second date: ").split("/")]

dt1 = date(y1,m1,d1)
dt2 = date(y2,m2,d2)

dt = dt1-dt2
print("the difference is ",dt)


#difference in weeks
weeks,days = divmod(dt.days,7)
print("The difference in weeks is ", weeks, days) 

#difference in months
months,days = divmod(dt.days,30)
print("The difference in months is ", months,days) 


#compairing two dates
if (dt1==dt2):
	print("both the dates are equal")
elif (dt1 > dt2):
	print("second date is older")
else:
	print("first date is older")


#to find next date after 25 days
nextdate = dt1 + timedelta(days=25)
print("date after 25 days is " , nextdate)
