#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
import os

import pytest

import allure

@allure.feature("测试Dome")
class TestClass:

    @allure.story("测试用例 1")
    def test_one(self):

        x = "hello"

        assert 'h' in x

    @allure.story("测试用例 2")
    def test_two(self):

        x = "test"

        assert hasattr(x, 'check')

if __name__ == '__main__':
    pytest.main(["-v", "-x", "-s", "t2.py", "--alluredir=./result/2 "])  # 收集测试结果
    # 生成测试报告到指定路径下:
    os.system("allure "
              "generate "
              "./result/2 "
              "-o "
              "./report/2/ "
              "--clean ")
    # 打开报告：
    os.system("allure "
              "open "
              "-h "
              "127.0.0.1 "
              "-p "
              "8883 "
              "./report/2/ ")
