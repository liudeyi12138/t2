#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-手机取证分析-资金专题分析-原始数据查询'''
class RawDataPage(BasePage):

    @allure.step('资金专题分析-原始数据查询-分类原始数据-支付宝')
    def check_classification_rawdata_alipay1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-支付宝')
    def check_classification_rawdata_alipay2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '关小鸿' in text
            print('支付宝注册表信息校验完成')
            return self
        except Exception as e:
            print('支付宝注册表信息校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-支付宝')
    def check_classification_rawdata_alipay3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-支付宝')
    def check_classification_rawdata_alipay4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '18358887303' in text
            print('支付宝交易信息表信息校验完成')
            return self
        except Exception as e:
            print('支付宝交易信息表信息校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-支付宝')
    def check_classification_rawdata_alipay5(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-支付宝')
    def check_classification_rawdata_alipay6(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '46270548998888883901364' in text
            print('支付宝购物信息表信息校验完成')
            return self
        except Exception as e:
            print('支付宝购物信息表信息校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-支付宝')
    def check_classification_rawdata_alipay7(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-支付宝')
    def check_classification_rawdata_alipay8(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '2409:8962:580e:04e8:2891:cb15:29e4:639d' in text
            print('支付宝登陆日志表信息校验完成')
            return self
        except Exception as e:
            print('支付宝登陆日志表信息校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '共 39 条' in text
            print('银行卡账单表信息校验完成')
            return self
        except Exception as e:
            print('银行卡账单表信息校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '352888198888888888' in text
            print('银行卡信息表信息校验完成')
            return self
        except Exception as e:
            print('银行卡信息表信息校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard5(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard6(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '510888198888838888' in text
            print('银行卡人员信息表信息校验完成')
            return self
        except Exception as e:
            print('银行卡人员信息表信息校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard7(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard8(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '中国四****市绵阳市xxxx8栋8单元888' in text
            print('银行卡住址表信息校验完成')
            return self
        except Exception as e:
            print('银行卡住址表信息校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard9(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard10(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '重庆市南川区公安xxxxxxxxx' in text
            print('银行卡强制措施表信息校验完成')
            return self
        except Exception as e:
            print('银行卡强制措施表信息校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard11(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-银行卡')
    def check_classification_rawdata_bankcard12(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '183888888750' in text
            print('银行卡联系方式表信息校验完成')
            return self
        except Exception as e:
            print('银行卡联系方式表信息校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-财付通')
    def check_classification_rawdata_tenpay1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-财付通')
    def check_classification_rawdata_tenpay2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '刘小小' in text
            print('财付通基本信息表校验完成')
            return self
        except Exception as e:
            print('财付通基本信息表校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-财付通')
    def check_classification_rawdata_tenpay3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-财付通')
    def check_classification_rawdata_tenpay4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '1000039501180121022888888888883139511737' in text
            print('财付通交易信息表信息校验完成')
            return self
        except Exception as e:
            print('财付通交易信息表信息校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-分类原始数据-取证报告')
    def check_classification_rawdata_report1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-分类原始数据-取证报告')
    def check_classification_rawdata_report2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '共 25 条' in text
            print('转账支付记录表校验完成')
            return self
        except Exception as e:
            print('转账支付记录表校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-汇总流水-支付宝')
    def check_classification_summaryflow_alipay1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-汇总流水-支付宝')
    def check_classification_summaryflow_alipay2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '139' in text
            print('支付宝汇总流水校验完成')
            return self
        except Exception as e:
            print('支付宝汇总流水校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-汇总流水-银行卡')
    def check_classification_summaryflow_bankcard1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-汇总流水-银行卡')
    def check_classification_summaryflow_bankcard2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '18' in text
            print('银行卡汇总流水校验完成')
            return self
        except Exception as e:
            print('银行卡汇总流水校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-汇总流水-财付通')
    def check_classification_summaryflow_tenpay1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-汇总流水-财付通')
    def check_classification_summaryflow_tenpay2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '9' in text
            print('财付通汇总流水校验完成')
            return self
        except Exception as e:
            print('财付通汇总流水校验失败', format(e))

    @allure.step('资金专题分析-原始数据查询-汇总流水-取证报告')
    def check_classification_summaryflow_report1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        return self

    @allure.step('资金专题分析-原始数据查询-汇总流水-取证报告')
    def check_classification_summaryflow_report2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/rawdatapage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/rawdatapage.yaml")
        try:
            assert '共 4 条' in text
            print('取证报告汇总流水校验完成')
            return self
        except Exception as e:
            print('取证报告汇总流水校验失败', format(e))