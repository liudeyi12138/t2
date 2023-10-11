#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-微信分析-关联分析'''
class WeChatAssociationPage(BasePage):

    @allure.step('微信分析-关联分析')
    def check_WeChat_Association1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/WeChat_module/WeChatAssociationPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/WeChat_module/WeChatAssociationPage.yaml")
        return self

    @allure.step('微信分析-关联分析')
    def check_WeChat_Association2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/WeChat_module/WeChatAssociationPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/WeChat_module/WeChatAssociationPage.yaml")
        try:
            assert 'zcpzsw' in text
            print('关联分析校验完成')
            return self
        except Exception as e:
            print('关联分析校验失败', format(e))