#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
import inspect
import json
import logging
import re
import string
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:

    _params = {}

    def __init__(self, driver: webdriver = None):
        self._driver = driver


    #返回上级页面：
    def reback(self):
        self._driver.back()
    #隐式等待：
    def set_implicitly(self, time):
        self._driver.implicitly_wait(time)

    # 显示等待：判断元素是否可点击
    def webdriver_wait(self, path, time):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function  # 获取当前代码、上级代码方法名,获取当前代码、上级代码modole名称
            # print(name)
            steps = yaml.safe_load(f)[name]  # 读取yaml文件
        for step in steps:
            # print(step)
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:#判断元素是否可点击
                    WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable((step["by"], step["locator"])))
                if "see" == action:#判断元素是否可见
                    WebDriverWait(self._driver, time).until(expected_conditions.visibility_of_element_located((step["by"], step["locator"])))

    # 查找元素：
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    # 查找元素组：
    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    #封装测试步骤
    def steps(self,path):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function#获取当前代码、上级代码方法名,获取当前代码、上级代码modole名称
            # print(name)
            steps = yaml.safe_load(f)[name]#读取yaml文件
        raw = json.dumps(steps)#json序列化
        for key, value in self._params.items():
            raw = raw.replace('${' + key + '}', value)#方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
            print(raw)
        steps = json.loads(raw)#json反序列化
        for step in steps:
            # print(step)
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "send-enter" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                    # driver = webdriver.Chrome()
                    ActionChains(self._driver).send_keys(Keys.ENTER).perform()  # 回车键
                    sleep(1)
                if "send_submit" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                    # self._driver.keyevent(84)
                    # self._driver.press_keycode(84)
                    self._driver.press_keycode(66)#模拟键盘回车键

                if "roll" == action:
                    #滚动查找元素
                    text = step["locator"]
                    self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               f'scrollIntoView(new UiSelector().text("{text}")'
                                                               '.instance(0));')
                if "roll_click" == action:
                    #滚动查找元素并点击
                    ele = self.find(step["by"], step["locator"])
                    self._driver.execute_script("arguments[0].scrollIntoView();", ele)  # 滚动至元素ele可见
                    ele.click()

                if "roll_check" == action:
                    #首页滚动查找元素，scrollable(true).instance(1)中的1代表第二个scrollable=true的控件
                    #new UiSelector().text()，new UiSelector().resourceId() 或者组合查询new UiSelector().text().resourceId()
                    #textContains(String text)控件text属性包含的内容
                    text = step["locator"]
                    self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(1)).'
                                                               f'scrollIntoView(new UiSelector().text("{text}")'
                                                               '.instance(0));')
                if "exam_click" == action:#课程考试
                    WebDriverWait(self._driver, 10).until(
                        expected_conditions.element_to_be_clickable((step["by"], step["locator2"])))#显示等待开始考试按钮
                    num = self.find(step["by"], step["locator1"]).text
                    number = re.sub("\D", "", num)#获取出题数
                    # print(int(number))
                    self.find(step["by"], step["locator2"]).click()#点击开始考试按钮
                    for i in range(int(number)):
                        # print(i)
                        WebDriverWait(self._driver, 10).until(
                            expected_conditions.visibility_of_element_located((step["by"], step["locator3"])))#显示等待选项按钮
                        self.find(step["by"], step["locator3"]).click()#选择A
                        en_able = self.find(step["by"], step["locator5"]).is_enabled()#确定按钮是否可点击
                        while en_able:#判断en_able是否为true
                            self.find(step["by"], step["locator5"]).click()#点击确定
                            break
                        else:
                            self.find(step["by"], step["locator4"]).click()  # 选择B
                            self.find(step["by"], step["locator5"]).click()  # 点击确定
                            # break
                            continue
                if "upload_picture" == action:#查找相册图片，并上传
                    images  = self.finds(step["by"], step["locator"])
                    images[2].click()

                if "text" == action:#获取元素文本信息
                    text_message = self.find(step["by"], step["locator"]).text
                    # print(text_message)
                    return text_message

                if "len > 0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0

                # 获取全部页面句柄，切换到当前最新打开的窗口
                if "change" == action:
                    all_handles = self._driver.window_handles
                    # print(all_handles)
                    self._driver.switch_to.window(all_handles[step["locator"]])

                # 鼠标悬停
                if "hover" == action:
                    element = self._driver.find_element(step["by"], step["locator"])
                    ActionChains(self._driver).move_to_element(element).perform()

                # 鼠标右键点击
                if "right_click" == action:
                    ActionChains(self._driver).context_click(self._driver.find_element(step["by"], step["locator"])).perform()

                # 模拟键盘回车键
                if "enter_click" == action:
                    element = self._driver.find_element(step["by"], step["locator"])
                    element.send_keys(Keys.ENTER)

                # 模拟键盘删除键
                if "back_click" == action:
                    element = self._driver.find_element(step["by"], step["locator"])
                    element.send_keys(Keys.BACK_SPACE)

                # 模拟键盘方向下键
                if "ARROW_DOWN" == action:
                    element = self._driver.find_element(step["by"], step["locator"])
                    element.send_keys(Keys.ARROW_DOWN)


