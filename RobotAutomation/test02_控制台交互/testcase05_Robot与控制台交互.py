#
#
# from selenium import webdriver
# import unittest
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# # 引入 Keys 模块
# from selenium.webdriver.common.keys import Keys
# import win32gui, win32con
# import ctypes
# import pywinauto
# from pywinauto.keyboard import send_keys
# from selenium.webdriver.common.action_chains import ActionChains
#
# """
# 实现需求，控制台的登录，选择对应的租户，添加流程包，
# """
#
#
# class Setting:
#     driver = None
#     url = None
#
#
# def setUpModule():
#     Setting.driver = webdriver.Chrome()
#     Setting.driver.maximize_window()
#     Setting.driver.implicitly_wait(10)
#     Setting.url = "https://console.encoo.com/"
#
#
# def tearDownModule():
#     time.sleep(2)
#     Setting.driver.quit()
#
#
# class ConsoleTest(unittest.TestCase):
#     """从登录-->到流程包管理模块"""
#
#     def login(self):
#         Setting.driver.get(Setting.url)
#         Setting.driver.find_element_by_id('telphone').send_keys('15936558246')
#         Setting.driver.find_element_by_id('password').send_keys('123456')
#         Setting.driver.find_element_by_id('submitBtn').click()
#         Setting.driver.implicitly_wait(10)
#
#     def PackageManagement(self):
#         # 选择RPA管理
#         Setting.driver.find_element_by_xpath('//*[@id="root"]/div/div/aside/ul/li[2]/div/span[2]/span').click()
#
#     def XianshiWait(self, xpathroad):
#         try:
#             element = WebDriverWait(Setting.driver, 10, 0.5).until(
#                 EC.presence_of_element_located(
#                     (By.XPATH, f'{xpathroad}'))
#             )
#             return element
#         except:
#             return None
#
#     def test01_登录生产控制台(self):
#         '''登录云扩生产控制台'''
#         self.login()
#         title = Setting.driver.title
#         current_url = Setting.driver.current_url
#         self.assertEqual(title, "云扩控制台")
#         time.sleep(3)
#         # print('第1个', current_url)
#         self.assertIn('https://console.encoo.com/callback?code=', current_url)
#
#     def test02_选择租户(self):
#         '''登录控制台，选择所需的租户'''
#         time.sleep(3)
#         # print('第2个', Setting.driver.current_url)
#         self.assertEqual('https://console.encoo.com/userTenantEntrySelect', Setting.driver.current_url)
#
#     def test03_进入第三个企业版租户(self):
#         '''登录控制台，进入第三个企业版租户'''
#         # 尝试加一个显示等待
#         selenium_element = self.XianshiWait('//*[@id="root"]/main/div[2]/div/div[2]/div/div[4]/div[2]/button/span')
#         # print(333, selenium_element)
#         Setting.driver.find_element_by_xpath(
#             '//*[@id="root"]/main/div[2]/div/div[2]/div/div[4]/div[2]/button/span').click()
#         time.sleep(5)
#         # print('第3个', Setting.driver.current_url)
#         self.assertEqual('https://console.encoo.com/', Setting.driver.current_url)
#
#     def test04_控制台流程包管理(self):
#         '''登录控制台，进入控制台流程包管理'''
#         # 选择RPA管理,
#         self.PackageManagement()
#         selenium_element = self.XianshiWait('//*[@id="menu.rpa.name$Menu"]/li[1]')
#         # print(444, selenium_element)
#         # 流程包管理
#         Setting.driver.find_element_by_xpath('//*[@id="menu.rpa.name$Menu"]/li[1]').click()
#         print('第4个', Setting.driver.current_url)
#         url = 'https://console.encoo.com/resourceGroup/f65d7a8a-561b-4a2e-94d8-d83207471349/package'
#         self.assertEqual(url, Setting.driver.current_url)
#
#     def test05_控制台选择上传(self):
#         '''控制台流程包管理，选择上传流程包功能'''
#
#         # 选择上传按钮，class的名称里面不能有空格，空格换成点即可
#         Setting.driver.find_element_by_class_name('ant-btn.ant-btn-primary.css-rrqrsx').click()
#         time.sleep(2)
#         # print('第5个', Setting.driver.current_url)
#         '''判断上传功能，是否打开了桌面窗口，如果有打开窗口，那么就说明上传按钮是成功有效的'''
#         hwnd_title = {}
#         def get_all_hwnd(hwnd, mouse):
#             if (win32gui.IsWindow(hwnd)) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
#                 hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
#         win32gui.EnumWindows(get_all_hwnd, 0)
#         a = '打开'
#         for hand in hwnd_title.values():
#             # print(hand)
#             if a in hand:
#                 # print('打开窗口通过')
#                 self.assertIn(a, hand)
#
#     def test06_打开桌面文件上传流程包(self):
#         '''控制台流程包管理，连接打开窗口上传流程包'''
#         open_desktop = pywinauto.Desktop()
#         desktop = open_desktop['打开']
#         desktop.maximize()
#         desktop['Toolbar3'].click()
#         time.sleep(2)
#         send_keys(r'C:\Users\bqm66\Desktop')
#         send_keys("{VK_RETURN}")
#         # 打开桌面后，选中文件名输入框，传值文件的名字，然后回车键上传成功
#         time.sleep(2)
#         desktop["文件名(&N):Edit"].type_keys("bianliang.dgs")
#         send_keys("{VK_RETURN}")
#         time.sleep(6)
#         # 选择 输入备注
#         selenium_element = self.XianshiWait('//*[@id="description"]')
#         print(6, selenium_element)
#         Setting.driver.find_element_by_id('description').send_keys('日志变量参数')
#         # 选择确定
#         road = '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]'
#         Setting.driver.find_element_by_xpath(road).click()
#         time.sleep(3)
#         # 流程包管理-判断文件上传成功呢？
#         text_content = Setting.driver.find_element_by_class_name('ant-table-tbody').text
#         # print('内容是>>>>>>', text_content)
#         self.assertIn('变量参数含日志', text_content)
#
#     def test07_切换到控制台流程部署(self):
#         '''选择切换到流程部署'''
#         # self.PackageManagement()  #后面这个流程部署的代码单独拉出去做成一个py文件
#         # 选择切换到流程部署
#         Setting.driver.find_element_by_xpath('//*[@id="menu.rpa.name$Menu"]/li[2]').click()
#         # print('第7个', Setting.driver.current_url)
#         url = 'https://console.encoo.com/resourceGroup/f65d7a8a-561b-4a2e-94d8-d83207471349/workflow'
#         self.assertEqual(url, Setting.driver.current_url)
#
#     def test08_控制台流程部署新建(self):
#         '''选择新建功能'''
#         # 选择新建按钮
#         Setting.driver.find_element_by_class_name('anticon.anticon-plus').click()
#         # 获取新建窗口元素
#         NewCreate = Setting.driver.find_element_by_class_name('ant-modal-content').get_attribute('textContent')
#         # print(NewCreate)
#         self.assertIn('新建', NewCreate)
#
#     def test09_编辑流程部署名称(self):
#         '''编辑流程部署对应名称'''
#         # 新建窗口编辑详细信息
#         from Settings.jia1 import numincreate
#         new_data = numincreate()
#         # print(new_data)
#         Setting.driver.find_element_by_id('name').send_keys(f'流程部署名称第{new_data}个')
#         time.sleep(2)
#         liuchengbushu_value = Setting.driver.find_element_by_id('name').get_attribute('value')
#         # print('流程部署的元素', liuchengbushu_value)
#         value = f'流程部署名称第{new_data}个'
#         # if value == liuchengbushu_value:
#         #     print('你们对上去了')
#         # else:
#         #     print('原来是我错误了')
#         self.assertEqual(value, liuchengbushu_value)
#         # 因为执行速度太快，所以这个地方要加一个时间延迟等待元素出现，不然会报元素找不到的错误
#         time.sleep(2)
#
#     def test10_编辑流程包名称(self):
#         """编辑流程包对应名称"""
#         # 先定位到流程包名称的input框实现点击，然后悬浮，之后选择对应的流程包
#         Setting.driver.find_element_by_id('packageId').click()
#         time.sleep(2)
#         mouse = Setting.driver.find_element_by_id('packageId')
#         # 流程包名称点击后选择到对应的“变量参数含日志”的流程包
#         ActionChains(Setting.driver).move_to_element(mouse).perform()
#         time.sleep(2)
#         # 点击选择到对应的“变量参数含日志”的流程包
#         Setting.driver.find_element_by_class_name('ant-select-item-option-content').click()
#         time.sleep(2)
#         # 获取流程包名称的div中所有页面元素
#         liuchengbao_value = Setting.driver.find_elements_by_class_name('ant-select-selector')[1].get_attribute(
#             'innerHTML')
#         elements = 'aria-expanded="false"'
#         # if elements in liuchengbao_value:
#         #     print('我在里面')
#         # else:
#         #     print('名称选择失败了')
#
#         self.assertIn(elements, liuchengbao_value)
#
#     def test11_编辑流程包版本(self):
#         """选择流程包对应版本号"""
#         # 先定位到流程包版本名称的input框实现点击，然后悬浮，之后选择对应的流程包
#         Setting.driver.find_element_by_id('packageVersionId').click()
#         time.sleep(2)
#         mouse = Setting.driver.find_element_by_id('packageVersionId')
#         # 流程包banben点击后选择到对应的“变量参数含日志”的流程包
#         ActionChains(Setting.driver).move_to_element(mouse).perform()
#         time.sleep(2)
#         # 点击选择到对应的“流程包版本”；我的实现思路是键盘上的快捷键传值
#         from selenium.webdriver.common.keys import Keys
#         Setting.driver.find_element_by_id('packageVersionId').send_keys(Keys.DOWN)
#         time.sleep(1)
#         Setting.driver.find_element_by_id('packageVersionId').send_keys(Keys.ENTER)
#         time.sleep(1)
#         # 获取流程banben的div中所有页面元素
#         version_classname = 'ant-select-selection-item'
#         liuchengbaoversion_value = Setting.driver.find_elements_by_class_name(version_classname)[2].get_attribute(
#             'innerHTML')
#         # print(liuchengbaoversion_value)
#         elements = '1.'
#         self.assertIn(elements, liuchengbaoversion_value)
#
#     def test12_编辑流程包失败最大尝试次数(self):
#         """将最大次数设置为0"""
#         # 先定位到流程包版本名称的input框实现点击，然后悬浮，之后选择对应的流程包
#         Setting.driver.find_element_by_id('maxRetryCount').send_keys(Keys.CONTROL, 'a')
#         Setting.driver.find_element_by_id('maxRetryCount').send_keys('0')
#         time.sleep(2)
#
#         # 获取失败最大尝试次数的元素
#         liuchengcishu_value = Setting.driver.find_elements_by_class_name('ant-input-number-input-wrap')[0].get_attribute(
#             'innerHTML')
#         # print('次数的元素',liuchengcishu_value)
#         elements = 'value="0"'
#         self.assertIn(elements, liuchengcishu_value)
#
#     def test13_编辑流程包布尔参数(self):
#         """下拉到最底部，对布尔默认值进行查询"""
#         time.sleep(2)
#         Setting.driver.execute_script("document.querySelector('.ant-modal-wrap').scrollTop = 5000")
#
#         road = "//td[text()='布尔']/following-sibling::td//input[@id='defaultValue']"
#         temp = Setting.driver.find_element_by_xpath(road).get_attribute('value')
#         print('你的值是：', temp)
#         self.assertEqual('False', temp)
#
#     def test14_编辑流程包数字参数(self):
#         """下拉到最底部，对数字默认值进行查询"""
#         road = "//td[text()='数字']/following-sibling::td//input[@id='defaultValue']"
#         temp = Setting.driver.find_element_by_xpath(road).get_attribute('value')
#         print('你的值是：', temp, '类型', type(temp))
#         data_str = '1'
#         self.assertEqual(data_str, temp)
#
#     def test15_编辑流程包系统32参数(self):
#         """下拉到最底部，对系统32默认值进行查询"""
#         road = "//td[text()='系统32']/following-sibling::td//input[@id='defaultValue']"
#         temp = Setting.driver.find_element_by_xpath(road).get_attribute('value')
#         print('你的值是：', temp, '类型', type(temp))
#         data_str = '2'
#         self.assertEqual(data_str, temp)
#
#     def test16_编辑流程包系统64参数(self):
#         """下拉到最底部，对系统64默认值进行查询"""
#         road = "//td[text()='系统64']/following-sibling::td//input[@id='defaultValue']"
#         temp = Setting.driver.find_element_by_xpath(road).get_attribute('value')
#         print('你的值是：', temp, '类型', type(temp))
#         data_str = '3'
#         self.assertEqual(data_str, temp)
#
#     def test17_编辑流程包单文本参数(self):
#         """下拉到最底部，对单文本默认值进行查询"""
#         road = "//td[text()='单文本']/following-sibling::td//input[@id='defaultValue']"
#         temp = Setting.driver.find_element_by_xpath(road).get_attribute('value')
#         print('你的值是：', temp)
#         self.assertEqual('你好', temp)
#
#     def test18_编辑流程包日期参数(self):
#         """下拉到最底部，对日期默认值进行查询"""
#         road = "//td[text()='日期']/following-sibling::td//input[@id='defaultValue']"
#         temp = Setting.driver.find_element_by_xpath(road).get_attribute('value')
#         print('你的值是：', temp)
#         data_str = '2020-07-28 02:32:47'
#         self.assertEqual(data_str, temp)
#
#     def test19_编辑流程包增加参数string(self):
#         """下拉到最底部，对参数string默认值进行查询"""
#         road = "//td[text()='增加参数string']/following-sibling::td//input[@id='defaultValue']"
#         temp = Setting.driver.find_element_by_xpath(road).get_attribute('value')
#         print('你的值是：', temp)
#         data_str = '我不好'
#         self.assertEqual(data_str, temp)
#
#     def test20_编辑流程包增加参数32(self):
#         """下拉到最底部，对参数string默认值进行查询"""
#         road = "//td[text()='增加参数32']/following-sibling::td//input[@id='defaultValue']"
#         temp = Setting.driver.find_element_by_xpath(road).get_attribute('value')
#         print('你的值是：', temp, '类型', type(temp))
#         data_str = '4'
#         self.assertEqual(data_str, temp)
#
#     def test21_编辑流程包argument1(self):
#         """下拉到最底部，对参数argument1默认值进行查询"""
#         road = "//td[text()='argument1']/following-sibling::td//input[@id='defaultValue']"
#         temp = Setting.driver.find_element_by_xpath(road).get_attribute('value')
#         print('你的值是：', temp)
#         data_str = '我很好'
#         self.assertEqual(data_str, temp)
#
#     def test22_编辑流程包下一步(self):
#         """选择下一步操作,进行机器人选择"""
#         Setting.driver.find_element_by_xpath('//span[text()="下一步"]').click()
#         time.sleep(2)
#         content = Setting.driver.find_element_by_class_name('ant-modal-body').get_attribute('textContent')
#         print('指定机器人执行页面的文本内容', content)
#         data_str = '机器人执行'
#         self.assertIn(data_str, content)
#
#
#
#
# if __name__ == "__main__":
#     unittest.main()
#
#
#
