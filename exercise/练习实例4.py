# -*- coding:utf-8 -*-

# 输入某年某月某日，判断这一天是这一年的第几天？

time = input("请输入年月日（如20150815）：")
year = int(time[:4])
month = int(time[4:6])
day = int(time[6:])
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
sumdays = 0

print("%d年%d月%d日" % (year,month,day))

# 1.先计算普通年份天数
for i in range(0,month):
     sumdays = days[i] + sumdays

     
# 2.判断闰年，若月份大于2则总天数+1
if (year%4==0 and year%100!=0) or (year%100==0 and year%400==0):
    if month > 2:
        sumdays += 1

sumdays = sumdays + day
print("这是%d年的第%d天" % (year,sumdays))
    
