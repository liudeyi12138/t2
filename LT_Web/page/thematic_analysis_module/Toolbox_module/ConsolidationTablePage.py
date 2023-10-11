#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''工具箱-制作并表'''
class ConsolidationTablePage(BasePage):

    @allure.step('制作并表')
    def check_ConsolidationTable1(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml")
        sleep(1)
        return self

    @allure.step('制作并表')
    def check_ConsolidationTable2(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml")
        sleep(1)
        return self

    @allure.step('制作并表')
    def check_ConsolidationTable3(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml")
        sleep(1)
        return self

    @allure.step('制作并表')
    def check_ConsolidationTable4(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml")
        sleep(1)
        return self

    @allure.step('制作并表')
    def check_ConsolidationTable5(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml")
        sleep(1)
        return self

    @allure.step('制作并表')
    def check_ConsolidationTable6(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml")
        sleep(1)
        return self

    @allure.step('制作并表')
    def check_ConsolidationTable7(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml")
        sleep(1)
        return self

    @allure.step('校验并表是否保存成功')
    def check_ConsolidationTable8(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Toolbox_module/ConsolidationTablePage.yaml")
        try:
            assert '并表1 (当前分组：过程库1)' in text
            print('并表校验完成')
            return self
        except Exception as e:
            print('并表校验失败', format(e))


