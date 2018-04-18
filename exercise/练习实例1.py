# -*- coding:utf-8 -*-

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

for i1 in range(1,5):
    for i2 in range(1,5):
        if i1 != i2:
            for i3 in range(1,5):
                if i1 != i3 and i2 != i3:
                    i = i1*100+i2*10+i3
                    print(i)
