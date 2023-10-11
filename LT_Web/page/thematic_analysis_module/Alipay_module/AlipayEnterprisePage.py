#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-支付宝分析-企业支付宝分析'''
class AlipayEnterprisePage(BasePage):

    @allure.step('企业支付宝分析-试机分析')
    def check_Alipay_EnterpriseTest1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml")
        return self

    @allure.step('企业支付宝分析-试机分析')
    def check_Alipay_EnterpriseTest2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml")
        try:
            assert '2088932888881592' in text
            print('试机分析校验完成')
            return self
        except Exception as e:
            print('试机分析校验失败', format(e))

    @allure.step('企业支付宝分析-典型卡分析')
    def check_Alipay_Enterprise_Typical1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml")
        return self


    @allure.step('企业支付宝分析-典型卡分析')
    def check_Alipay_Enterprise_Typical2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml")
        return self

    @allure.step('企业支付宝分析-典型卡分析')
    def check_Alipay_Enterprise_Typical3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml")
        try:
            assert '吴小钦' in text
            print('典型卡分析校验完成')
            return self
        except Exception as e:
            print('典型卡分析校验失败', format(e))



    @allure.step('企业支付宝分析-交易分析')
    def check_Alipay_Enterprise_Transaction1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml")
        return self

    @allure.step('企业支付宝分析-交易分析')
    def check_Alipay_Enterprise_Transaction2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml")
        try:
            assert '赵小成' in text
            print('交易分析校验完成')
            return self
        except Exception as e:
            print('交易分析校验失败', format(e))

    @allure.step('企业支付宝分析-大金额转账')
    def check_Alipay_Enterprise_Transf1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml")
        return self

    @allure.step('企业支付宝分析-大金额转账')
    def check_Alipay_Enterprise_Transf2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayEnterprisePage.yaml")
        try:
            assert '2088042888882823' in text
            print('大金额转账校验完成')
            return self
        except Exception as e:
            print('大金额转账校验失败', format(e))

