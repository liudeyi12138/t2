import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# sys.path.append("C:\\Users\\admin\\PycharmProjects\\LeiTingWeb\\LT_Web\\page\\basepagemodule")
sys.path.append(rootPath)
print(rootPath)

driver = webdriver.Chrome()
driver.get('http://192.168.1.40/#/login')
driver.maximize_window()#最大化浏览器窗口
print('hello world')
# //*[@id="app"]/div/div[1]/form/div[2]/div/div/input
# //input[contains(@placeholder,'请输入用户名')]
# //*[@id="app"]/div/div[1]/form/div[4]/div/button
driver.find_element(By.XPATH,"//input[contains(@placeholder,'请输入用户名')]").send_keys('admin')
# sleep(2)
driver.find_element(By.XPATH,"//input[contains(@placeholder,'请输入密码')]").send_keys('123456')
# sleep(2)
driver.find_element(By.XPATH,"//span[contains(text(),'登录')]").click()
sleep(1)
# driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/div[1]/div/div[1]/div[2]/button//span[contains(text(),'新建案件')]").click()
#
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys('自动化测试案件01')
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div[2]/form/div[4]/div/div/div/input').send_keys('2021-6-22')
# driver.find_element(By.XPATH,"//span[contains(text(),'提交')]").click()
# sleep(1)
# driver.find_element(By.XPATH,"//*[@class='el-message-box']//span[contains(text(),'确定')]").click()
# # # driver.find_element(By.XPATH,"//*[@role='alert']//p[contains(text(),'提交成功')]")
# # # loc=driver.find_element(By.XPATH,"//*[@role='alert']//p")
# # loc=driver.find_element(By.XPATH,"//*[@id="app"]/div/div[2]/div[1]/div/div[3]")
# # action_chains=ActionChains(driver)
# # action_chains.move_to_element(loc).perform()	#  鼠标悬浮在该弹窗，防止弹窗消失
# # message = driver.text(loc)	#  text（）获取弹窗元素文本
# # print(message)
# loc=driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/div[3]')
# action_chains=ActionChains(driver)
# action_chains.move_to_element(loc).perform()	#  鼠标悬浮
# #找到这个元素
# # ele = driver.find_element_by_xpath('//a[text()="_百度百科"]')
# #利用js将为元素设置焦点
# # driver.execute_script("arguments[0].focus();", loc)
# target = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/div[3]/div[1]/div[1]/div[1]/div[1]/span[contains(text(),"自动化测试案件01")]')
# driver.execute_script("arguments[0].scrollIntoView();", target)

s=driver.find_element(By.XPATH,"//*[@id='app']//input[contains(@placeholder,'请输入案件名称')]").send_keys('自动化测试案件01')
# s.send_keys(Keys.ENTER)#回车键
ActionChains(driver).send_keys(Keys.ENTER).perform()#回车键
sleep(1)
driver.find_element(By.XPATH,'//*[@id="app"]//span[contains(text(),"自动化测试案件01")]').click()
sleep(2)
driver.find_element(By.XPATH,"//*[@class='el-submenu__title']//span[contains(text(),'数据管理')]").click()
sleep(2)
driver.find_element(By.XPATH,"//*[@role='menuitem']//span[contains(text(),'批次管理')]").click()
# sleep(2)
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/button').click()
# time=10
# WebDriverWait(driver, time).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/button')))
# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div/div/button').click()

sleep(1)
# driver.find_element(By.XPATH,'//*[@class="el-form-item is-required"]//input').send_keys('自动化测试批次01')
# driver.find_element(By.XPATH,"//span[contains(text(),'提交')]").click()
# '//*[@class="cell"][contains(text(),"自动化测试批次01")]'
# '//*[@class="cell"][contains(text(),"自动化测试批次01")]/../../td[9]'
# '//*[@class="cell"][contains(text(),"自动化测试批次01")]/../../td[9]//button[4]'
driver.find_element(By.XPATH,'//*[@class="cell"][contains(text(),"自动化测试批次01")]/../../td[9]//button[1]').click()
# sleep(1)
# # 在单击链接之前，首先将窗口句柄存储为
# window_before = driver.window_handles[0]
# # 点击链接后，将新打开的窗口的窗口句柄作为
# window_after = driver.window_handles[1]
# # 然后执行切换到窗口方法以移动到新打开的窗口
sleep(1)
windows = driver.window_handles
# driver.switch_to_window(windows[-1])
driver.switch_to.window(windows[-1])
# driver.find_element(By.XPATH,"//*[@type='button']//span[contains(text(),'导入数据')]").click()

# driver.find_element(By.XPATH,'//*[@class="el-upload el-upload--text"]/input').send_keys('C:/Users/admin/Desktop/1测试痕迹调取目录.xlsx')
driver.find_element(By.XPATH,'//*[@class="uploadbox"]//input').send_keys('C:/Users/admin/Desktop/a')
driver.find_element(By.XPATH,'//*[@class="uploadbox"]//span[contains(text(),"清洗数据")]').click()
sleep(5)
ele = driver.find_element(By.XPATH,'//*[@class="tablebox"]//span[contains(text(),"导入")]')
driver.execute_script("arguments[0].scrollIntoView();", ele)  # 滚动至元素ele可见
sleep(5)
ele.click()

