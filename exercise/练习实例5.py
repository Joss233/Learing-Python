# -*- coding:utf-8 -*-

# 输入三个整数x,y,z，请把这三个数由小到大输出。
# 联想到输入n个数并按序输出。


int_nums, nums = [], []
nums = input("请输入n个数：").split() # 使用split()对输入进行切片

for i in nums:
    #print(nums)
    int_nums.append(int(i))

int_nums.sort()
print(int_nums)
