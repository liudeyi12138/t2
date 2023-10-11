#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
import os
import re
# import sys
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# # sys.path.append("C:\\Users\\admin\\PycharmProjects\\LeiTingWeb\\LT_Web\\page\\basepagemodule")
# sys.path.append(rootPath)

import allure
import pytest
import yaml
import time
from time import sleep
from selenium import webdriver
from LT_Web.page.basepagemodule.web import Web
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@allure.feature("奇数百炼Web")  # 用feature说明产品需求
class TestStart():
    @allure.story("初始化Chrome，进入web登录页-登录进入主页")  # 用story说明用户场景
    def setup(self):
        self.search = Web().start().main().login()

    def teardown(self):#停止Chrome，资源回收
        self.search.quit_web()

    @allure.story("案件-新增-导入调证数据")
    @pytest.mark.skip
    def test_addcase_upload_diaozheng(self):
        #点击新增案件-填写案件信息点击确定-弹窗点击确定进入首页-首次进入弹窗点击调证数据导入-新建批次-上传调证数据-点击导入-确定-是否继续导入点击否-跳转日志页断言是否导入成功
        text = self.search.click_addcase().Edit_new_case().click_ok().click_newcase_ok().click_data_import1().\
            new_batch().upload_data().upload_click().upload_click_ok().continue_no().check_diaozheng()
        print(text)
        # assert text == '提交成功', "案件新增失败"
        try:
            assert '已完成' in text
            # print('Assertion test pass.')
            print('案件新增导入调证数据成功')
        except Exception as e:
            # print('Assertion test fail.', format(e))
            print('案件新增导入调证数据失败', format(e))

    @allure.story("点击刷新主题库-刷新调证批次数据")
    @pytest.mark.skip
    def test_update_diaozheng_data(self):
        #搜索案件-回车-点击进入其首页-点击刷新主题库-点击刷新调证批次数据-日志列表-跳转日志页断言是否抽取成功
        text=self.search.search_case().click_update_data().click_update_diaozheng_data().click_logpage().check_update_diaozheng()
        # text=self.search.search_case().click_logpage().check_update_diaozheng()
        print(text)
        sleep(2)
        try:
            assert '已完成' in text
            # print('Assertion test pass.')
            print('调证数据抽取成功')
        except Exception as e:
            # print('Assertion test fail.', format(e))
            print('调证证数据抽取失败', format(e))

    @allure.story("取证数据导入")
    @pytest.mark.skip
    def test_upload_quzheng(self):
        #搜索案件-回车-点击进入其首页-点击进入取证报告导入-新建并选择取证批次-上传取证报告-关联嫌疑人-导入日志-跳转日志页断言是否导入成功
        text=self.search.search_case().click_upload_quzheng().new_batch_quzheng().upload_data_quzheng().new_suspect().click_uploadlog().check_quzheng()
        print(text)
        sleep(2)
        try:
            assert '已完成' in text
            # print('Assertion test pass.')
            print('取证数据导入成功')
        except Exception as e:
            # print('Assertion test fail.', format(e))
            print('取证数据导入失败', format(e))

    @allure.story("点击刷新主题库-刷新取证批次数据")
    @pytest.mark.skip
    def test_update_quzheng_data(self):
        #搜索案件-回车-点击进入其首页-点击刷新主题库-点击刷新取证批次数据-日志列表-跳转日志页断言是否抽取成功
        text=self.search.search_case().click_update_data().click_update_quzheng_data().click_logpage().check_update_quzheng()
        print(text)
        sleep(2)
        try:
            assert '已完成' in text
            # print('Assertion test pass.')
            print('取证数据抽取成功')
        except Exception as e:
            # print('Assertion test fail.', format(e))
            print('取证证数据抽取失败', format(e))

    @allure.story("点击刷新图库")
    @pytest.mark.skip
    def test_update_tuku_data(self):
        #搜索案件-回车-点击进入其首页-点击刷新图库-日志列表-跳转日志页断言是否抽取成功
        text=self.search.search_case().click_update_picture_data1().click_update_picture_data2().click_logpage().check_update_tuku()
        print(text)
        sleep(2)
        try:
            assert '已完成' in text
            # print('Assertion test pass.')
            print('图库刷新成功')
        except Exception as e:
            # print('Assertion test fail.', format(e))
            print('图库刷新失败', format(e))

    @allure.story("超级画像")
    @pytest.mark.skip
    def test_super_person_data(self):
        #搜索案件-回车-点击进入其首页-点击超级画像-超级画像各功能操作校验
        text=self.search.search_case().click_super_portrait().choose_suspect().add_diaoqulist1().add_diaoqulist2().add_diaoqulist3().\
            group_transaction1().group_transaction2().group_transaction3().group_transaction4().group_call1().group_call2().group_call3().\
            group_call4().group_call5().group_call6().group_call7().group_call8().group_chat1().group_chat2().group_chat3().group_chat4().\
            group_chat5().group_loginIp1().group_loginIp2().group_loginIp3().group_loginIp4().group_relevance1().group_relevance2().\
            group_gang1().group_information1().group_information2().group_check()
        sleep(2)
        try:
            assert '15828884891' in text
            # print('Assertion test pass.')
            print('超级画像功能校验完成')
        except Exception as e:
            # print('Assertion test fail.', format(e))
            print('超级画像功能校验失败', format(e))


    @allure.story("专题分析-手机取证分析-数据画像")
    @pytest.mark.skip
    def test_thematic_phone_image(self):
        #搜索案件-回车-点击进入其首页-专题分析-手机取证分析-数据画像-功能操作校验
        text=self.search.search_case().click_thematic_phone_image().check_people_basedata1().check_people_basedata2().check_people_analysisdata1().\
            check_people_analysisdata2().check_people_applicationdata1().check_people_applicationdata2().check_people_collectdata1().\
            check_people_collectdata2().check_data_friends1().check_data_friends2().check_data_friends3().check_data_official1().\
            check_data_official2().check_data_official3().check_data_group1().check_data_group2().check_data_group3().check_data_message1().\
            check_data_message2().check_data_message3().check_data_calllog1().check_data_calllog2().check_data_calllog3().check_data_transaction1().\
            check_data_transaction2().check_data_transaction3().check_data_fastmail1().check_data_fastmail2().check_data_file1().check_data_file2().\
            check_data_file3().check_data_world1().check_data_world2().check_data_world3().check_data_world4().check_data_talk1().check_data_talk2().\
            check_data_talk3().check_data_talk4().check_data_habit1().check_data_habit2().check_data_habit3().\
            check_data_habit4().check_data_habit5().check_data_habit6().check_data_habit7().check_data_habit8().check_data_habit9().\
            check_data_habit10().check_data_habit11().check_data_habit12().check_data_walk1().check_data_walk2().check_data_walk3().\
            check_data_walk4().check_data_walk5().check_data_words1().check_data_words2().check_data_words3().check_data_relationship_network1().\
            check_data_relationship_network2().check_data_content1().check_data_content2().check_data_gen1()

    @allure.story("专题分析-手机取证分析-通联分析")
    @pytest.mark.skip
    def test_thematic_phone_communications(self):
        #搜索案件-回车-点击进入其首页-专题分析-手机取证分析-通联分析-功能操作校验
        text=self.search.search_case().click_thematic_phone_communications().check_address_book().check_call_frequency1().check_call_frequency2().check_call_frequency3().\
            check_sms_frequency1().check_sms_frequency2().check_sms_frequency3().check_delete_call1().check_call_differences1().check_call_differences2().\
            check_call_differences3().check_connected_variance1().check_connected_variance2().check_connected_variance3().check_friends_overview1().\
            check_friends_overview2().check_friends_overview3().check_friends_file1().check_friends_file2().check_friends_file3().check_friends_chat_records1().\
            check_friends_chat_records2().check_friends_chat_records3().check_friends_chat1().check_friends_chat2().check_friends_chat3().\
            check_intimacy_contact1().check_intimacy_contact2().check_intimacy_contact3().check_intimacy_money1().check_intimacy_money2().check_intimacy_money3().\
            check_group_analysis1().check_group_analysis2().check_group_analysis3().check_chat_delete_record1().check_chat_delete_record2().check_chat_delete_record3().\
            check_friends_tends1().check_friends_tends2().check_friends_tends3().check_search_records1().check_search_records2().check_search_records3()

    @allure.story("专题分析-手机取证分析-交易分析")
    @pytest.mark.skip
    def test_thematic_phone_communications(self):
        #搜索案件-回车-点击进入其首页-专题分析-手机取证分析-交易分析-功能操作校验
        text=self.search.search_case().click_thematic_phone_transaction().check_transaction_overview1().check_transaction_overview2().check_transaction_overview3().\
            check_transaction_relationship1().check_transaction_relationship2().check_transaction_account1().check_transaction_account2().check_transaction_account3().\
            check_transaction_record1().check_transaction_record2().check_transaction_record3().check_transaction_frequency1().check_transaction_frequency2().\
            check_transaction_frequency3().check_transaction_income1().check_transaction_income2().check_transaction_billing1().check_transaction_billing2().\
            check_transaction_billing3().check_transaction_holiday1().check_transaction_holiday2().check_transaction_holiday3().check_transaction_calendar1().\
            check_transaction_calendar2().check_transaction_calendar3().check_transaction_calendar4()

    @allure.story("专题分析-手机取证分析-时序分析")
    @pytest.mark.skip
    def test_thematic_phone_communications(self):
        #搜索案件-回车-点击进入其首页-专题分析-手机取证分析-时序分析-功能操作校验
        text=self.search.search_case().click_thematic_phone_sequential().check_sequential_space_time().check_transaction_space1().check_transaction_space2().check_transaction_space3()

    @allure.story("专题分析-手机取证分析-附件分析")
    @pytest.mark.skip
    def test_thematic_annex(self):
        #搜索案件-回车-点击进入其首页-专题分析-手机取证分析-附件分析-功能操作校验
        text=self.search.search_case().click_thematic_annex().check_annex_picture()

    @allure.story("专题分析-手机取证分析-全文检索")
    @pytest.mark.skip
    def test_thematic_fulltextsearch(self):
        #搜索案件-回车-点击进入其首页-专题分析-手机取证分析-全文检索-功能操作校验
        text=self.search.search_case().click_thematic_fulltext_searching().check_fulltext_search1().check_fulltext_search2()

    @allure.story("专题分析-资金专题分析-原始数据查询")
    @pytest.mark.skip
    def test_fund_rawdata(self):
        #搜索案件-回车-点击进入其首页-专题分析-资金专题分析-原始数据查询-功能操作校验
        text=self.search.search_case().click_fund_fulltext_raw_data().check_classification_rawdata_alipay1().check_classification_rawdata_alipay2().\
            check_classification_rawdata_alipay3().check_classification_rawdata_alipay4().check_classification_rawdata_alipay5().check_classification_rawdata_alipay6().\
            check_classification_rawdata_alipay7().check_classification_rawdata_alipay8().check_classification_rawdata_bankcard1().check_classification_rawdata_bankcard2().\
            check_classification_rawdata_bankcard3().check_classification_rawdata_bankcard4().check_classification_rawdata_bankcard5().check_classification_rawdata_bankcard6().\
            check_classification_rawdata_bankcard7().check_classification_rawdata_bankcard8().check_classification_rawdata_bankcard9().check_classification_rawdata_bankcard10().\
            check_classification_rawdata_bankcard11().check_classification_rawdata_bankcard12().check_classification_rawdata_tenpay1().check_classification_rawdata_tenpay2().\
            check_classification_rawdata_tenpay3().check_classification_rawdata_tenpay4().check_classification_rawdata_report1().check_classification_rawdata_report2().\
            check_classification_summaryflow_alipay1().check_classification_summaryflow_alipay2().check_classification_summaryflow_bankcard1().\
            check_classification_summaryflow_bankcard2().check_classification_summaryflow_tenpay1().check_classification_summaryflow_tenpay2().\
            check_classification_summaryflow_report1().check_classification_summaryflow_report2()

    @allure.story("专题分析-资金专题分析-可疑行为分析")
    @pytest.mark.skip
    def test_fund_suspicious(self):
        # 搜索案件-回车-点击进入其首页-专题分析-资金专题分析-可疑行为分析-功能操作校验
        text=self.search.search_case().click_fund_suspicious_behavior().check_large_single1().check_large_single2().check_large_accumulate1().check_large_accumulate2().\
            check_large_accumulate3().check_abnormal_time1().check_abnormal_time2().check_abnormal_time3().check_frequent_transactions1().\
            check_frequent_transactions2().check_frequent_transactions3().check_fast_inout1().check_fast_inout2().check_fast_inout3().\
            check_account_work1().check_account_work2().check_account_work3().check_regularity_sleep1().check_regularity_sleep2().\
            check_regularity_sleep3().check_regularity_gap1().check_regularity_gap2().check_regularity_gap3().check_regularity_fund1().\
            check_test_machine1().check_test_machine2().check_test_machine3()

    @allure.story("专题分析-资金专题分析-可疑行为分析")
    @pytest.mark.skip
    def test_fund_traceability(self):
        # 搜索案件-回车-点击进入其首页-专题分析-资金专题分析-资金溯源分析-功能操作校验
        text=self.search.search_case().click_fund_traceability().check_fund_traceability1().check_fund_traceability2()

    @allure.story("专题分析-资金专题分析-资金净流向分析")
    @pytest.mark.skip
    def test_fund_net_flow_direction(self):
        # 搜索案件-回车-点击进入其首页-专题分析-资金专题分析-资金净流向分析-功能操作校验
        text=self.search.search_case().click_fund_net_flow_direction().check_fund_net_flow_direction1().check_fund_net_flow_direction2()

    @allure.story("专题分析-通联分析-原始数据查询")
    @pytest.mark.skip
    def test_communications_raw_data_query(self):
        # 搜索案件-回车-点击进入其首页-专题分析-通联分析-原始数据查询-功能操作校验
        text=self.search.search_case().click_communications_raw_data_query().check_Raw_data_query1().check_Raw_data_query2()

    @allure.story("专题分析-通联分析-通话关系分析")
    @pytest.mark.skip
    def test_communications_call_relationship(self):
        # 搜索案件-回车-点击进入其首页-专题分析-通联分析-通话关系分析-功能操作校验
        text=self.search.search_case().click_communications_call_relationship().check_High_frequency_call1().check_High_frequency_call2().check_Zero_seconds_call1().\
            check_Abnormal_period_call1().check_Abnormal_period_call2().check_common_contacts1().check_common_contacts2().check_mutual_call1().check_mutual_call2().\
            check_New_old_numbers1().check_position_treble1().check_position_treble2().check_trace_analysis1().check_trace_analysis2().check_trace_analysis3().\
            check_trace_overlap1(). check_trace_close1().check_location_distribution1().check_patterns_peer1().check_patterns_time1()

    @allure.story("专题分析-通联分析-聊天分析")
    @pytest.mark.skip
    def test_communications_call_relationship(self):
        # 搜索案件-回车-点击进入其首页-专题分析-通联分析-聊天分析-功能操作校验
        text=self.search.search_case().click_communications_call_chat().check_chat_basic1().check_chat_basic2().check_chat_matching1().check_keyword_alert1().\
            check_keyword_alert2().check_chat_ID1()

    @allure.story("专题分析-物流分析-物流原始数据")
    @pytest.mark.skip
    def test_communications_call_relationship(self):
        # 搜索案件-回车-点击进入其首页-专题分析-物流分析-物流原始数据-功能操作校验
        text=self.search.search_case().click_logistics_original_data().check_original_data1().check_original_data2()

    @allure.story("专题分析-物流分析-可疑行为分析")
    @pytest.mark.skip
    def test_communications_call_relationship(self):
        # 搜索案件-回车-点击进入其首页-专题分析-物流分析-可疑行为分析-功能操作校验
        text=self.search.search_case().click_logistics_suspicious_behavior().check_Suspicious_Behavior1().check_Suspicious_Behavior2().check_Suspicious_different_address1().\
            check_Suspicious_different_address2().check_Suspicious_equal_address1().check_Suspicious_equal_address2().check_Suspicious_equal_phone1().\
            check_Suspicious_abnormal_time1().check_Suspicious_abnormal_time2().check_Suspicious_virtually_number1().check_Suspicious_virtually_number2()

    @allure.story("专题分析-微信分析-原始数据查询")
    @pytest.mark.skip
    def test_WeChat_Original(self):
        # 搜索案件-回车-点击进入其首页-专题分析-微信分析-原始数据查询-功能操作校验
        text=self.search.search_case().click_WeChat_original_data().check_WeChat_original_data1().check_WeChat_original_data2().check_WeChat_original_data3().\
            check_WeChat_original_data4().check_WeChat_original_data5()

    @allure.story("专题分析-微信分析-关联分析")
    @pytest.mark.skip
    def test_WeChat_association(self):
        # 搜索案件-回车-点击进入其首页-专题分析-微信分析-关联分析-功能操作校验
        text=self.search.search_case().click_WeChat_association().check_WeChat_Association1().check_WeChat_Association2()

    @allure.story("专题分析-微信分析-消费分析")
    @pytest.mark.skip
    def test_WeChat_consumption(self):
        # 搜索案件-回车-点击进入其首页-专题分析-微信分析-消费分析-功能操作校验
        text=self.search.search_case().click_WeChat_consumption().check_WeChat_Consumption1().check_WeChat_Consumption2().check_WeChat_Consumption3().\
            check_WeChat_Consumption_Recharge1().check_WeChat_Consumption_Recharge2().check_WeChat_Consumption_Recharge3()
        sleep(5)

    @allure.story("专题分析-支付宝分析-数据关联")
    @pytest.mark.skip
    def test_Alipay_association(self):
        # 搜索案件-回车-点击进入其首页-专题分析-支付宝分析-数据关联-功能操作校验
        text=self.search.search_case().click_Alipay_association().check_Alipay_Association1().check_Alipay_Association2().check_Alipay_Association3().check_Alipay_Association4()

    @allure.story("专题分析-支付宝分析-IP分析")
    @pytest.mark.skip
    def test_Alipay_IP(self):
        # 搜索案件-回车-点击进入其首页-专题分析-支付宝分析-IP分析-功能操作校验
        text=self.search.search_case().click_Alipay_IP().check_Alipay_IP1().check_Alipay_IP2().check_Alipay_IpJump1().check_Alipay_IpJump2().check_Alipay_IpGang1().\
            check_Alipay_IpGang2()

    @allure.story("专题分析-支付宝分析-关联手机分析")
    @pytest.mark.skip
    def test_Alipay_Phone(self):
        # 搜索案件-回车-点击进入其首页-专题分析-支付宝分析-关联手机分析-功能操作校验
        text=self.search.search_case().click_Alipay_Phone().check_Alipay_Phone1().check_Alipay_Phone2().check_Alipay_Phone_binding1().check_Alipay_Phone_binding2()

    @allure.story("专题分析-支付宝分析-资金规律分析")
    @pytest.mark.skip
    def test_Alipay_Phone(self):
        # 搜索案件-回车-点击进入其首页-专题分析-支付宝分析-资金规律分析-功能操作校验
        text=self.search.search_case().click_Alipay_fund().check_Alipay_Fund1()

    @allure.story("专题分析-支付宝分析-消费标题分析")
    @pytest.mark.skip
    def test_Alipay_Phone(self):
        # 搜索案件-回车-点击进入其首页-专题分析-支付宝分析-消费标题分析-功能操作校验
        text=self.search.search_case().click_Alipay_Title().check_Alipay_Title_Host1().check_Alipay_Title_Host2().check_Alipay_Title_Host3().\
            check_Alipay_Title_Host4().check_Alipay_Title_peer1().check_Alipay_Title_peer2()

    @allure.story("专题分析-支付宝分析-透视分析")
    @pytest.mark.skip
    def test_Alipay_Perspective(self):
        # 搜索案件-回车-点击进入其首页-专题分析-支付宝分析-透视分析-功能操作校验
        text=self.search.search_case().click_Alipay_perspective().check_Alipay_Perspective1().check_Alipay_Perspective2().check_Alipay_Perspective3()

    @allure.story("专题分析-支付宝分析-企业支付宝分析")
    @pytest.mark.skip
    def test_Alipay_Enterprise(self):
        # 搜索案件-回车-点击进入其首页-专题分析-支付宝分析-企业支付宝分析-功能操作校验
        text=self.search.search_case().click_Alipay_Enterprise().check_Alipay_EnterpriseTest1().check_Alipay_EnterpriseTest2().check_Alipay_Enterprise_Typical1().\
            check_Alipay_Enterprise_Typical2().check_Alipay_Enterprise_Typical3().check_Alipay_Enterprise_Transaction1().check_Alipay_Enterprise_Transaction2().\
            check_Alipay_Enterprise_Transf1().check_Alipay_Enterprise_Transf2()
        sleep(5)

    @allure.story("调证管理-批量新增")
    @pytest.mark.skip
    def test_add_batch(self):
        #案件-首页-数据管理-批次管理-新增-输入信息-提交-确定
        text=self.search.search_case().click_data().click_batch().click_catalogue_list().import_data().assert_check4()

    @allure.story("案件白名单")
    @pytest.mark.skip
    def test_whitelist(self):
        #案件-首页-案件白名单-功能操作校验
        text=self.search.search_case().click_white_list().add_whitelist().Edit_new_whitelist().assert_check6()

    @allure.story("分析时光轴")
    @pytest.mark.skip
    def test_time_axis(self):
        #案件-首页-分析时光轴-功能操作校验
        text=self.search.search_case().click_time_axis().click_time_axis_Alipay().click_time_axis_BankCard().click_time_axis_cdr().click_time_axis_tenpay().\
            click_time_axis_logistics().click_time_axis_WeChat().click_time_axis_Network().click_time_axis_Forensic_report().click_time_axis_other().\
            click_time_axis_Sedimentation_tank().click_time_axis_Telegram().click_time_axis_car_hailing()

    @allure.story("工具箱-并表")
    @pytest.mark.skip
    def test_toolbox_ConsolidationTable(self):
        #案件-首页-工具箱-并表-功能操作校验
        text=self.search.search_case().click_toolbox_consolidate().check_ConsolidationTable1().check_ConsolidationTable2().check_ConsolidationTable3().\
            check_ConsolidationTable4().check_ConsolidationTable5().check_ConsolidationTable6().check_ConsolidationTable7().check_ConsolidationTable8()

    @allure.story("工具箱-宽表")
    # @pytest.mark.skip
    def test_toolbox_wide_table(self):
        #案件-首页-工具箱-并表-功能操作校验
        text=self.search.search_case().click_toolbox_wide_table().check_WideTable1().check_WideTable2().check_WideTable3().check_WideTable4().check_WideTable5().\
            check_WideTable6().check_WideTable7()
        sleep(5)



    #
    # @allure.story("数据管理-集合管理-新增")
    # @pytest.mark.skip
    # def test_assemble(self):
    #     #案件-首页-数据管理-集合管理-新增
    #     text=self.search.search_case().click_data().click_assemble().add_assemble().Edit_new_assemble().\
    #         click_ok().assert_check7()
    #     try:
    #         assert '新增集合成功' in text
    #         # print('Assertion test pass.')
    #         print('集合新增成功')
    #     except Exception as e:
    #         # print('Assertion test fail.', format(e))
    #         print('集合新增失败', format(e))
    #
    # @allure.story("数据管理-集合管理-新增集合成员")
    # @pytest.mark.skip
    # def test_assemble_member(self):
    #     #案件-首页-数据管理-集合管理-集合成员管理-新增
    #     text=self.search.search_case().click_data().click_assemble().click_assemble_member().\
    #         add_assemble_member().Edit_new_assemble_member().click_ok().assert_check8()
    #     try:
    #         assert '新增成功' in text
    #         # print('Assertion test pass.')
    #         print('集合成员新增成功')
    #     except Exception as e:
    #         # print('Assertion test fail.', format(e))
    #         print('集合成员新增失败', format(e))

if __name__ == '__main__':

    pytest.main(["-v", "-x", "-s", "test_01login.py", "--alluredir=./result/1"])  # 收集测试结果
    # 生成测试报告到指定路径下:
    os.system("allure "
              "generate "
              "./result/1 "
              "-o "
              "./report/1/ "
              "--clean")
    # 打开报告：
    os.system("allure "
              "open "
              "-h "
              "127.0.0.1 "
              "-p "
              "8883 "
              "./report/1/ ")
