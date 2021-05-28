# -*- coding: utf-8 -*-
# @Time : 2020/10/21 16:04
# @Author : Jclian91
# @File : global_conf.py
# @Place : Yangpu, Shanghai
import os

# 项目所在地址
PROJECT_DIR = os.getenv("WORK_DIR", os.path.dirname(os.path.abspath(__file__)).replace("config", ""))
# print(PROJECT_DIR)
