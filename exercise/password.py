# -*- coding:utf-8 -*-

import chardet

password = "2333"
i = 0

tryword = input("请输入密码:")

while i < 3:
    i += 1
    if tryword == password:
        print("密码正确!")
        break
    elif i < 3:
        tryword = input("密码错误,请重新输入:")
    else:
        exit()
