#!/usr/bin/env python
#-*-coding:utf-8 -*-

#author:haoxuejun

#正常用例 登陆成功的测试用例的数据
loginsucess = {'user':'1185375204@qq.com','passwd':'15030805249youar'}


#异常用例  用户名框下的错误信息  用户不村在，用户名为空
userwrongdate = [{'user':'111','passwd':'123456','check':'用户不存在'},
 {'user':'','passwd':'123456','check':'账号不能为空'}
 ]

#异常用例   密码下的错误信息  密码为空,密码的位数不对
passwdwrongdata=[{'user':'1185375204@qq.com','passwd':'','check':'密码不能为空'},
    {'user':'1185375204@qq.com','passwd':'1','check':'请输入6-24位密码'}
    # {'user':'1185375204@qq.com','passwd':'123456','check':'密码错误, 你还可以尝试4次'}
                 ]

