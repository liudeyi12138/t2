#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-手机取证分析-资金专题分析-可疑行为分析'''
class SuspiciousBehaviorPage(BasePage):

    @allure.step('资金专题分析-可疑行为分析-大额转账-单笔大额转账')
    def check_large_single1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-大额转账-单笔大额转账')
    def check_large_single2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        try:
            assert '120000' in text
            print('单笔大额转账信息校验完成')
            return self
        except Exception as e:
            print('单笔大额转账信息校验失败', format(e))

    @allure.step('资金专题分析-可疑行为分析-大额转账-累计日大额转账')
    def check_large_accumulate1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-大额转账-累计日大额转账')
    def check_large_accumulate2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-大额转账-累计日大额转账')
    def check_large_accumulate3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        try:
            assert '1068145' in text
            print('累计日大额转账信息校验完成')
            return self
        except Exception as e:
            print('累计日大额转账信息校验失败', format(e))

    @allure.step('资金专题分析-可疑行为分析-异常时间段转账')
    def check_abnormal_time1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-异常时间段转账')
    def check_abnormal_time2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-异常时间段转账')
    def check_abnormal_time3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        try:
            assert '662546' in text
            print('异常时间段转账信息校验完成')
            return self
        except Exception as e:
            print('异常时间段转账信息校验失败', format(e))
            
    @allure.step('资金专题分析-可疑行为分析-频繁交易')
    def check_frequent_transactions1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-频繁交易')
    def check_frequent_transactions2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-频繁交易')
    def check_frequent_transactions3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        try:
            assert '1.17' in text
            print('频繁交易信息校验完成')
            return self
        except Exception as e:
            print('频繁交易信息校验失败', format(e))
            
    @allure.step('资金专题分析-可疑行为分析-快进快出')
    def check_fast_inout1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-快进快出')
    def check_fast_inout2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-快进快出')
    def check_fast_inout3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        try:
            assert '290199.4' in text
            print('快进快出信息校验完成')
            return self
        except Exception as e:
            print('快进快出信息校验失败', format(e))        
            
    @allure.step('资金专题分析-可疑行为分析-账户分工')
    def check_account_work1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-账户分工')
    def check_account_work2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-账户分工')
    def check_account_work3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        try:
            assert '3895510.25' in text
            print('账户分工信息校验完成')
            return self
        except Exception as e:
            print('账户分工信息校验失败', format(e))
            
    @allure.step('资金专题分析-可疑行为分析-规律性分析-沉睡账户')
    def check_regularity_sleep1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-规律性分析-沉睡账户')
    def check_regularity_sleep2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-规律性分析-沉睡账户')
    def check_regularity_sleep3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        try:
            assert '刘小小' in text
            print('规律性分析-沉睡账户信息校验完成')
            return self
        except Exception as e:
            print('规律性分析-沉睡账户信息校验失败', format(e))
            
    @allure.step('资金专题分析-可疑行为分析-规律性分析-间隙性账户')
    def check_regularity_gap1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-规律性分析-间隙性账户')
    def check_regularity_gap2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-规律性分析-间隙性账户')
    def check_regularity_gap3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        try:
            assert '黄小扬' in text
            print('规律性分析-间隙性账户信息校验完成')
            return self
        except Exception as e:
            print('规律性分析-间隙性账户信息校验失败', format(e))

    @allure.step('资金专题分析-可疑行为分析-规律性分析-资金规律')
    def check_regularity_fund1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-试机测试')
    def check_test_machine1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-试机测试')
    def check_test_machine2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        return self

    @allure.step('资金专题分析-可疑行为分析-试机测试')
    def check_test_machine3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/fund_module/suspiciousbehaviorpage.yaml")
        try:
            assert '田小维' in text
            print('试机测试信息校验完成')
            return self
        except Exception as e:
            print('试机测试信息校验失败', format(e))







