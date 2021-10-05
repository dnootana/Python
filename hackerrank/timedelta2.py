def is_leap(year):
    leap = False
    if ( (year % 100 == 0) and (year % 400 != 0) ):
        leap = False
    else:
        if (year % 4 == 0):
            leap = True
        else:
            leap = False

    return leap

def time_parser(t):

    time_parts = t.split(' ')

    day = time_parts[1]
    month = time_parts[2]
    year = time_parts[3]

    time = time_parts[4].split(':')

    hours = time[0]
    minutes = time[1]
    seconds = time[2]

    time_zone = time_parts[5]

    time_zone_hours = (int)(time_zone[:3])
    time_zone_minutes=  (int)(time_zone[3:])

    return ((int)(day), month, (int)(year), (int)(hours), (int)(minutes), (int)(seconds), time_zone_hours, time_zone_minutes)

def total_days_in_year(y1, y2, days_per_year):

    total_days = 0
    # Add all the days in the year
    for i in range(y1, y2):
        if is_leap(i):
            total_days += (days_per_year+1)
        else:
            total_days += days_per_year

    return total_days

def get_days_until_current_month(day, m, year, days_array):
    

    days_until_month = 0
    for i in range(0, m):
        days_until_month += days_array[i]

    # Leap year and greater than Feb
    if (is_leap(year) and month_idx > 1):
        days_until_month += 1

    return days_until_month + day-1

def time_delta(t1,t2):
    month_list = {'Jan':0, 'Feb':1, 'Mar':2, 'Apr':3, 'May':4, 'Jun':5, 'Jul':6, 'Aug':7, 'Sep':8, 'Oct':9, 'Nov':10, 'Dec':11}
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    one_year_days = sum(months)

    # Parse the sub-parts    
    (day1, month1, year1, hours1, minutes1, seconds1, time_zone_h1, time_zone_m1) = time_parser(t1)    
    (day2, month2, year2, hours2, minutes2, seconds2, time_zone_h2, time_zone_m2) = time_parser(t2)

    total_month_days1 = get_days_until_current_month(day1, month_list[month1], year1, months)
    total_month_days2 = get_days_until_current_month(day2, month_list[month2], year2, months)

    time_sec1 = hours1 * 3600 + minutes1 * 60 + seconds1
    time_sec2 = hours2 * 3600 + minutes2 * 60 + seconds2

    zone_diff1 = abs(time_zone_h1) * 3600 + time_zone_m1 * 60
    if (time_zone_h1 < 0):
        zone_diff1 *= -1

    zone_diff2 = abs(time_zone_h2) * 3600 + time_zone_m2 * 60
    if (time_zone_h2 < 0):
        zone_diff2 *= -1
    # This is a later year
    if year1 >= year2:
        total_days = total_days_in_year(year2, year1, one_year_days) + total_month_days1 - total_month_days2
        total_sec = total_days * 24 * 3600 + time_sec1 - time_sec2 - zone_diff1 + zone_diff2        

    # This is an earlier year
    else:
        total_days = total_days_in_year(year1, year2, one_year_days) - total_month_days1 + total_month_days2
        total_sec = total_days * 24 * 3600 - time_sec1 + time_sec2 + zone_diff1 - zone_diff2

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