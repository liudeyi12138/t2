#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-微信分析-消费分析'''
class WeChatConsumptionPage(BasePage):

    @allure.step('微信分析-消费分析')
    def check_WeChat_Consumption1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml")
        return self

    @allure.step('微信分析-消费分析')
    def check_WeChat_Consumption2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml")
        return self

    @allure.step('微信分析-消费分析')
    def check_WeChat_Consumption3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml")
        try:
            assert '1000050001200302022208000340344585466737' in text
            print('消费分析分析校验完成')
            return self
        except Exception as e:
            print('消费分析分析校验失败', format(e))

    @allure.step('微信分析-消费分析-充值信息')
    def check_WeChat_Consumption_Recharge1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml")
        return self

    def check_WeChat_Consumption_Recharge2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml")
        return self

    @allure.step('微信分析-消费分析-充值信息')
    def check_WeChat_Consumption_Recharge3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/WeChat_module/WeChatConsumptionPage.yaml")
        try:
            assert 'wang13882114561' in text
            print('充值信息校验完成')
            return self
        except Exception as e:
            print('充值信息校验失败', format(e))