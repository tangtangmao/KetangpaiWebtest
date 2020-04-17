#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/4 15:08
#@Author: hxj
#@File  : loginlocator.py
from selenium.webdriver.common.by import By
"""
1、元素定位并不一定只用一次
2、可能以后元素的定位会变
3、页面元素比较复杂的时候，可能有好几十个元素定位，不太友好
"""
#登陆页面的元素定位
login_button = (By.XPATH, "//*[text()='登录']")
#用户名元素定位
user_text=(By.NAME,'account')
#密码元素定位
passwd_text=(By.NAME,'pass')

#登陆提交的按钮
submit_button=(By.XPATH,"//*[@class='btn-btn']")
#用户名下面的错误提示
user_errMsg=(By.XPATH,"//*[@name='account']/following-sibling::p")
#密码下面的错误提示
passwd_errMsg=(By.XPATH,"//*[@name='pass']/following-sibling::p")
