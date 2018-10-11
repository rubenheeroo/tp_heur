import time, datetime

"""print(time.time())

help(time)

print(time.localtime())
print(datetime.datetime.now())
p = time.strftime(%Y, time.localtime(now))
print(p)"""
a= datetime.date(2018, 1, 1)
for i in range(0,365):
    if a.weekday()==4:
        print (a)
#b = datetime.weekday(annee, 1, 1)
print(a)
#print (b)

print(a.weekday())

