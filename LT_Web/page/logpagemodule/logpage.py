#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''导入日志列表'''
class LogPage(BasePage):

    @allure.step('断言调证数据是否导入成功')
    def check_diaozheng(self):
        sleep(4)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/logpage.yaml", time=10)#显示等待
        text = self.steps("../data/logpage.yaml")
        return text

    @allure.step('断言取证数据是否导入成功')
    def check_quzheng(self):
        sleep(1)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/logpage.yaml", time=10)#显示等待
        text = self.steps("../data/logpage.yaml")
        return text

    @allure.step('断言调证批次数据是否抽取成功')
    def check_update_diaozheng(self):
        sleep(5)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/logpage.yaml", time=10)#显示等待
        text = self.steps("../data/logpage.yaml")
        sleep(5)
        return text

    @allure.step('断言调调证次数据是否抽取成功')
    def check_update_quzheng(self):
        sleep(3)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/logpage.yaml", time=10)#显示等待
        text = self.steps("../data/logpage.yaml")
        return text

    @allure.step('断言图库数据是否抽取成功')
    def check_update_tuku(self):
        sleep(5)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/logpage.yaml", time=10)#显示等待
        text = self.steps("../data/logpage.yaml")
        return text






