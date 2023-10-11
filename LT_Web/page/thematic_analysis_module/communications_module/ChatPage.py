#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-通联分析-聊天分析'''
class ChatPage(BasePage):

    @allure.step('聊天基础分析')
    def check_chat_basic1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/ChatPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/ChatPage.yaml")
        return self

    @allure.step('聊天基础分析')
    def check_chat_basic2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/ChatPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/communications_module/ChatPage.yaml")
        return self
        # try:
        #     assert '156****3118' in text
        #     print('原始数据查询校验完成')
        #     return self
        # except Exception as e:
        #     print('原始数据查询校验失败', format(e))

    @allure.step('聊天匹配分析')
    def check_chat_matching1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/ChatPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/ChatPage.yaml")
        return self

    @allure.step('关键字预警')
    def check_keyword_alert1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/ChatPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/ChatPage.yaml")
        return self

    @allure.step('关键字预警')
    def check_keyword_alert2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/ChatPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/ChatPage.yaml")
        return self


    @allure.step('聊天账号分析')
    def check_chat_ID1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/ChatPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/ChatPage.yaml")
        return self
