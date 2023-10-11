#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage

'''调证管理-调证管理详情'''
class CatalogueListPage(BasePage):

    @allure.step('批量新增')
    def import_data(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/batchcataloguelistpage.yaml", time=10)#显示等待
        self.steps("../data/batchcataloguelistpage.yaml")
        # sleep(2)
        return self

    @allure.step('断言是否新增成功')
    def assert_check4(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/batchcataloguelistpage.yaml", time=10)#显示等待
        text = self.steps("../data/batchcataloguelistpage.yaml")
        try:
            assert '13063096677' in text
            print('批量新增完成')
            return self
        except Exception as e:
            print('批量新增失败', format(e))


