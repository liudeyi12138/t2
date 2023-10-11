#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''工具箱-制作宽表'''
class WideTablePage(BasePage):

    @allure.step('制作宽表')
    def check_WideTable1(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml")
        sleep(1)
        return self

    @allure.step('制作宽表')
    def check_WideTable2(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml")
        sleep(1)
        return self

    @allure.step('制作宽表')
    def check_WideTable3(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml")
        sleep(1)
        return self

    @allure.step('制作宽表')
    def check_WideTable4(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml")
        sleep(1)
        return self

    @allure.step('制作宽表')
    def check_WideTable5(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml")
        sleep(1)
        return self

    @allure.step('制作宽表')
    def check_WideTable6(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml")
        sleep(1)
        return self

    @allure.step('校验宽表是否保存成功')
    def check_WideTable7(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/Toolbox_module/WideTablePage.yaml")
        try:
            assert '宽表1 (当前分组：过程库2)' in text
            print('宽表校验完成')
            return self
        except Exception as e:
            print('宽表校验失败', format(e))


