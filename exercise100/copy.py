# -*- coding:utf-8 -*-

old_filename = input("输入需要复制的文件名：")

old_file = open(old_filename,"r",encoding="utf-8").read()

new_filename = input("输入新文件名：")

new_file = open(new_filename,"w").write(old_file)
