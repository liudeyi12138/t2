#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage


'''专题分析-手机取证分析-数据画像'''
class DataImagePage(BasePage):

    @allure.step('人物身份-基础信息')
    def check_people_basedata1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('人物身份-基础信息')
    def check_people_basedata2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '嫌疑人1' in text
            # print('Assertion test pass.')
            print('基础信息校验完成')
            return self
        except Exception as e:
            # print('Assertion test fail.', format(e))
            print('基础信息校验失败', format(e))

    @allure.step('人物身份-分析信息')
    def check_people_analysisdata1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('人物身份-分析信息')
    def check_people_analysisdata2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '2' in text
            # print('Assertion test pass.')
            print('分析信息校验完成')
            return self
        except Exception as e:
            # print('Assertion test fail.', format(e))
            print('分析信息校验失败', format(e))

    @allure.step('人物身份-应用信息')
    def check_people_applicationdata1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('人物身份-应用信息')
    def check_people_applicationdata2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '25' in text
            # print('Assertion test pass.')
            print('应用信息校验完成')
            return self
        except Exception as e:
            # print('Assertion test fail.', format(e))
            print('应用信息校验失败', format(e))

    @allure.step('人物身份-采集信息')
    def check_people_collectdata1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('人物身份-采集信息')
    def check_people_collectdata2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '73' in text
            print('采集信息校验完成')
            return self
        except Exception as e:
            print('采集信息校验失败', format(e))

    @allure.step('数据初析-好友')
    def check_data_friends1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-好友')
    def check_data_friends2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-好友')
    def check_data_friends3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '腾讯新闻' in text
            print('好友信息校验完成')
            return self
        except Exception as e:
            print('好友信息校验失败', format(e))

    @allure.step('数据初析-公众号')
    def check_data_official1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-公众号')
    def check_data_official2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-公众号')
    def check_data_official3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert 'QQ精选' in text
            print('公众号信息校验完成')
            return self
        except Exception as e:
            print('公众号信息校验失败', format(e))

    @allure.step('数据初析-群组')
    def check_data_group1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-群组')
    def check_data_group2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-群组')
    def check_data_group3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '驾驶员群' in text
            print('群组信息校验完成')
            return self
        except Exception as e:
            print('群组信息校验失败', format(e))

    @allure.step('数据初析-短信')
    def check_data_message1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-短信')
    def check_data_message2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-短信')
    def check_data_message3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '血' in text
            print('短信信息校验完成')
            return self
        except Exception as e:
            print('短信信息校验失败', format(e))

    @allure.step('数据初析-通话记录')
    def check_data_calllog1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-通话记录')
    def check_data_calllog2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-通话记录')
    def check_data_calllog3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '1518XXX2520' in text
            print('通话记录信息校验完成')
            return self
        except Exception as e:
            print('通话记录信息校验失败', format(e))

    @allure.step('数据初析-交易信息')
    def check_data_transaction1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-交易信息')
    def check_data_transaction2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-交易信息')
    def check_data_transaction3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '400' in text
            print('交易信息信息校验完成')
            return self
        except Exception as e:
            print('交易信息信息校验失败', format(e))

    @allure.step('数据初析-快递信息')
    def check_data_fastmail1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-快递信息')
    def check_data_fastmail2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    # @allure.step('数据初析-快递信息')
    # def check_data_fastmail3(self):
    #     sleep(2)
    #     self.set_implicitly(10)  # 隐式等待
    #     # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
    #     text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
    #     try:
    #         assert '400' in text
    #         print('快递信息信息校验完成')
    #         return self
    #     except Exception as e:
    #         print('快递信息信息校验失败', format(e))

    @allure.step('数据初析-文件信息')
    def check_data_file1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-文件信息')
    def check_data_file2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-文件信息')
    def check_data_file3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '音频' in text
            print('文件信息信息校验完成')
            return self
        except Exception as e:
            print('文件信息信息校验失败', format(e))
            
    @allure.step('数据初析-词云分析')
    def check_data_world1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-词云分析')
    def check_data_world2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-词云分析')
    def check_data_world3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-词云分析')
    def check_data_world4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '聊天' in text
            print('词云分析信息校验完成')
            return self
        except Exception as e:
            print('词云分析信息校验失败', format(e))
            
    @allure.step('数据初析-社交聊天')
    def check_data_talk1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-社交聊天')
    def check_data_talk2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-社交聊天')
    def check_data_talk3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-社交聊天')
    def check_data_talk4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '现场' in text
            print('社交聊天信息校验完成')
            return self
        except Exception as e:
            print('社交聊天信息校验失败', format(e))

    @allure.step('数据初析-行为习惯')
    def check_data_habit1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行为习惯')
    def check_data_habit2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行为习惯')
    def check_data_habit3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行为习惯')
    def check_data_habit4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行为习惯')
    def check_data_habit5(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行为习惯')
    def check_data_habit6(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行为习惯')
    def check_data_habit7(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行为习惯')
    def check_data_habit8(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行为习惯')
    def check_data_habit9(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行为习惯')
    def check_data_habit10(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行为习惯')
    def check_data_habit11(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行为习惯')
    def check_data_habit12(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self



    @allure.step('断言取证数据是否导入成功')
    def check_quzheng(self):
        sleep(1)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/logpage.yaml", time=10)#显示等待
        text = self.steps("../data/logpage.yaml")
        return text

    @allure.step('断言调证批次数据是否抽取成功')
    def check_update_diaozheng(self):
        sleep(5)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/logpage.yaml", time=10)#显示等待
        text = self.steps("../data/logpage.yaml")
        sleep(5)
        return text

    @allure.step('断言调调证次数据是否抽取成功')
    def check_update_quzheng(self):
        sleep(3)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/logpage.yaml", time=10)#显示等待
        text = self.steps("../data/logpage.yaml")
        return text

    @allure.step('断言图库数据是否抽取成功')
    def check_update_tuku(self):
        sleep(5)
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/logpage.yaml", time=10)#显示等待
        text = self.steps("../data/logpage.yaml")
        return text


    @allure.step('数据初析-行踪规律')
    def check_data_walk1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行踪规律')
    def check_data_walk2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行踪规律')
    def check_data_walk3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行踪规律')
    def check_data_walk4(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-行踪规律')
    def check_data_walk5(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-高频词语')
    def check_data_words1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-高频词语')
    def check_data_words2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-高频词语')
    def check_data_words3(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        try:
            assert '聊天' in text
            print('高频词语信息校验完成')
            return self
        except Exception as e:
            print('高频词语信息校验失败', format(e))

    @allure.step('数据初析-关系网络')
    def check_data_relationship_network1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-关系网络')
    def check_data_relationship_network2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-内容分析')
    def check_data_content1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self

    @allure.step('数据初析-内容分析')
    def check_data_content2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        text = self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        # print(text)
        try:
            assert '微信' in text
            print('内容分析信息校验完成')
            return self
        except Exception as e:
            print('内容分析信息校验失败', format(e))

    @allure.step('数据初析-情报挖掘')
    def check_data_gen1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/thematic_analysis_module/phone_module/dataimagepage.yaml", time=10)#显示等待
        self.steps("../data/thematic_analysis_module/phone_module/dataimagepage.yaml")
        return self










