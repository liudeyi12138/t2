from time import sleep

import pyautogui as py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://192.168.30.101:10101/login')
driver.maximize_window()#最大化浏览器窗口
print('hello world')
# //*[@id="app"]/div/div[1]/form/div[2]/div/div/input
# //input[contains(@placeholder,'请输入用户名')]
# //*[@id="app"]/div/div[1]/form/div[4]/div/button
driver.find_element(By.XPATH,"//input[contains(@placeholder,'用户名')]").send_keys('ldy')
# sleep(2)
driver.find_element(By.XPATH,"//input[contains(@placeholder,'密码')]").send_keys('ldy12138')
# sleep(2)
driver.find_element(By.XPATH,"//span[contains(text(),'登 录')]").click()
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

s=driver.find_element(By.XPATH,"//*[@id='app']//input[contains(@placeholder,'请输入关键字')]").send_keys('自动化测试案件01')
# s.send_keys(Keys.ENTER)#回车键
ActionChains(driver).send_keys(Keys.ENTER).perform()#回车键
sleep(1)
driver.find_element(By.XPATH,'//*[@id="app"]//div[contains(text(),"自动化测试案件01")]').click()
# sleep(2)
# driver.find_element(By.XPATH,"//*[@class='el-submenu__title']//span[contains(text(),'数据管理')]").click()
# sleep(2)
# driver.find_element(By.XPATH,"//*[@role='menuitem']//span[contains(text(),'集合管理')]").click()
# sleep(1)
# driver.find_element(By.XPATH,"//*[@class='el-icon-plus']").click()#点击新增
# sleep(1)
# driver.find_element(By.XPATH,'//*[@class="el-form-item is-required"]//input').send_keys('自动化测试集合02')
# driver.find_element(By.XPATH,"//span[contains(text(),'提交')]").click()
# sleep(2)
# driver.find_element(By.XPATH,"//*[@class='el-message-box']//span[contains(text(),'确定')]").click()

# locator=(By.XPATH,"//*[@role='alert']//p[contains(text(),'新增集合成功')]")
# locator=(By.XPATH,"//*[@class='el-breadcrumb__item']//a[contains(text(),'首页')]")
# WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(locator))#显示等待元素可见
# msg = driver.find_element(By.XPATH,"//*[@role='alert']//p[contains(text(),'新增集合成功')]").text
# msg = driver.find_element(By.XPATH,"//*[@class='el-breadcrumb__item']//a[contains(text(),'首页')]").text
# print(msg)
sleep(3)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
# sleep(2)
# element = driver.find_element(By.XPATH, '//*[@class="ant-dropdown-link ant-dropdown-trigger"]//span[contains(text(),"数据导入")]')
# ActionChains(driver).move_to_element(element).perform()
# sleep(5)

# ele = driver.find_element(By.XPATH, "//*[@class='ant-layout-sider ant-layout-sider-dark layout-sider']//span[contains(text(),'导入日志列表')]")#点击导入日志列表
# driver.execute_async_script("arguments[0].click()",ele)

sleep(2)
# driver.find_element(By.XPATH,'//*[@id="components-layout-demo-custom-trigger"]/aside/div/ul/div[10]/li/span/a').click()


driver.find_element(By.XPATH,'//*[@class="ant-layout-sider-children"]//span[contains(text(),"超级画像")]/../..').click()
sleep(2)
driver.find_element(By.XPATH,"//*[@class='app-main']//div[@title='吴小钦']").click()
sleep(2)



print('111')
# driver.find_element(By.XPATH,"//*[@class='app-main']//a[contains(text(),'吴小钦')]").click(button='right')
# py.click("//*[@class='app-main']//a[contains(text(),'吴小钦')]",button='right')
t = driver.find_element(By.XPATH,"//*[@class='app-main']//a[contains(text(),'2088042888884838')]")
print(t.text)
# driver.find_element(By.XPATH,"//*[@class='app-main']//a[contains(text(),'2088042888884838')]").click()
sleep(2)
ActionChains(driver).context_click(t).perform()
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[13]/div/div/div/div[2]/div/div/div/div/div/div/ul/li[2]").click()
sleep(5)
print('222222')

