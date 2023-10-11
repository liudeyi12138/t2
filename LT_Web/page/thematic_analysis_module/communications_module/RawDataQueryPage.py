#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-通联分析-原始数据查询'''
class RawDataQueryPage(BasePage):

    @allure.step('原始数据查询')
    def check_Raw_data_query1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/RawDataQueryPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/RawDataQueryPage.yaml")
        return self

    def check_Raw_data_query2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/RawDataQueryPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/communications_module/RawDataQueryPage.yaml")
        try:
            assert '156****3118' in text
            print('原始数据查询校验完成')
            return self
        except Exception as e:
            print('原始数据查询校验失败', format(e))


