#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-手机取证分析-交易分析'''
class TransactionPage(BasePage):

    @allure.step('交易概述')
    def check_transaction_overview1(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易概述')
    def check_transaction_overview2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易概述')
    def check_transaction_overview3(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        try:
            assert '1760' in text
            print('交易概述信息校验完成')
            return self
        except Exception as e:
            print('交易概述信息校验失败', format(e))

    @allure.step('交易关系')
    def check_transaction_relationship1(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易关系')
    def check_transaction_relationship2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self
    
    @allure.step('交易分析-交易账号')
    def check_transaction_account1(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-交易账号')
    def check_transaction_account2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-交易账号')
    def check_transaction_account3(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        try:
            assert '12' in text
            print('交易账号信息校验完成')
            return self
        except Exception as e:
            print('交易账号信息校验失败', format(e))
    
    @allure.step('交易分析-交易记录')
    def check_transaction_record1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-交易记录')
    def check_transaction_record2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-交易记录')
    def check_transaction_record3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        try:
            assert '共 12 条' in text
            print('交易记录信息校验完成')
            return self
        except Exception as e:
            print('交易记录信息校验失败', format(e))

    @allure.step('交易分析-交易频率')
    def check_transaction_frequency1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-交易频率')
    def check_transaction_frequency2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-交易频率')
    def check_transaction_frequency3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        try:
            assert '共 2 条' in text
            print('交易频率信息校验完成')
            return self
        except Exception as e:
            print('交易频率信息校验失败', format(e))

    @allure.step('交易分析-收支分析')
    def check_transaction_income1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-收支分析')
    def check_transaction_income2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-账单时序')
    def check_transaction_billing1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-账单时序')
    def check_transaction_billing2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-账单时序')
    def check_transaction_billing3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        try:
            assert '共 8 条' in text
            print('账单时序信息校验完成')
            return self
        except Exception as e:
            print('账单时序信息校验失败', format(e))

    @allure.step('交易分析-节假日交易')
    def check_transaction_holiday1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-节假日交易')
    def check_transaction_holiday2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-节假日交易')
    def check_transaction_holiday3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        try:
            assert '暂无数据' in text
            print('节假日交易信息校验完成')
            return self
        except Exception as e:
            print('节假日交易信息校验失败', format(e))

    @allure.step('交易分析-交易日历')
    def check_transaction_calendar1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-交易日历')
    def check_transaction_calendar2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-交易日历')
    def check_transaction_calendar3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        return self

    @allure.step('交易分析-交易日历')
    def check_transaction_calendar4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/transactionpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/transactionpage.yaml")
        try:
            assert '12' in text
            print('交易日历信息校验完成')
            return self
        except Exception as e:
            print('交易日历信息校验失败', format(e))



