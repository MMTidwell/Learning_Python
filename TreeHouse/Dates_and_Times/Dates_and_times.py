from __future__ import print_function
import datetime

print("___.datetime.now()___")
print(datetime.datetime.now())
# => 2016-04-25 10:10:34.110000
#    Date       Time

treehouse_start = datetime.datetime.now()
print(treehouse_start)
# => 2016-04-25 10:12:34.230000
print("___.replace()___")
treehouse_start = treehouse_start.replace(hour=9, minute=0, second=0, microsecond=0)
print(treehouse_start)
# => 2016-04-25 09:00:00

th_start = datetime.datetime(2014, 10, 15, 9)
print(th_start)
# this does the same as above, controls the date too.
# => 2014-10-15 09:00:00

print(datetime.datetime.now() - treehouse_start)
time_worked = datetime.datetime.now() - treehouse_start
print(time_worked.days)
# => 0
print(time_worked.microseconds)
# => 783000
print(time_worked.seconds)
# => 4875
print(dir(time_worked))
# => ['__abs__', '__add__', '__class__', '__delattr__', '__div__', '__doc__', '__eq__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__pos__', '__radd__', '__rdiv__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmul__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'days', 'max', 'microseconds', 'min', 'resolution', 'seconds', 'total_seconds']
hours_worked = round(time_worked.seconds / 3600)
print(hours_worked)
# => 1.0

now = datetime.datetime.now()
print(now + datetime.timedelta(hours=5, days=3))
# => prints 3 days form today => 2016-04-28 15:37:55.971000
print(now + datetime.timedelta(hours=5, days=-5))
# => prints 3 days ago due to '-' in days => 2016-04-20 15:39:14.564000
print(now.date())
# => 2016-04-25
print(now.time())
# => 10:40:39.316000

hour = datetime.timedelta(hours=1)
print(hour)
# => 1:00:00

workday = hour * 9
tomorrow = datetime.datetime.now().replace(hour=9, minute=0) + datetime.timedelta(days=1)
print(tomorrow)
# => 2016-04-26 09:00:54.220000
print(tomorrow + workday)
# => 2016-04-26 18:00:36.165000

print("___making an appointment___")
appointment = datetime.timedelta(minutes=45)
start = datetime.datetime(2014, 11, 1, 12, 45)
#       (YEAR, MONTH, DAY, HOUR, MIN)
print(start)
# => 2014-11-01 12:45:00

print("___combine dates and time together___")
now = datetime.datetime.now()  # can work with time zones
today = datetime.datetime.today()  # today's date
print(now)
print(today)

today = datetime.datetime.combine(datetime.date.today(), datetime.time())
print(today)
print(today.year)
print(today.month)
print(today.day)
print(now.hour)
print(today.weekday())  # python weeks start on Monday's


def minutes(dt1, dt2):
    difference = round((dt2 - dt1).total_seconds() / 60)
    return difference


print('___dating methods___')
now = datetime.datetime.now()
print(now)
print(now.strftime("%B %d"))
#   => (month, day)
print(now.strftime("%m/%d/%y"))
# when needing to know what to put in, look online
birthday = datetime.datetime.strptime("2016-4-26", '%Y-%m-%d')
birthday_party = datetime.datetime.strptime('2016-4-26 13:00', '%Y-%m-%d %H:%M')
print(birthday)
print(birthday_party)


def time_tango(date, time):
    date_time = datetime.datetime.combine(date, time)
    print(date_time)


today = datetime.datetime.today()
print(now)  # can take a time zone where today can not
print(today)
today = datetime.datetime.combine(datetime.date.today(), datetime.time())
print(today)  # this will start automatically at midnight
print(today.month)
print(today.hour)
print(today.year)
print(now.hour)
print(today.weekday())  # shows numbers for days of the week starting with monday = 1
print('')


# STRFTIME AND STRPTIME CHALLENGE
def to_string(x):
    return x.datetime('$d %B %Y')


def from_string(x, y):
    date = datetime.datetime.strptime(x, y)
    return date


# SIMPLE TIME MACHINE
# Write a function named delorean that takes an integer. Return a datetime that is that many hours ahead from starter.
starter = datetime.datetime(2015, 10, 21, 16, 29)


def delorean(x):
    return starter.replace(hour=starter.hour + x)



# HARDER TIME MACHINE
# years is not recognized with timedeltas, you must use days and * by 365
def time_machine(x, y):
    if y == "minutes":
        return starter + datetime.timedelta(minutes=x)
    if y == "hours":
        return starter + datetime.timedelta(hours=x)
    if y == "days":
        return starter + datetime.timedelta(days=x)
    if y == "years":
        return starter + datetime.timedelta(days=x * 365)


# TIMESTAMP ORDERING
def timestamp_oldest(*args):
    time_list = []
    for arg in args:
        time_list.append(arg)

    time_list.sort()
    return datetime.datetime.fromtimestamp(time_list[0])
