#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/4 9:53
#@Author: hxj
#@File  : test_loginpage.py
# 1185375204@qq.com
# 15030805249youar
import os,sys
basedir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(basedir)[0]
sys.path.append(os.path.split(rootPath)[0])
from selenium import webdriver
from PageObjects.loginpage import LoginPage
from PageObjects.indexpage import IndexPage
from TestDatas import Common_Datas as CD
from TestDatas import Login_data as LD
from Common.my_logger import Log
from Common import dir_config
loger_path = dir_config.loger_path
my_logger =Log(__name__, loger_path).Logger
import pytest


class TestLogin():

#针对整个类文件的，在整个测试类开始执行前打开浏览器，并进行初始化

    def setup_class(self):
        my_logger.info("##########所有测试用例之前，setupClass整个测试类只执行一次##########")
        print("##########所有测试用例之前，setupClass整个测试类只执行一次##########")
        self.driver = webdriver.Chrome()
        self.driver.get(CD.web_login_url)
        self.lg = LoginPage(self.driver)
        #点击登录的按钮，进入登陆的页面
        self.lg.enter_Login()

    # 在整个测试类执行完，关闭浏览器
    def teardown_class(self):
        my_logger.info("############所有测试用例之后，tearDownClass,整个测试类只执行一次##########")
        print("############所有测试用例之后，tearDownClass,整个测试类只执行一次##########")
        self.driver.quit()


    #为了每个测试用例不互相干扰，所以每个测试用例执行完毕后刷新浏览器
    def teardown(self):
        my_logger.info("********tearDown每个测试用例执行后都要执行一次********")
        print("********tearDown每个测试用例执行后都要执行一次********")
        self.driver.refresh()

    """
    unitest中用例的执行顺序，是按照ACSII码的顺序加载测试用例的，数字与字母的顺序为0--9，A--Z，a--z，
    因为正常的用例执行后，会进行页面的跳转，所以才会把正常的用例放在最后面执行，因此才给用例编上号
    """
    #异常用例   用户不存在，用户名为空

    @pytest.mark.parametrize('data',LD.userwrongdate)
    def test_login_1_user_wrongFormat(self,data):
        my_logger.info('此时输入的用户名是{0}密码是{1}'.format(data['user'],data['passwd']))
        #步骤  输入用户名 密码点击登录
        self.lg.login(data['user'],data['passwd'])
        #断言，登录页面提示
        #登录页面中，获取登录框中文本内容
        #对比文本内容与期望值是否相等
        assert LoginPage(self.driver).user_errMsg()==data['check']
    #
    # #
    # #异常用例  密码为空，密码不正确
    @pytest.mark.parametrize('data1',LD.passwdwrongdata)
    def test_login_2_passwd_wrongFormat(self,data1):
        my_logger.info('此时输入的用户名{0}密码是{1}'.format(data1['user'],data1['passwd']))
        #步骤 输入用户名密码点击登录
        self.lg.login(data1['user'],data1['passwd'])
        #断言  登录页面中，获取登陆框中文本内容
        #对比文本内容与期望值是否一致
        assert LoginPage(self.driver).pwd_errMsg(), data1['check']


    # #正常用例    登陆成功的用例
    def test_login_3_success(self):
        my_logger.info('正常登陆的用户名是{0},密码是{1}'.format(LD.loginsucess['user'],LD.loginsucess['passwd']))
        #输入用户名密码，点击登录
        self.lg.login(LD.loginsucess['user'],LD.loginsucess['passwd'])
        #断言，首页当中能否找到用户这个元素
        assert IndexPage(self.driver).isExitUser()




# if __name__=="__main__":
#     pytest