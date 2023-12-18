#!/usr/bin/env python3
# Student ID: cfederici

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second
        if type(hour) != int or type(minute) != int or type(second) != int:
            raise TypeError("hour, minute, and second must be integers")

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    """while loop that shows if sum.minute is greater than or = to 60, the sum.hour will be increased by one 
    and sum.minute reduced by 60."""
    while sum.minute >= 60:
        sum.hour += 1
        sum.minute -= 60
    """while loop again that shows if sum.second is greater than or = to 60, the minute is added by 1 and
    second subtracted by 60."""
    while sum.second >= 60:
        sum.minute += 1
        sum.second -= 60
    return sum

def change_time(time, seconds):
    time.second += seconds
    if valid_time(time) != True:
        while time.second >= 60:
             time.second -= 60
             time.minute +=1
        while time.minute >= 60:
             time.minute -= 60
             time.hour += 1
    return None

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True