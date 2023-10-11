#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
from time import sleep

import allure

# from LT_Web.page.Operationmodule.HomePage.rotation import Rotation
from LT_Web.page.basepagemodule.base_page import BasePage
from LT_Web.page.datamanagemodule.assemblepage import AssemblePage
from LT_Web.page.datamanagemodule.batchpage import BatchPage
from LT_Web.page.datamanagemodule.datauploadpage import DataUploadPage
from LT_Web.page.datamanagemodule.whitelistpage import WhiteListPage
from LT_Web.page.logpagemodule.logpage import LogPage
from LT_Web.page.superportraitmodule.superpersonpage import SuperPersonPage
from LT_Web.page.thematic_analysis_module.Alipay_module.AlipayAssociationPage import AlipayAssociationPage
from LT_Web.page.thematic_analysis_module.Alipay_module.AlipayEnterprisePage import AlipayEnterprisePage
from LT_Web.page.thematic_analysis_module.Alipay_module.AlipayFundPage import AlipayFundPage
from LT_Web.page.thematic_analysis_module.Alipay_module.AlipayIPPage import AlipayIPPage
from LT_Web.page.thematic_analysis_module.Alipay_module.AlipayPerspectivePage import AlipayPerspectivePage
from LT_Web.page.thematic_analysis_module.Alipay_module.AlipayPhonePage import AlipayPhonePage
from LT_Web.page.thematic_analysis_module.Alipay_module.AlipayTitlePage import AlipayTitlePage
from LT_Web.page.thematic_analysis_module.Logistics_module.OriginalDataPage import OriginalDataPage
from LT_Web.page.thematic_analysis_module.Logistics_module.OriginalSuspiciousBehaviorPage import \
    OriginalSuspiciousBehaviorPage
from LT_Web.page.thematic_analysis_module.Toolbox_module.ConsolidationTablePage import ConsolidationTablePage
from LT_Web.page.thematic_analysis_module.Toolbox_module.WideTablePage import WideTablePage
from LT_Web.page.thematic_analysis_module.WeChat_module.WeChatAssociationPage import WeChatAssociationPage
from LT_Web.page.thematic_analysis_module.WeChat_module.WeChatConsumptionPage import WeChatConsumptionPage
from LT_Web.page.thematic_analysis_module.WeChat_module.WeChatOriginalPage import WeChatOriginalPage
from LT_Web.page.thematic_analysis_module.communications_module.CallRelationshipPage import CallRelationshipPage
from LT_Web.page.thematic_analysis_module.communications_module.ChatPage import ChatPage
from LT_Web.page.thematic_analysis_module.communications_module.RawDataQueryPage import RawDataQueryPage
from LT_Web.page.thematic_analysis_module.fund_module.suspiciousbehaviorpage import SuspiciousBehaviorPage
from LT_Web.page.thematic_analysis_module.fund_module.traceabilitypage import TraceabilityPage
from LT_Web.page.thematic_analysis_module.fund_module.NetFlowDirectionPage import NetFlowDirectionPage
from LT_Web.page.thematic_analysis_module.phone_module.annexpage import AnnexPage
from LT_Web.page.thematic_analysis_module.phone_module.communicationspage import CommunicationsPage
from LT_Web.page.thematic_analysis_module.phone_module.dataimagepage import DataImagePage
from LT_Web.page.thematic_analysis_module.phone_module.fulltextsearchpage import FullTextsearchPage
from LT_Web.page.thematic_analysis_module.fund_module.rawdatapage import RawDataPage
from LT_Web.page.thematic_analysis_module.phone_module.sequentialpage import SequentialPage
from LT_Web.page.thematic_analysis_module.phone_module.transactionpage import TransactionPage

