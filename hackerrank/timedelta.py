#!/bin/python3

import math
import os
import random
import re
import sys

def time_parser(T):
    time_parts = T.split(' ')
    date = time_parts[1]
    month = time_parts[2]
    year = time_parts[3]
    time = time_parts[4].split(':')
    hour = time[0]
    minutes = time[1]
    seconds = time[2]
    time_zone = time_parts[5]
    time_zone_hour = int(time_zone[:3])
    time_zone_minutes = int(time_zone[3:])
    return ((int)(date), month, (int)(year), (int)(hour), (int)(minutes), (int)(seconds), (int)(time_zone_hour), (int)(time_zone_minutes))

def is_leap(Y):
    leap = False
    if (Y%400==0 or (Y%4==0 and Y%100!=0)):
        leap=True
    return leap

def get_year_days(y1,y2,t_days):
    total_days=0
    for i in range(y1,y2):
        total_days +=t_days;
        if is_leap(i):
            total_days +=1
    return total_days

def days_until_today(y,m,d,days_list):
    total_days=0
    for i in range(m):
        total_days+=days_list[i]
    if is_leap(y) and m>1:
        total_days+=1
    return total_days + d - 1

def time_delta(t1, t2):
    (date1, month1, year1, hour1, minutes1, seconds1, time_zone_h1, time_zone_m1) = time_parser(t1)
    (date2, month2, year2, hour2, minutes2, seconds2, time_zone_h2, time_zone_m2) = time_parser(t2)

    month_list = {'Jan':0,'Feb':1,'Mar':2,'Apr':3,'May':4,'Jun':5,'Jul':6,'Aug':7,'Sep':8,'Oct':9,'Nov':10,'Dec':11}
    days_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    one_year_days = sum(days_list)

    time_sec1 = hour1 * 3600 + minutes1*60 + seconds1
    time_sec2 = hour2 * 3600 + minutes2*60 + seconds2

    zone_diff1 = abs(time_zone_h1)*3600 + time_zone_m1*60
    if time_zone_h1<0:
        zone_diff1*=-1
        
    zone_diff2 = abs(time_zone_h2)*3600+ time_zone_m2*60
    if time_zone_h2<0:
        zone_diff2*=-1
    total_month_days2 = days_until_today(year2,month_list[month2],date2,days_list)
    total_month_days1 = days_until_today(year1,month_list[month1],date1,days_list)
    
    if year2 <= year1:
        total_days = get_year_days(year2,year1,one_year_days) + total_month_days1 - total_month_days2
        total_sec = total_days * 3600 * 24 + time_sec1 - time_sec2 + zone_diff2 - zone_diff1

    else:
        total_days = get_year_days(year1,year2,one_year_days) + total_month_days2 - total_month_days1
        total_sec = total_days * 3600 * 24 + time_sec2 - time_sec1 + zone_diff1 - zone_diff2
        

    return str(abs(total_sec))
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)

        #fptr.write(delta + '\n')

    #fptr.close()

