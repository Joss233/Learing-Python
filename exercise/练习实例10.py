# -*- coding:utf-8 -*-

# 暂停一秒输出，并格式化当前时间。


import time

print("现在开始···")
time.sleep(3)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
