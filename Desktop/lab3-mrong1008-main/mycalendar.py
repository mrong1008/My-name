#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 平年：365 天 ， 2月 28 天  2021 
# 闰年：366 天 ， 2月 29 天  2020

# 年份整除4 ——》 闰年
# else -> 平年

# 2100 ->平年

# 某一个年份可以整除100， 那么只有当他可以整除400的时候，才是闰年

# //
# 1:31, 2:28/29, 3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31

def is_leap_year(year):
    if year%100 == 0:
        if year %400 == 0:
            return True
        else:
            return False
    else:
        if year%4 == 0:
            return True
        else:
            return False
def num_days_in_month(year, month):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month<8:
        if month%2 == 0: #4,6
            return 30
        else:  #1，3，5，7
            return 31
    else:
        if month%2 == 0: #8，10，12
            return 31
        else: #9,11
            return 30
def day_in_year(year, month, day):
    days = 0
    for i in range(1,month):
        print(i,num_days_in_month(year, i))
        days += num_days_in_month(year, i)
    days += day
    return days 
def day_in_year_to_date(year, day):
    calcu = 0
    for month in range(1,13):
        #calcu += mycalendar(year, month)
        if day < num_days_in_month(year, month):
            return (year,month,day)
        day -= num_days_in_month(year, month)
        if day == 0:
            return (year,month,num_days_in_month(year, month))

