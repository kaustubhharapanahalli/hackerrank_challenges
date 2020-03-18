"""
Challenge:         calendar module
Link to Challenge: https://www.hackerrank.com/challenges/calendar-module/problem

Author:            Kaustubh M. Harapanahalli
"""

import calendar

mm, dd, yyyy = map(int, input().split())
calendar.setfirstweekday(calendar.SUNDAY)

print(list(calendar.day_name)[calendar.weekday(yyyy, mm, dd)].upper())
