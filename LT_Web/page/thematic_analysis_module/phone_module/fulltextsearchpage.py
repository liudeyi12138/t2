#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-手机取证分析-全文检索'''
class FullTextsearchPage(BasePage):

    @allure.step('全文检索')
    def check_fulltext_search1(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/fulltextsearchpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/fulltextsearchpage.yaml")
        return self

    @allure.step('全文检索')
    def check_fulltext_search2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/fulltextsearchpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/fulltextsearchpage.yaml")
        try:
            assert '暂无数据' in text
            print('全文检索信息校验完成')
            return self
        except Exception as e:
            print('全文检索信息校验失败', format(e))


