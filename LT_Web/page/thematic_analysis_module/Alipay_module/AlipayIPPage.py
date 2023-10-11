#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-支付宝分析-IP分析-支付宝登录统计'''
class AlipayIPPage(BasePage):

    @allure.step('IP分析-支付宝登录统计')
    def check_Alipay_IP1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml")
        return self

    @allure.step('IP分析-支付宝登录统计')
    def check_Alipay_IP2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml")
        try:
            assert '117.136.62.146' in text
            print('支付宝登录统计校验完成')
            return self
        except Exception as e:
            print('支付宝登录统计校验失败', format(e))

    @allure.step('IP分析-IP跳转分析')
    def check_Alipay_IpJump1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml")
        return self

    @allure.step('IP分析-IP跳转分析')
    def check_Alipay_IpJump2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml")
        try:
            assert '关小鸿' in text
            print('IP跳转分析校验完成')
            return self
        except Exception as e:
            print('IP跳转分析校验失败', format(e))

    @allure.step('IP分析-团伙预判')
    def check_Alipay_IpGang1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml")
        return self

    @allure.step('IP分析-团伙预判')
    def check_Alipay_IpGang2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayIPPage.yaml")
        try:
            assert '福建' in text
            print('团伙预判校验完成')
            return self
        except Exception as e:
            print('团伙预判校验失败', format(e))
