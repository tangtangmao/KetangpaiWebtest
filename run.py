#!/usr/bin/env python
#-*-coding:utf-8 -*-

#author:haoxuejun

#生成allure的测试报告
# allure serve ../OutPuts/allurereport
import pytest
import sys
print("开始测试")
#执行pytest前的参数准备
pytest_execute_params = ['-v','--alluredir','OutPuts/allurereport/','--clean-alluredir']

exit_code = pytest.main(pytest_execute_params)
print('结束测试')
sys.exit(exit_code)