#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-支付宝分析-关联手机分析'''
class AlipayPhonePage(BasePage):

    @allure.step('关联手机分析-共同充值手机')
    def check_Alipay_Phone1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayPhonePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayPhonePage.yaml")
        return self

    @allure.step('关联手机分析-共同充值手机')
    def check_Alipay_Phone2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayPhonePage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayPhonePage.yaml")
        try:
            assert '157' in text
            print('共同充值手机校验完成')
            return self
        except Exception as e:
            print('共同充值手机校验失败', format(e))

    @allure.step('关联手机分析-账户绑定手机')
    def check_Alipay_Phone_binding1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayPhonePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayPhonePage.yaml")
        return self

    @allure.step('关联手机分析-账户绑定手机')
    def check_Alipay_Phone_binding2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayPhonePage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayPhonePage.yaml")
        try:
            assert '187' in text
            print('账户绑定手机校验完成')
            return self
        except Exception as e:
            print('账户绑定手机校验失败', format(e))

    @allure.step('IP分析-团伙预判')
    def check_Alipay_IpGang1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayPhonePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayPhonePage.yaml")
        return self
