#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/5 9:44
#@Author: hxj
#@File  : base_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common import dir_config
import datetime
from Common.my_logger import Log
from Common import dir_config
loger_path = dir_config.loger_path
my_logger =Log(__name__, loger_path).Logger

class BasePage:

    # driver = webdriver.Chrome()
    # driver.find_element().send_keys()
    # driver.find_element_by_name('')


    def __init__(self,driver):
        self.driver = driver

    #等待元素可见
    def wait_eleVisible(self,locator,timeout,poll_frequency=0.5,doc=''):
        """
            :param timeout: 等待的时长
            :param poll_frequency: 轮询的时间
            :param locator:元素定位，元祖形势（元素的定位类型，元素的定位）
            :param doc:
            :return: None
            """

        try:
            #开始等待的时间是
            start = datetime.datetime.now()
            # print('开始的时间是{0}'.format(start))
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located((locator)))
            #等待后的时间是
            end= datetime.datetime.now()
            #等待的时长是
            time = (end-start).seconds
            my_logger.info('等待元素{0}可见开始等待的时间是{1}，结束等待的时间{2}，等待的时长是{3}'.format(locator,start,end,time))
        except:
            #如果元素不可见或是没有出现就进行截屏
            self.save_screenshots(doc)
           # """
           # errror只是记录一个日志消息，日志的级别是error。而Exception则在记录消息的同时，默认会记录错误发生的
           # traceback信息，所以如果想记录更为详细的错误信息，最好使用exception，error方法若是也想输出堆栈信息则
           # 需要设置exc_info，logging.errror("错误"，exc_info=True)
           # """
            my_logger.exception('等待元素可见失败')
            raise

    #查找元素
    def get_element(self,locator,doc=''):
        """

        :param locator: 元素定位表达式，元素类型，表达方式（元素定位类型，元素定位方法）
        :param doc:截图时，需要用到的功能模块的备注
        :return:webelement
        """

        try:
            my_logger.info('当前要查找的元素是{0}'.format(locator))
            return self.driver.find_element(*locator)
        except :
            my_logger.exception('查找元素{0}失败！！！'.format(locator))
            #如果失败截图
            self.save_screenshots(doc)
            raise

    #像元素中输入内容
    def input_element(self,locator,text,doc=''):
        """
        :param locator: 元素的定位表达式，元素形式（定位）
        :param text:向元素中输入的内容
        :param doc:截图时，需要用到的功能模块的备注
        :return: None
        """
        ele = self.get_element(locator)
        my_logger.info("当前在{0}元素中输入{1}".format(locator, text))
        try:
            #将元素中可能存在的提示信息清空
            ele.clear()
            #向元素中输入内容
            ele.send_keys(text)
        except:
            my_logger.exception('向{0}元素输入{1}失败')
            #截图
            self.save_screenshots(doc)
            raise

    #获取元素的文本内容
    def get_elementTxt(self,locator,doc=''):
        """

        :param locator:元素的定位表达式，元祖形势（定位类型，定位的元素表达式）
        :param doc:截图时，要用到文件的说明
        :return:Text 元素的文本内容
        """
        self.wait_eleVisible(locator,10,doc)
        ele =self.get_element(locator,doc)
        try:
           text = ele.text
           my_logger.info('{0}的元素的文本内容是{1}'.format(locator,text))
           return text
        except:
            my_logger.error('error级别',exc_info=True)
            self.save_screenshots(doc)
            raise

    #获取元素的属性
    def get_element_attribute(self,locator,attr,doc=''):
        """

        :param locator: 元素的定位表达式，元祖形势（定位的类型，定位的元素表达式）
        :param attr:要获取的属性名称
        :param doc:截图时要用到的模块说明
        :return:attribute属性
        """
        self.wait_eleVisible(locator,10,doc)
        ele = self.get_element(*locator,doc)
        try:
            my_logger.info('获取元素{0}的属性{1}'.format(locator,attr))
            attribute = ele.get_attribute(attr)
            return attribute
        except:
            my_logger.exception('获取元素{0}的属性{1}失败'.format(locator,attr))
            self.save_screenshots(doc)
            raise


    #点击元素
    def click_ele(self,locator,doc=''):
        """

        :param locator: 元素的定位表达式，元祖形式（元素的定位方式，元素表达式）
        :param doc:截图时要用到的元素的模块名称
        :return:None
        """
        my_logger.info('查找元素{0}'.format(locator))
        #找元素
        ele = self.get_element(locator)
        try:
            # 进行操作
            ele.click()
        except:
            my_logger.exception('点击元素{0}操作失败'.format(locator))
            #如果失败则进行截图
            self.save_screenshots(doc)
            raise


    #窗口切换
    def switch_window(self):

        # driver.switch_to.window(window_name)
        pass

    #frame切换
    def switch_frame(self):
        pass
    #截图操作
    def save_screenshots(self,doc):
        """
        :param doc: 模块的名称+用力的名字的一个说明性的
        :return: None
        1、文件的名字要注意，文件的名字不要太长，
        2、不能含有特殊的字符像冒号啥的
        """
        #当前的时间
        time = datetime.datetime.now().strftime('%y-%m-%d_%H_%M_%S')
        #文件的路径名称为模块名+用例名+操作名称+当时的时间
        # filepath=图片的保存目录/页面功能名称_当前时间到秒.png
        filename =dir_config.screenshot_path+\
                      "/{0}-{1}.png".format(doc,time)

        try:
            #调用自带的截屏操作，这个截屏操作仅仅是截取的网页的图片
            self.driver.get_screenshot_as_file(filename)
            my_logger.info("截取网页成功，截取的路径为{0}".format(filename))
        except:

            my_logger.exception("截取失败")
            raise


    #文件上传操作
    def uploadfile(self):
        pass
