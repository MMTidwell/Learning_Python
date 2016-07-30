# Build apt scheduler that builds a date/time in 6 time zones
from __future__ import print_function
import datetime
import pytz

# List of time zones
OTHER_TIMEZONES = [
    pytz.timezone('US/Eastern'),
    pytz.timezone('Pacific/Auckland'),
    pytz.timezone('Asia/Calcutta'),
    pytz.timezone('UTC'),
    pytz.timezone('Europe/Paris'),
    pytz.timezone('Africa/Khartoum')
]
fmt = '%m-%d %H:%M:%S %Z%z'

while True:
    date_input = input('When is your meeting? Please use MM/DD//YYYY HH:MM format. ')
    try:
        local_date = datetime.strptime(date_input, '%m/%d/%Y %H:%M')
    except ValueError:
        print('Doesnt seem to be a valid date and time.'.format(date_input))
    else:
        local_date = pytz.timezone('US/Pacific').localize(local_date)
        utc_date = local_date.astimezone(pytz.utc)

        output = []
        for timezone in OTHER_TIMEZONES:
            output.append(utc_date.astiemzone(timezone))
        for appointment in output:
            print(appointment.strftime(fmt))
        break


# SHOULD HAVE AN OUTPUT WITH ALL TIME ZONES AND WHAT TIME IT WILL BE
#   This does not work for some reason with strptime.