'''案件首页'''
class HomePage(BasePage):

    @allure.step('首次进入弹窗点击-调证数据导入')
    def click_data_import1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        # return Operation(self._driver)#进运营管理
        return DataUploadPage(self._driver)


    @allure.step('弹窗点击-取证数据导入')
    def click_data_import2(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)  # 显示等待
        text = self.steps("../data/homepage.yaml")
        # return Operation(self._driver)#进运营管理
        return text

    @allure.step('点击取证报告导入')
    def click_upload_quzheng(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)  # 显示等待
        self.steps("../data/homepage.yaml")
        # return Operation(self._driver)#进运营管理
        return DataUploadPage(self._driver)

    @allure.step('点击刷新主题库')   
    def click_update_data(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return self

    @allure.step('点刷新调证批次数据')   
    def click_update_diaozheng_data(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return self

    @allure.step('刷新取证批次数据')   
    def click_update_quzheng_data(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return self

    @allure.step('点击刷新图库')   
    def click_update_picture_data1(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return self

    @allure.step('点击刷新图库-确定')   
    def click_update_picture_data2(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return self

    @allure.step('点击导入日志列表')   
    def click_logpage(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return LogPage(self._driver)

    @allure.step('点击超级画像')   
    def click_super_portrait(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return SuperPersonPage(self._driver)

    @allure.step('点击专题分析-手机取证分析-数据画像')   
    def click_thematic_phone_image(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return DataImagePage(self._driver)

    @allure.step('点击专题分析-手机取证分析-通联分析')
    def click_thematic_phone_communications(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return CommunicationsPage(self._driver)

    @allure.step('点击专题分析-手机取证分析-交易分析')
    def click_thematic_phone_transaction(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return TransactionPage(self._driver)


    @allure.step('点击专题分析-手机取证分析-时序分析')
    def click_thematic_phone_sequential(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return SequentialPage(self._driver)

    @allure.step('点击专题分析-手机取证分析-附件分析')
    def click_thematic_annex(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AnnexPage(self._driver)

    @allure.step('点击专题分析-手机取证分析-全文检索')
    def click_thematic_fulltext_searching(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return FullTextsearchPage(self._driver)

    @allure.step('点击专题分析-资金专题分析-原始数据查询')
    def click_fund_fulltext_raw_data(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return RawDataPage(self._driver)

    @allure.step('点击专题分析-资金专题分析-可疑行为分析')
    def click_fund_suspicious_behavior(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return SuspiciousBehaviorPage(self._driver)

    @allure.step('点击专题分析-资金专题分析-资金溯源分析')
    def click_fund_traceability(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return TraceabilityPage(self._driver)

    @allure.step('点击专题分析-资金专题分析-资金净流向分析')
    def click_fund_net_flow_direction(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return NetFlowDirectionPage(self._driver)


    @allure.step('点击专题分析-通联分析-原始数据查询')
    def click_communications_raw_data_query(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return RawDataQueryPage(self._driver)

    @allure.step('点击专题分析-通联分析-通话关系分析')
    def click_communications_call_relationship(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return CallRelationshipPage(self._driver)

    @allure.step('点击专题分析-通联分析-聊天分析')
    def click_communications_call_chat(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return ChatPage(self._driver)

    @allure.step('点击专题分析-物流分析-物流原始数据')
    def click_logistics_original_data(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return OriginalDataPage(self._driver)

    @allure.step('点击专题分析-物流分析-可疑行为分析')
    def click_logistics_suspicious_behavior(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return OriginalSuspiciousBehaviorPage(self._driver)

    @allure.step('点击专题分析-微信分析-原始数据查询')
    def click_WeChat_original_data(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return WeChatOriginalPage(self._driver)

    @allure.step('点击专题分析-微信分析-关联分析')
    def click_WeChat_association(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return WeChatAssociationPage(self._driver)

    @allure.step('点击专题分析-微信分析-消费分析')
    def click_WeChat_consumption(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return WeChatConsumptionPage(self._driver)

    @allure.step('点击专题分析-支付宝分析-数据关联')
    def click_Alipay_association(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AlipayAssociationPage(self._driver)

    @allure.step('点击专题分析-支付宝分析-IP分析')
    def click_Alipay_IP(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AlipayIPPage(self._driver)

    @allure.step('点击专题分析-支付宝分析-关联手机分析')
    def click_Alipay_Phone(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AlipayPhonePage(self._driver)

    @allure.step('点击专题分析-支付宝分析-资金规律分析')
    def click_Alipay_fund(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AlipayFundPage(self._driver)

    @allure.step('点击专题分析-支付宝分析-消费标题分析')
    def click_Alipay_Title(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AlipayTitlePage(self._driver)

    @allure.step('点击专题分析-支付宝分析-透视分析')
    def click_Alipay_perspective(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AlipayPerspectivePage(self._driver)

    @allure.step('点击专题分析-支付宝分析-企业支付宝分析')
    def click_Alipay_Enterprise(self):
        sleep(2)
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AlipayEnterprisePage(self._driver)


#####################################################################################################################################################################################
    @allure.step('点击调证管理')
    def click_data(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return self

    @allure.step('点击批次')
    def click_batch(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(2)
        return BatchPage(self._driver)

    @allure.step('点击案件白名单')
    def click_white_list(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        # sleep(2)
        return WhiteListPage(self._driver)

    @allure.step('点击集合管理')
    def click_assemble(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AssemblePage(self._driver)
#=====================================================
    @allure.step('点击支付宝分析')
    def click_Alipay(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AssemblePage(self._driver)

    @allure.step('点击原始数据验证')
    def c(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AssemblePage(self._driver)

    @allure.step('点击数据关联')
    def click_data_association(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AssemblePage(self._driver)

    @allure.step('点击IP分析')
    def click_IP_analysis(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AssemblePage(self._driver)

    @allure.step('点击关联手机分析')
    def click_relation_phone(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AssemblePage(self._driver)

    @allure.step('点击企业支付宝分析')
    def click_enterprise_Alipay(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AssemblePage(self._driver)

    @allure.step('点击资金规律分析')
    def click_capital_law(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AssemblePage(self._driver)

    @allure.step('点击消费标题分析')
    def click_consume_title(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AssemblePage(self._driver)

    @allure.step('点击透视分析')
    def click_perspective(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return AssemblePage(self._driver)

    @allure.step('分析时光轴')
    def click_time_axis(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-支付宝')
    def click_time_axis_Alipay(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-银行卡')
    def click_time_axis_BankCard(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-话单')
    def click_time_axis_cdr(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-财付通')
    def click_time_axis_tenpay(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-物流')
    def click_time_axis_logistics(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-微信')
    def click_time_axis_WeChat(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-网技数据')
    def click_time_axis_Network(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-取证报告')
    def click_time_axis_Forensic_report(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-其它')
    def click_time_axis_other(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-沉淀库')
    def click_time_axis_Sedimentation_tank(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-Telegram')
    def click_time_axis_Telegram(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击分析时光轴-网约车')
    def click_time_axis_car_hailing(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        sleep(1)
        return self

    @allure.step('点击工具箱-制作并表')
    def click_toolbox_consolidate(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return ConsolidationTablePage(self._driver)


    @allure.step('点击工具箱-制作宽表')
    def click_toolbox_wide_table(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return WideTablePage(self._driver)


    @allure.step('点击工具箱-Excel清洗')
    def click_toolbox_Excel(self):
        # self.set_implicitly(10)  # 隐式等待
        self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return ConsolidationTablePage(self._driver)


    @allure.step('点击工具箱-手工绘图')
    def click_toolbox_drawing(self):
        self.set_implicitly(10)  # 隐式等待
        # self.webdriver_wait(path="../data/homepage.yaml", time=10)#显示等待
        self.steps("../data/homepage.yaml")
        return ConsolidationTablePage(self._driver)












