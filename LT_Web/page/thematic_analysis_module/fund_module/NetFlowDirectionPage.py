#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-手机取证分析-资金专题分析-资金净流向分析'''
class NetFlowDirectionPage(BasePage):

    @allure.step('资金净流向分析')
    def check_fund_net_flow_direction1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/NetFlowDirectionPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/NetFlowDirectionPage.yaml")
        return self

    def check_fund_net_flow_direction2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/NetFlowDirectionPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/NetFlowDirectionPage.yaml")
        return self

