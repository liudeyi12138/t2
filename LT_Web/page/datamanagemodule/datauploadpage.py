#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage
from LT_Web.page.logpagemodule.logpage import LogPage

'''批次管理-数据上传'''
class DataUploadPage(BasePage):

    @allure.step('首次进入-新建批次')
    def new_batch(self):
        sleep(2)
        # # 获取打开的多个窗口句柄
        # windows = self._driver.window_handles
        # # 切换到当前最新打开的窗口
        # self._driver.switch_to.window(windows[-1])
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/datauploadpage.yaml", time=10)#显示等待
        self.steps("../data/datauploadpage.yaml")
        return self

    @allure.step('数据上传-上传调证数据')
    def upload_data(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/datauploadpage.yaml", time=10)#显示等待
        self.steps("../data/datauploadpage.yaml")
        sleep(5)
        return self

    @allure.step('调证数据上传完成-点击导入确定')
    def upload_click(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/datauploadpage.yaml", time=10)#显示等待
        self.steps("../data/datauploadpage.yaml")
        return self

    @allure.step('调证数据上传完成-点击导入后-点击弹窗的确定')
    def upload_click_ok(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/datauploadpage.yaml", time=10)#显示等待
        self.steps("../data/datauploadpage.yaml")
        # sleep(2)
        return self

    @allure.step('弹窗对否继续导入-否')
    def continue_no(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/datauploadpage.yaml", time=10)#显示等待
        self.steps("../data/datauploadpage.yaml")
        sleep(2)
        return LogPage(self._driver)

    @allure.step('新建取证批次')
    def new_batch_quzheng(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/datauploadpage.yaml", time=10)#显示等待
        self.steps("../data/datauploadpage.yaml")
        return self

    @allure.step('数据上传-上传取证数据')
    def upload_data_quzheng(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/datauploadpage.yaml", time=10)#显示等待
        self.steps("../data/datauploadpage.yaml")
        sleep(2)
        return self

    @allure.step('关联嫌疑人-确定')
    def new_suspect(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/datauploadpage.yaml", time=10)#显示等待
        self.steps("../data/datauploadpage.yaml")
        sleep(2)
        return self

    @allure.step('点击导入日志')
    def click_uploadlog(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/datauploadpage.yaml", time=10)#显示等待
        self.steps("../data/datauploadpage.yaml")
        sleep(2)
        return LogPage(self._driver)

    @allure.step('断言是否数据导入成功')
    def assert_check5(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/datauploadpage.yaml", time=10)#显示等待
        text = self.steps("../data/datauploadpage.yaml")
        return text