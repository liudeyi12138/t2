#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
import allure
from selenium import webdriver
from LT_Web.page.basepagemodule.base_page import BasePage
from LT_Web.page.main import Main


class Web(BasePage):
    @allure.step('启动Chrome')
    def start(self):
        self._driver = webdriver.Chrome()
        # self._driver.get('http://192.168.30.101:10101/login')
        self._driver.get('http://192.168.1.40:10009/login')
        self._driver.maximize_window()  # 将浏览器最大化显示
        return self

    #
    # def restart(self):
    #     pass
    #
    # def stop(self):
    #     self._driver.quit()

    def main(self) -> Main:
        return Main(self._driver)
