#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage
from LT_Web.page.datamanagemodule.batchcataloguelistpage import CatalogueListPage
from LT_Web.page.datamanagemodule.datauploadpage import DataUploadPage

'''集合成员管理'''
class AssembleMemberPage(BasePage):

    @allure.step('集合成员管理-点击新增')  # 将函数作为一个步骤，调用此函数时，报告中输出这个步骤，我把这样的函数叫“step函数”
    def add_assemble_member(self):
        # 获取打开的多个窗口句柄
        windows = self._driver.window_handles
        # 切换到当前最新打开的窗口
        self._driver.switch_to.window(windows[-1])
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/assemblemember.yaml", time=10)#显示等待
        self.steps("../data/assemblemember.yaml")
        return self

    @allure.step('填写新增集合成员信息，点击提交')  # 将函数作为一个步骤，调用此函数时，报告中输出这个步骤，我把这样的函数叫“step函数”
    def Edit_new_assemble_member(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/assemblemember.yaml", time=10)  # 显示等待
        self.steps("../data/assemblemember.yaml")
        sleep(2)
        return self

    @allure.step('点击确定')
    def click_ok(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/assemblemember.yaml", time=10)  # 显示等待
        self.steps("../data/assemblemember.yaml")
        return self

    @allure.step('断言是否集合加入成功')
    def assert_check8(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/assemblemember.yaml", time=10)  # 显示等待
        text = self.steps("../data/assemblemember.yaml")
        return text


