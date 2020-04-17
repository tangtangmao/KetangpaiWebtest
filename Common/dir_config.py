#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/4 21:43
#@Author: hxj
#@File  : dir_config.py

import os
#项目文件的目录
base_path = os.path.dirname(os.path.dirname(__file__))
#测试用例的目录
test_case_path = os.path.join(base_path,'TestCases')
# print(test_case_path)
#测试数据的目录
test_case_data_path = os.path.join(base_path,"TestDatas")
# print(test_case_data_path)
#测试结果输出的目录
test_report_outs= os.path.join(base_path,"OutPuts/allurereport")
# print(test_report_outs)
#截图输出的目录
screenshot_path = os.path.join(base_path,"OutPuts/screenshots")

#日志输出的路径
loger_path = os.path.join(base_path,'OutPuts/log/login.log')



