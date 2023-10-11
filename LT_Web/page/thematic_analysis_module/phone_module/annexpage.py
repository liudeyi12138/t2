#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-手机取证分析-附件分析'''
class AnnexPage(BasePage):

    @allure.step('附件分析-图片')
    def check_annex_picture(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/annexpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/annexpage.yaml")
        return self


