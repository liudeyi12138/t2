#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''超级画像'''
class SuperPersonPage(BasePage):

    @allure.step('人员画像-选择嫌疑人')
    def choose_suspect(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self


    @allure.step('操作数据加入调取目录')
    def add_diaoqulist1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('操作数据加入调取目录')
    def add_diaoqulist2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('操作数据加入调取目录')
    def add_diaoqulist3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同交易对端-查询')
    def group_transaction1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同交易对端-右键点击')
    def group_transaction2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同交易对端-加入白名单')
    def group_transaction3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同交易对端-加入白名单-确定')
    def group_transaction4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同通话对端-点击')
    def group_call1(self):
        sleep(3)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同通话对端-查询')
    def group_call2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同通话对端-查看详情')
    def group_call3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同通话对端-点击保存')
    def group_call4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同通话对端-编辑过程库')
    def group_call5(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同通话对端-编辑过程库-选择数据类型')
    def group_call6(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同通话对端-保存至过程库')
    def group_call7(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同通话对端-保存至过程库-关闭弹窗')
    def group_call8(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同聊天对端-点击')
    def group_chat1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同聊天对端-查询')
    def group_chat2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同聊天对端-查看操作详情')
    def group_chat3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同聊天对端-详情-搜索聊天信息')
    def group_chat4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同聊天对端-详情-搜索聊天信息-关闭弹窗')
    def group_chat5(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同登录IP-点击')
    def group_loginIp1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self


    @allure.step('群体分析-共同登录IP-查询')
    def group_loginIp2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同登录IP-查看操作详情')
    def group_loginIp3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('群体分析-共同登录IP-查看操作详情-关闭弹窗')
    def group_loginIp4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('关联分析')
    def group_relevance1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('关联分析-查询')
    def group_relevance2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('团伙管理')
    def group_gang1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('信息补齐')
    def group_information1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('信息补齐-选择嫌疑人')
    def group_information2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        self.steps("../data/superpersonpage.yaml")
        return self

    @allure.step('校验')
    def group_check(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/superpersonpage.yaml", time=10)#显示等待
        text = self.steps("../data/superpersonpage.yaml")
        return text


