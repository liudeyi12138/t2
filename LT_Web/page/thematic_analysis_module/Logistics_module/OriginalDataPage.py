#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-物流分析-物流原始数据'''
class OriginalDataPage(BasePage):

    @allure.step('物流原始数据')
    def check_original_data1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/logistics_module/OriginalDataPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/logistics_module/OriginalDataPage.yaml")
        return self

    @allure.step('物流原始数据')
    def check_original_data2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/OriginalDataPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/logistics_module/OriginalDataPage.yaml")
        try:
            assert '16621081422' in text
            print('物流原始数据查询校验完成')
            return self
        except Exception as e:
            print('物流原始数据查询校验失败', format(e))
