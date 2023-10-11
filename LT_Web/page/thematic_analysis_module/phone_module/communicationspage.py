#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-手机取证分析-通联分析'''
class CommunicationsPage(BasePage):

    @allure.step('通联概况-通讯录概览')
    def check_address_book(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通联概况-通话频率')
    def check_call_frequency1(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通联概况-通话频率')
    def check_call_frequency2(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通联概况-通话频率')
    def check_call_frequency3(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '1912XXX3638' in text
            print('通话频率信息校验完成')
            return self
        except Exception as e:
            print('通话频率信息校验失败', format(e))
            
    @allure.step('通联概况-短信频率')
    def check_sms_frequency1(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通联概况-短信频率')
    def check_sms_frequency2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通联概况-短信频率')
    def check_sms_frequency3(self):
        sleep(2)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '1569XXX9672' in text
            print('短信频率信息校验完成')
            return self
        except Exception as e:
            print('短信频率信息校验失败', format(e))

    @allure.step('通联异常-删除通话')
    def check_delete_call1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通联异常-通话差异')
    def check_call_differences1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通联异常-通话差异')
    def check_call_differences2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通联异常-通话差异')
    def check_call_differences3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '276' in text
            print('通话差异信息校验完成')
            return self
        except Exception as e:
            print('通话差异信息校验失败', format(e))

    @allure.step('通联异常-通联方差')
    def check_connected_variance1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通联异常-通联方差')
    def check_connected_variance2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通联异常-通联方差')
    def check_connected_variance3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '326.6' in text
            print('通联方差信息校验完成')
            return self
        except Exception as e:
            print('通联方差信息校验失败', format(e))

    @allure.step('通讯好友-好友概览')
    def check_friends_overview1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通讯好友-好友概览')
    def check_friends_overview2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通讯好友-好友概览')
    def check_friends_overview3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '和X多' in text
            print('好友概览信息校验完成')
            return self
        except Exception as e:
            print('好友概览信息校验失败', format(e))

    @allure.step('通讯好友-文件通讯')
    def check_friends_file1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self
    
    @allure.step('通讯好友-文件通讯')
    def check_friends_file2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通讯好友-文件通讯')
    def check_friends_file3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '腾讯新闻' in text
            print('文件通讯信息校验完成')
            return self
        except Exception as e:
            print('文件通讯信息校验失败', format(e))

    @allure.step('通讯好友-聊天记录查询')
    def check_friends_chat_records1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self
    
    @allure.step('通讯好友-聊天记录查询')
    def check_friends_chat_records2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通讯好友-聊天记录查询')
    def check_friends_chat_records3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '在不在' in text
            print('聊天记录查询信息校验完成')
            return self
        except Exception as e:
            print('聊天记录查询信息校验失败', format(e))

    @allure.step('通讯好友-好友聊天查询')
    def check_friends_chat1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self
    
    @allure.step('通讯好友-好友聊天查询')
    def check_friends_chat2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('通讯好友-好友聊天查询')
    def check_friends_chat3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '狐狸已成精' in text
            print('好友聊天查询信息校验完成')
            return self
        except Exception as e:
            print('好友聊天查询信息校验失败', format(e))

    @allure.step('亲密关系-联系概况')
    def check_intimacy_contact1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self
    
    @allure.step('亲密关系-联系概况')
    def check_intimacy_contact2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('亲密关系-联系概况')
    def check_intimacy_contact3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert 'a1472XXX3043' in text
            print('联系概况信息校验完成')
            return self
        except Exception as e:
            print('联系概况信息校验失败', format(e))

    @allure.step('亲密关系-金钱往来')
    def check_intimacy_money1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self
    
    @allure.step('亲密关系-金钱往来')
    def check_intimacy_money2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('亲密关系-金钱往来')
    def check_intimacy_money3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '唐' in text
            print('金钱往来信息校验完成')
            return self
        except Exception as e:
            print('金钱往来信息校验失败', format(e))


    @allure.step('群组分析')
    def check_group_analysis1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self
    
    @allure.step('群组分析')
    def check_group_analysis2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('群组分析')
    def check_group_analysis3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '岁月' in text
            print('群组分析信息校验完成')
            return self
        except Exception as e:
            print('群组分析信息校验失败', format(e))

    @allure.step('异常聊天-删除聊天记录')
    def check_chat_delete_record1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self
    
    @allure.step('异常聊天-删除聊天记录')
    def check_chat_delete_record2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('异常聊天-删除聊天记录')
    def check_chat_delete_record3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '狐狸已成精' in text
            print('删除聊天记录信息校验完成')
            return self
        except Exception as e:
            print('删除聊天记录信息校验失败', format(e))

    @allure.step('好友动态')
    def check_friends_tends1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self
    
    @allure.step('好友动态')
    def check_friends_tends2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('好友动态')
    def check_friends_tends3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '君无戏言' in text
            print('好友动态信息校验完成')
            return self
        except Exception as e:
            print('好友动态信息校验失败', format(e))


    @allure.step('搜索记录')
    def check_search_records1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self
    
    @allure.step('搜索记录')
    def check_search_records2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        return self

    @allure.step('搜索记录')
    def check_search_records3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/communicationspage.yaml",time=10)  # 显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/communicationspage.yaml")
        try:
            assert '8:50:06' in text
            print('搜索记录信息校验完成')
            return self
        except Exception as e:
            print('搜索记录信息校验失败', format(e))







