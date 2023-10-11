#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-微信分析-原始数据查询'''
class WeChatOriginalPage(BasePage):

    @allure.step('原始数据查询')
    def check_WeChat_original_data1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/WeChat_module/WeChatOriginalPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/WeChat_module/WeChatOriginalPage.yaml")
        return self

    @allure.step('原始数据查询')
    def check_WeChat_original_data2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/WeChat_module/WeChatOriginalPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/WeChat_module/WeChatOriginalPage.yaml")
        return self

    @allure.step('原始数据查询')
    def check_WeChat_original_data3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/WeChat_module/WeChatOriginalPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/WeChat_module/WeChatOriginalPage.yaml")
        return self

    @allure.step('原始数据查询')
    def check_WeChat_original_data4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/WeChatOriginalPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/WeChat_module/WeChatOriginalPage.yaml")
        return self

    @allure.step('原始数据查询')
    def check_WeChat_original_data5(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/WeChatOriginalPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/WeChat_module/WeChatOriginalPage.yaml")
        try:
            assert '忘梓' in text
            print('微信原始数据查询校验完成')
            return self
        except Exception as e:
            print('微信原始数据查询校验失败', format(e))
