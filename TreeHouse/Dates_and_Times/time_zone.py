# Time Zone
#   https://www.youtube.com/watch?v=-5wpm-gesOY
#   https://www.youtube.com/watch?v=uW6QqcmCfm8
#   When you create a datetime with a time zone then the object will know where in the world it is and how
#       to sort itself out.
#   A datetime knows it time zone is AWARE
#   A datetime that does not know what time zone it is in is NAIVE

import datetime
import pytz

#   timezone('specific time zone you are working with')
pacific = pytz.timezone('US/Pacific')
eastern = pytz.timezone('US/Eastern')
fmt = '%Y-"%m-%d %H:%M:%S %Z%z'
utc = pytz.utc
#   takes a naive datetime and give it with a certain timezone
start = pacific.localize(datetime.datetime(2014, 4, 21, 9))

print('___ASTIMEZONE___')
print(start.strftime(fmt))
#   '2014-"04-21 09:00:00 PDT-0700'
# localize is for naive time zone
start_eastern = start.astimezone(eastern)
print(start_eastern)
#   datetime.datetime(2014, 4, 21, 12, 0, tzinfo=<DstTzInfo 'US/Eastern' EDT-1 day, 20:00:00 DST>)
print(start)
#   datetime.datetime(2014, 4, 21, 9, 0, tzinfo=<DstTzInfo 'US/Pacific' PDT-1 day, 17:00:00 DST>)

print('___UTC TIME ZONE___')
start_utc = datetime.datetime(2014, 4, 21, 1, tzinfo=utc)
print(start_utc.strftime(fmt))
#   '2014-"04-21 01:00:00 UTC+0000'
start_pacific = start_utc.astimezone(pacific)
print(start_pacific)
#   datetime.datetime(2014, 4, 20, 18, 0, tzinfo=<DstTzInfo 'US/Pacific' PDT-1 day, 17:00:00 DST>)

print("___REAL WORLD EXAMPLES___")
auckland = pytz.timezone('Pacific/Auckland')
mumbai = pytz.timezone('Asia/Calcutta')
apollo_13_naive = datetime.datetime(1970, 4, 11, 14, 13)
apollo_13_eastern = eastern.localize(apollo_13_naive)
print(apollo_13_naive)
#   datetime.datetime(1970, 4, 11, 14, 13)
print(apollo_13_eastern)
#   datetime.datetime(1970, 4, 11, 14, 13, tzinfo=<DstTzInfo 'US/Eastern' EST-1 day, 19:00:00 STD>)
apollo_13_utc = apollo_13_eastern.astimezone(utc)
print(apollo_13_utc.astimezone(pacific).strftime(fmt))
#   '1970-"04-11 11:13:00 PST-0800'
print(apollo_13_utc.astimezone(auckland).strftime(fmt))
#   '1970-"04-12 07:13:00 NZST+1200'
print(apollo_13_utc.astimezone(mumbai).strftime(fmt))
#   '1970-"04-12 00:43:00 IST+0530'
print(pytz.all_timezones)
#   prints all of the time zones. The list is super long
print(pytz.country_timezones['US'])
#   [u'America/New_York', u'America/Detroit', u'America/Kentucky/Louisville', u'America/Kentucky/Monticello', u'America/Indiana/Indianapolis', u'America/Indiana/Vincennes', u'America/Indiana/Winamac', u'America/Indiana/Marengo', u'America/Indiana/Petersburg', u'America/Indiana/Vevay', u'America/Chicago', u'America/Indiana/Tell_City', u'America/Indiana/Knox', u'America/Menominee', u'America/North_Dakota/Center', u'America/North_Dakota/New_Salem', u'America/North_Dakota/Beulah', u'America/Denver', u'America/Boise', u'America/Phoenix', u'America/Los_Angeles', u'America/Anchorage', u'America/Juneau', u'America/Sitka', u'America/Metlakatla', u'America/Yakutat', u'America/Nome', u'America/Adak', u'Pacific/Honolulu']



# PYTZ FORMAT CHALLENGE
#   1. starter is a naive datetime. Use pytz to make it a "US/Pacific" datetime instead and assign this
#       converted datetime to the variable local.
#   2. Now create a variable named pytz_string by using strftime with the local datetime. Use the fmt string
#       for the formatting.

# import datetime
# import pytz

pacific = pytz.timezone('US/Pacific')
fmt = '%m-%d %H:%M %Z%z'
starter = datetime.datetime(2015, 10, 21, 4, 29)
local = pacific.localize(starter)
pytz_string = local.astimezone(pacific).strftime(fmt)


# TIME ZONE STRINGS CHALLENGE
#   1. Create a function named to_timezone that takes a timezone name as a string. Convert starter to that
#       timezone using pytz's timezones and return the new datetime.
starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(tzname):
    tz = pytz.timezone(tzname)
    datetime = starter.astimezone(tz)
    return datetime

