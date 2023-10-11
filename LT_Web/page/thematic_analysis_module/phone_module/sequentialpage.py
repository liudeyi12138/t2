#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-手机取证分析-时序分析'''
class SequentialPage(BasePage):

    @allure.step('时序分析-时空序数')
    def check_sequential_space_time(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/sequentialpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/sequentialpage.yaml")
        return self

    @allure.step('时序分析-空间序数')
    def check_transaction_space1(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/sequentialpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/sequentialpage.yaml")
        return self

    @allure.step('时序分析-空间序数')
    def check_transaction_space2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/sequentialpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/sequentialpage.yaml")
        return self

    @allure.step('时序分析-空间序数')
    def check_transaction_space3(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/sequentialpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/sequentialpage.yaml")
        try:
            assert '1731XXX5448' in text
            print('空间序数信息校验完成')
            return self
        except Exception as e:
            print('空间序数信息校验失败', format(e))


