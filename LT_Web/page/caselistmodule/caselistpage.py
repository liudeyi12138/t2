#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage
from LT_Web.page.homepagemodule.homepage import HomePage

'''案件管理'''
class CaseList(BasePage):

    @allure.step('点击新建案件')  # 将函数作为一个步骤，调用此函数时，报告中输出这个步骤，我把这样的函数叫“step函数”
    def click_addcase(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/caselistpage.yaml", time=10)#显示等待
        self.steps("../data/caselistpage.yaml")
        # return Operation(self._driver)#进运营管理
        return self

    @allure.step('编辑新增案件信息点击提交')
    def Edit_new_case(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/caselistpage.yaml", time=10)#显示等待
        self.steps("../data/caselistpage.yaml")
        # return Operation(self._driver)#进运营管理
        return self

    @allure.step('点击确定')
    def click_ok(self):
        sleep(1)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/caselistpage.yaml", time=10)#显示等待
        self.steps("../data/caselistpage.yaml")
        # return Operation(self._driver)#进运营管理
        return self

    @allure.step('断言是否新增案件成功')
    def assert_check1(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/caselistpage.yaml", time=10)#显示等待
        text = self.steps("../data/caselistpage.yaml")#获取页面提示信息
        # return Operation(self._driver)#进运营管理
        return text

    @allure.step('案件新建成功后点击弹窗确定进入其首页')
    def click_newcase_ok(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/caselistpage.yaml", time=10)#显示等待
        self.steps("../data/caselistpage.yaml")
        # sleep(2)
        return HomePage(self._driver)

    @allure.step('搜索案件-回车-点击击进入其首页')
    def search_case(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/caselistpage.yaml", time=10)#显示等待
        self.steps("../data/caselistpage.yaml")
        sleep(1)
        return HomePage(self._driver)

    # @allure.step('搜索案件后点击进入其首页')
    # def search_click(self):
    #     # self.set_implicitly(10)  # 隐式等待
    #     self.webdriver_wait(path="../data/caselistpage.yaml", time=10)#显示等待
    #     self.steps("../data/caselistpage.yaml")
    #     # return Operation(self._driver)#进运营管理
    #     return self

    @allure.step('释放资源')
    def quit_web(self):#资源回收，释放资源
        self._driver.quit()
        return self
