#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage
from LT_Web.page.datamanagemodule.batchcataloguelistpage import CatalogueListPage
from LT_Web.page.datamanagemodule.datauploadpage import DataUploadPage

'''白名单管理'''
class WhiteListPage(BasePage):

    @allure.step('白名单管理-点击新增')  # 将函数作为一个步骤，调用此函数时，报告中输出这个步骤，我把这样的函数叫“step函数”
    def add_whitelist(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/whitelistpage.yaml", time=10)#显示等待
        self.steps("../data/whitelistpage.yaml")
        # sleep(2)
        return self

    @allure.step('填写新增白名单信息，点击提交')  # 将函数作为一个步骤，调用此函数时，报告中输出这个步骤，我把这样的函数叫“step函数”
    def Edit_new_whitelist(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/whitelistpage.yaml", time=10)#显示等待
        self.steps("../data/whitelistpage.yaml")
        # sleep(2)
        return self

    @allure.step('断言是否白名单加入成功')
    def assert_check6(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/whitelistpage.yaml", time=10)#显示等待
        text = self.steps("../data/whitelistpage.yaml")
        try:
            assert '20230726001' in text
            # print('Assertion test pass.')
            print('白名单新增成功')
        except Exception as e:
            # print('Assertion test fail.', format(e))
            print('白名单新增失败', format(e))


