#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/4 9:41
#@Author: hxj
#@File  : indexpage.py
"""
登陆后首页的元素和方法
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class IndexPage:
    # driver = webdriver.Chrome()

    def __init__(self,driver):
        self.driver = driver


    def isExitUser(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@class='avatar']")))
            # self.driver.find_element_by_xpath("//*[@class='avatar']")
            return  True
        except:
            return False
            raise

