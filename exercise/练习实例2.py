# -*- coding:utf-8 -*-

'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10
万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，
可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过10
0万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
i = int(input("请输入当月利润："))
sum1=sum2=sum3=sum4=sum5=sum6=0

if i <= 100000:
    sum1 = i*0.1
elif i > 100000 and i <= 200000:
    sum1 = 100000*0.1
    sum2 = (i-100000)*0.075
elif i > 200000 and i <= 400000:
    sum1 = 100000*0.1
    sum2 = 100000*0.075
    sum3 = (i-200000)*0.05
elif i > 400000 and i <= 600000:
    sum1 = 100000*0.1
    sum2 = 100000*0.075
    sum3 = 200000*0.05
    sum4 = (i-400000)*0.03
elif i > 600000 and i <= 1000000:
    sum1 = 100000*0.1
    sum2 = 100000*0.075
    sum3 = 200000*0.05
    sum4 = 400000*0.03
    sum5 = (i-600000)*0.015 
elif i > 1000000:
    sum1 = 100000*0.1
    sum2 = 100000*0.075
    sum3 = 200000*0.05
    sum4 = 400000*0.03
    sum5 = 600000*0.015 
    sum6 = (i-1000000)*0.01
    
sum = sum1+sum2+sum3+sum4+sum5+sum6

# print(sum1, sum2, sum3, sum4, sum5, sum6)
print(sum)


# Better
'''
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print (i-arr[idx])*rat[idx]
        i=arr[idx]
print r
'''
