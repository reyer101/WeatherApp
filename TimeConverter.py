import datetime

#Functions to convert UTC times into standard times


def time_convert(utc_time):
    time = datetime.datetime.fromtimestamp(utc_time).strftime('%I:%M%p')

    return time

def current_time():
    time = datetime.datetime.now().strftime('%I:%M%p')

    return time