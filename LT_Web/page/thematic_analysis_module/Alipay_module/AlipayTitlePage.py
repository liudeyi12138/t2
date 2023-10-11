#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-支付宝分析-消费标题分析'''
class AlipayTitlePage(BasePage):

    @allure.step('消费标题分析-主端')
    def check_Alipay_Title_Host1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml")
        return self

    @allure.step('消费标题分析-主端')
    def check_Alipay_Title_Host2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml")
        return self

    @allure.step('消费标题分析-主端')
    def check_Alipay_Title_Host3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml")
        return self

    @allure.step('消费标题分析-主端')
    def check_Alipay_Title_Host4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml")
        try:
            assert '红包' in text
            print('主端校验完成')
            return self
        except Exception as e:
            print('主端校验失败', format(e))

    @allure.step('消费标题分析-对端')
    def check_Alipay_Title_peer1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml")
        return self

    @allure.step('消费标题分析-对端')
    def check_Alipay_Title_peer2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayTitlePage.yaml")
        try:
            assert '王小世' in text
            print('对端校验完成')
            return self
        except Exception as e:
            print('对端校验失败', format(e))
