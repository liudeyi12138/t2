#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-支付宝分析-数据关联'''
class AlipayAssociationPage(BasePage):

    @allure.step('数据关联-支付宝主端信息')
    def check_Alipay_Association1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayAssociationPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayAssociationPage.yaml")
        return self

    @allure.step('数据关联-支付宝主端信息')
    def check_Alipay_Association2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayAssociationPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayAssociationPage.yaml")
        try:
            assert '黄小扬' in text
            print('支付宝主端信息校验完成')
            return self
        except Exception as e:
            print('支付宝主端信息校验失败', format(e))

    @allure.step('数据关联-未调取对端基本信息')
    def check_Alipay_Association3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayAssociationPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayAssociationPage.yaml")
        return self

    @allure.step('数据关联-未调取对端基本信息')
    def check_Alipay_Association4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayAssociationPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayAssociationPage.yaml")
        try:
            assert '周小哲' in text
            print('未调取对端基本信息校验完成')
            return self
        except Exception as e:
            print('未调取对端基本信息校验失败', format(e))