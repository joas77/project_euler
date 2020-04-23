# https://projecteuler.net/problem=19
"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import datetime

if __name__ == "__main__":
    sunday = datetime.date(year=1901,month=1, day=6) # January 6, 1901 was 1th sunday in year 1901
    delta_week = datetime.timedelta(days=7)
    last_20cent_day = datetime.date(year=2000, month=12, day=31)

    sunday_counter = 0

    while sunday <= last_20cent_day:
        if sunday.day == 1:
            sunday_counter +=1
        sunday += delta_week

    print(f"solution: {sunday_counter}")