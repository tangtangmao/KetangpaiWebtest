#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/4 9:27
#@Author: hxj
#@File  : loginpage.py
"""登陆页的操作"""


import time
from PageLocators import loginlocator as LC
from Common.base_page import BasePage
from Common.my_logger import Log
from Common import dir_config
loger_path = dir_config.loger_path
my_logger =Log(__name__, loger_path).Logger

class LoginPage(BasePage):


    def __init__(self,driver):
        self.driver = driver


    #登陆的入口
    def enter_Login(self):
        doc = '登陆界面_登陆的入口界面'
        my_logger.info('登陆界面的登陆入口的界面')
        try:
            self.wait_eleVisible(timeout=10,locator =LC.login_button,doc = doc)
            self.click_ele(LC.login_button,doc = doc)
        except :
            my_logger.error('进入登陆界面的登陆入口界面失败了')
            raise


    def login(self,username,passwd):
        my_logger.info('登陆界面的-登陆功能')
        time.sleep(2)
        doc = '登陆界面-登陆功能'
        # 等待用户名输入框的出现
        self.wait_eleVisible(LC.user_text,timeout=10,doc = doc)
        # 账户输入框
        self.input_element(LC.user_text,username,doc=doc)
        # 密码输入框
        self.input_element(LC.passwd_text,passwd,doc=doc)
        # 点击登录按钮
        self.click_ele(LC.submit_button,doc=doc)

    def user_errMsg(self):
        my_logger.info('登陆界面-获取用户名下的错误提示信息')
        doc = '登陆界面-获取用户名下的错误提示信息'
        self.wait_eleVisible(LC.user_errMsg,timeout=10,doc=doc)
        return self.get_elementTxt(LC.user_errMsg,doc=doc)


    def pwd_errMsg(self):
        my_logger.info('登陆界面-获取密码下的提示信息')
        doc='登陆界面-获取密码下的提示信息'
        self.wait_eleVisible(LC.passwd_errMsg,timeout=10,doc=doc)

        return self.get_elementTxt(LC.passwd_errMsg,doc=doc)

