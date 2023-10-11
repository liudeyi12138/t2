#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu

'''首页'''
from time import sleep

import allure



from LT_Web.page.basepagemodule.base_page import BasePage
from LT_Web.page.caselistmodule.caselistpage import CaseList

'''首页'''
class Main(BasePage):

    @allure.step('登录')
    def login(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/main.yaml", time=10)  # 显示等待
        self.steps("../data/main.yaml")
        return CaseList(self._driver)


    @allure.step('释放资源')
    def quit_web(self):#资源回收，释放资源
        self._driver.quit()
        return self