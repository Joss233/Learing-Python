# -*- coding:utf-8 -*-


# 将一个列表的数据复制到另一个列表中。

old_list = input("请输入原列表中的元素：").split(" ")
new_list = []

for i in old_list:
    new_list.append(i)

print("新的列表为：",new_list)
