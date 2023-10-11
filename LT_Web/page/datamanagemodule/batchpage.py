#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage
from LT_Web.page.datamanagemodule.batchcataloguelistpage import CatalogueListPage
from LT_Web.page.datamanagemodule.datauploadpage import DataUploadPage

'''调证管理'''
class BatchPage(BasePage):

    @allure.step('点击目录列表-需求详情')
    def click_catalogue_list(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/batchpage.yaml", time=10)#显示等待
        self.steps("../data/batchpage.yaml")
        return CatalogueListPage(self._driver)

    @allure.step('点击上传数据')
    def click_upload_data(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/batchpage.yaml", time=10)#显示等待
        self.steps("../data/batchpage.yaml")
        return DataUploadPage(self._driver)






