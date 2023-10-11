#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-支付宝分析-透视分析'''
class AlipayPerspectivePage(BasePage):

    @allure.step('透视分析')
    def check_Alipay_Perspective1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayPerspectivePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayPerspectivePage.yaml")
        return self

    @allure.step('透视分析')
    def check_Alipay_Perspective2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayPerspectivePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Alipay_module/AlipayPerspectivePage.yaml")
        return self

    @allure.step('透视分析')
    def check_Alipay_Perspective3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Alipay_module/AlipayPerspectivePage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Alipay_module/AlipayPerspectivePage.yaml")
        try:
            assert '6217003288888249555' in text
            print('透视分析校验完成')
            return self
        except Exception as e:
            print('透视分析校验失败', format(e))
