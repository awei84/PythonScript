#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@Author: awei84    
@Contact: xx@qq.com
@Modify_Time: 2021/6/15 8:59       
@Desciption: python2转python3的脚本（使用python自带2to3）
"""

import os

# n表示不需要备份文件
def plpy2to3(rote, py34rote):
    if rote[-3:] == ".py": # 单纯的.py文件
        os.system("pythonw %s -wn %s" % (py34rote, rote))
        # 不在命令窗口输出转化内容，如果要在命令窗口输出的话，把pythonw改为python
        print("pythonw %s -wn %s" % (py34rote, rote))
    else:
        os.chdir(rote) # 文件夹
        print(os.getcwd())
        for i in alistdir(rote):
            if i[-3:] == ".py":
                os.system("pythonw %s -wn %s" % (py34rote, i))
                # 不在命令窗口输出转化内容，如果要在命令窗口输出的话，把pythonw改为python
                print("pythonw %s -wn %s" % (py34rote, i))


def alistdir(sendrote):
    """遍历指定目录下所有文件生成文件和路径"""
    listrote = []
    print("列出该系统目录下所有文件夹和文件:")
    listrote = []
    for root, dirs, files in os.walk(sendrote):
        for file in files:
            curroot = os.path.join(root, file)
            listrote.append(curroot)

    return listrote


# 目标目录rote 或者文件
rote = r"D:\pythonfile\workcode\Update44.py"
# 2to3.py
py34rote = "C:\\Python\\Python37\\Tools\\scripts\\2to3.py"
plpy2to3(rote, py34rote)
