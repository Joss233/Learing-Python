# -*- coding:utf-8 -*-


'''
输出斐波那契数列，斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34...。
'''

n = int(input("请输入你需要的斐波那契数列个数："))

if n == 1:
    l = [0]
elif n == 2:
    l = [0,1]
elif n > 2:
    l = [0,1]
    for i in range(2,n):
        l.append(l[i-2]+l[i-1])
else:
    print("错误的个数。")
    exit()
    
print(l)
