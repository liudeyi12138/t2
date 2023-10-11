#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-物流分析-可疑行为分析'''
class OriginalSuspiciousBehaviorPage(BasePage):

    @allure.step('可疑行为分析-发货地与手机归属地不一致')
    def check_Suspicious_Behavior1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml")
        return self

    @allure.step('可疑行为分析-发货地与手机归属地不一致')
    def check_Suspicious_Behavior2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml")
        try:
            assert '75418376674556' in text
            print('发货地与手机归属地不一致校验完成')
            return self
        except Exception as e:
            print('发货地与手机归属地不一致校验失败', format(e))

    @allure.step('可疑行为分析-收货地与手机归属地不一致')
    def check_Suspicious_different_address1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml")
        return self

    @allure.step('可疑行为分析-收货地与手机归属地不一致')
    def check_Suspicious_different_address2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml")
        try:
            assert '75420062066867' in text
            print('收货地与手机归属地不一致校验完成')
            return self
        except Exception as e:
            print('收货地与手机归属地不一致校验失败', format(e))

    @allure.step('可疑行为分析-收发货地址相同')
    def check_Suspicious_equal_address1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml")
        return self

    @allure.step('可疑行为分析-收发货地址相同')
    def check_Suspicious_equal_address2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml")
        try:
            assert '4310137155243' in text
            print('收发货地址相同校验完成')
            return self
        except Exception as e:
            print('收发货地址相同校验失败', format(e))

    @allure.step('可疑行为分析-收发货电话相同')
    def check_Suspicious_equal_phone1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml")
        return self


    @allure.step('可疑行为分析-异常揽件时间')
    def check_Suspicious_abnormal_time1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml")
        return self

    @allure.step('可疑行为分析-异常揽件时间')
    def check_Suspicious_abnormal_time2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml")
        try:
            assert '4310137191847' in text
            print('异常揽件时间校验完成')
            return self
        except Exception as e:
            print('异常揽件时间校验失败', format(e))

    @allure.step('可疑行为分析-虚拟号码')
    def check_Suspicious_virtually_number1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml")
        return self

    @allure.step('可疑行为分析-虚拟号码')
    def check_Suspicious_virtually_number2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/logistics_module/OriginalSuspiciousBehaviorPage.yaml")
        try:
            assert '75404659215190' in text
            print('虚拟号码校验完成')
            return self
        except Exception as e:
            print('虚拟号码校验失败', format(e))

