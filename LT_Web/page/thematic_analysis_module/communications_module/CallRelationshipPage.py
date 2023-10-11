#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-通联分析-通话关系分析'''
class CallRelationshipPage(BasePage):

    @allure.step('高频通话')
    def check_High_frequency_call1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

    @allure.step('高频通话')
    def check_High_frequency_call2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        try:
            assert '13468881201' in text
            print('高频通话校验完成')
            return self
        except Exception as e:
            print('高频通话校验失败', format(e))

    @allure.step('零秒通话')
    def check_Zero_seconds_call1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

    @allure.step('非正常时段通话')
    def check_Abnormal_period_call1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

    @allure.step('非正常时段通话')
    def check_Abnormal_period_call2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        try:
            assert '136****9989' in text
            print('非正常时段通话校验完成')
            return self
        except Exception as e:
            print('非正常时段通话校验失败', format(e))

    @allure.step('共同联系人')
    def check_common_contacts1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

    @allure.step('共同联系人')
    def check_common_contacts2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        try:
            assert '9533885' in text
            print('共同联系人校验完成')
            return self
        except Exception as e:
            print('共同联系人校验失败', format(e))


    @allure.step('互相通话')
    def check_mutual_call1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

    @allure.step('互相通话')
    def check_mutual_call2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        try:
            assert '18898889945' in text
            print('互相通话校验完成')
            return self
        except Exception as e:
            print('互相通话校验失败', format(e))

    @allure.step('新旧号码')
    def check_New_old_numbers1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self


    @allure.step('位置分析-高频位置分析')
    def check_position_treble1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

    @allure.step('位置分析-高频位置分析')
    def check_position_treble2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        try:
            assert '22891' in text
            print('高频位置分析校验完成')
            return self
        except Exception as e:
            print('高频位置分析校验失败', format(e))

    @allure.step('位置分析-轨迹分析')
    def check_trace_analysis1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

    def check_trace_analysis2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

    @allure.step('位置分析-轨迹分析')
    def check_trace_analysis3(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        try:
            assert '共 213 条' in text
            print('轨迹分析校验完成')
            return self
        except Exception as e:
            print('轨迹分析校验失败', format(e))

    @allure.step('位置分析-轨迹重叠')
    def check_trace_overlap1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

    @allure.step('位置分析-轨迹相近')
    def check_trace_close1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

    @allure.step('位置分析-位置分布')
    def check_location_distribution1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

    @allure.step('通话规律分析-对端统计分析')
    def check_patterns_peer1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self


    @allure.step('通话规律分析-时间统计分析')
    def check_patterns_time1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/communications_module/CallRelationshipPage.yaml")
        return self

