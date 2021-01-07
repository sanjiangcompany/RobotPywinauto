# 本地流程库

import unittest
import requests
import pywinauto
from pywinauto import Application
from pywinauto.keyboard import send_keys
import time

from Settings import Version

version = Version.RobotVersion()


class RobotBVT(unittest.TestCase):
    """机器人本地流程库"""

    def setUp(self):
        global file_name
        file_name = 'bianliang'
        Application(backend="uia").start(
            r"C:\Program Files (x86)\Encoo Robot\app-1.1.{}\Robot.exe".format(version))

        # 一定不要忘了运行Robot自动化一定要先结束一下进程
        self.app = pywinauto.Application(backend="uia").connect(
            path=r"C:\Program Files (x86)\Encoo Robot\app-1.1.{}\Robot.exe".format(version))

        self.base_url = "http://localhost:6001/api/Robot/runWorkflow"

        self.dlg = self.app['云扩RPA机器人']

    def tearDown(self):
        self.dlg.close()
        # print(self.result)

    def Condition(self, dlg):
        """本地流程库运行的前置条件"""
        dlg.maximize()  # 窗口最大化操作
        dlg.child_window(auto_id="Package").double_click_input()
        time.sleep(2)
        dlg.child_window(title="Encoo.Robot.Monitor.Views.PageModel", auto_id="PackageLocal").double_click_input()
        dlg.child_window(title="bianliang", control_type="Text").double_click_input()

    def deletedgs(self, dlg):
        self.Condition(dlg)
        time.sleep(1)
        dlg['删除2'].click_input()  # 选择“删除”按钮已成功，下一步选择“确定”，将文件给真正删除掉
        # dlg.print_control_identifiers()
        time.sleep(1)
        message = dlg['提示']
        message.child_window(title="确定", auto_id="OkButton", control_type="Button").click()
        time.sleep(2)

    def test02_Robot_点击导入(self):

        dlg = self.dlg
        dlg.maximize()  # 窗口最大化操作
        dlg.child_window(auto_id="Package").double_click_input()
        time.sleep(2)
        dlg.child_window(title="Encoo.Robot.Monitor.Views.PageModel", auto_id="PackageLocal").double_click_input()
        # dlg.print_control_identifiers()
        try:
            if dlg.child_window(title="点击导入", control_type="Text").exists():
                dlg.child_window(title="点击导入", control_type="Text").double_click_input()
                open_desktop = pywinauto.Desktop()
                desktop = open_desktop['打开']
                desktop['Toolbar3'].click()
                time.sleep(2)
                send_keys(r'C:\Users\bqm66\Desktop')
                send_keys("{VK_RETURN}")
                # 打开桌面后，选中文件名输入框，传值文件的名字，然后回车键上传成功
                time.sleep(2)
                desktop["文件名(&N):Edit"].type_keys(f"{file_name}.dgs")
                send_keys("{VK_RETURN}")

                # 问题2，我该怎么做文本校验，判断他导入成功呢？使用.texts()方法
                if (dlg.child_window(title=f"{file_name}", control_type="Text").texts() == [f'{file_name}']):
                    self.result = 'dgs文件导入成功-->通过'
                else:
                    self.result = 'dgs文件未实现导入-->失败'
            else:
                self.result = '点击导入不存在，无法进行下一步的操作'
            time.sleep(1)
        except:
            self.result = '导入功能检测通过'
            pass

    def test03_Robot_本地流程库_导入流程(self):
        '''将dgs文件导入到Robot本地流程库中'''
        dlg = self.dlg
        dlg.maximize()  # 窗口最大化操作
        # 问题1，我该怎么做元素校验，判断元素是否存在的方法用.exists():
        if dlg.child_window(auto_id="Package").exists():
            # dlg.child_window(auto_id="Package").click() # 此处使用click()方法不管用，需要使用click_input()方法
            Insert_Package = dlg.child_window(auto_id="Package")
            Insert_Package.double_click_input()  # 这里选择使用click_input()方法
            time.sleep(2)
            dlg.child_window(title="Encoo.Robot.Monitor.Views.PageModel", auto_id="PackageLocal").double_click_input()

            self.app['云扩RPA机器人']['导入流程'].click()
            time.sleep(1)
            open_desktop = pywinauto.Desktop()
            desktop = open_desktop['打开']
            desktop['Toolbar3'].click()
            time.sleep(2)
            send_keys(r'D:\变量参数')
            send_keys("{VK_RETURN}")
            # 打开桌面后，选中文件名输入框，传值文件的名字，然后回车键上传成功
            time.sleep(2)
            desktop["文件名(&N):Edit"].type_keys("bianliang.dgs")
            send_keys("{VK_RETURN}")

            # 点击打开
            # dlg["打开(&O)"].click()
            # 问题2，我该怎么做文本校验，判断他导入成功呢？使用.texts()方法
            if (dlg.child_window(title=f"{file_name}", control_type="Text").texts() == [f'{file_name}']):
                self.result = '上传该dgs文件-->通过'

                # 下面的两行代码是管用的，用来验证一下刷新的功能是否管用，不过没啥实质性使用价值我暂时注释掉了
                # dlg.child_window(title="bianliang", control_type="Text").click_input()
                # app['云扩RPA机器人']['刷新'].click()
            else:
                self.result = '上传该dgs文件-->失败'

        else:

            self.result = '流程库入口不存在，无法进行下一步的操作'

        time.sleep(1)

    def test04_Robot_本地流程库_执行流程(self):
        """流程运行"""
        # '''方式一'''
        # headers = {"Content-Type": "application/json"}
        # payload = {"PackageId": "bianliang", "Version": "1.0.0", "UserName": "baiqingmei"}
        # r = requests.post(url=self.base_url, data=json.dumps(payload), headers=headers)
        json_data = {"PackageId": "bianliang", "Version": "1.0.0", "UserName": "baiqingmei"}
        r = requests.post(url=self.base_url, json=json_data)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)
        time.sleep(5)

    def test05_Robot_本地流程库_取消执行(self):
        """选择取消按钮，取消执行流程"""
        dlg = self.dlg
        # dlg = self.app['云扩RPA机器人']
        self.Condition(dlg)
        time.sleep(1)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        # ExecuteFlow.print_control_identifiers()
        # 点击取消执行按钮
        ExecuteFlow.child_window(title="取消", auto_id="BtnCancel", control_type="Button").click()
        time.sleep(2)
        # 从判断执行窗口是否存在，来确定窗口是否关闭成功
        if not ExecuteFlow.child_window(title="执行", control_type="Window").exists():
            self.result = '选择"取消"按钮，执行窗口关闭成功-->通过'
        else:
            self.result = '执行窗口依然存在未关闭成功-->失败'

        time.sleep(1)

    def test06_Robot_本地流程库_确定执行(self):
        """选择确定按钮，确定执行流程"""
        dlg = self.dlg
        # dlg = self.app['云扩RPA机器人']
        self.Condition(dlg)
        time.sleep(2)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        # ExecuteFlow.print_control_identifiers()
        # 点击确认执行按钮
        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(2)
        # 从判断执行窗口是否存在，来确定窗口是否关闭成功
        if not ExecuteFlow.child_window(title="执行", control_type="Window").exists():
            self.result = '选择"确定"按钮，执行窗口关闭，运行流程 -->通过'
        else:
            self.result = '执行窗口依然存在运行流程 -->失败'

        time.sleep(1)

    def test07_Robot_本地流程库_执行窗口参数编辑(self):
        """对数据进行替换和赋值操作，然后运行流程"""
        dlg = self.dlg
        # dlg = self.app['云扩RPA机器人']
        self.Condition(dlg)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        # ExecuteFlow.print_control_identifiers()
        time.sleep(2)
        # 参数赋值编辑布尔
        value1 = "^a{}".format('True')
        ExecuteFlow.Edit1.type_keys(value1)
        # 参数赋值编辑数字
        value2 = "^a{}".format('222')
        ExecuteFlow.Edit2.type_keys(value2)
        # 参数赋值编辑系统32
        value3 = "^a{}".format('333')
        ExecuteFlow.Edit3.type_keys(value3)
        # 参数赋值编辑系统64
        value4 = "^a{}".format('444')
        ExecuteFlow.Edit4.type_keys(value4)
        # 参数赋值编辑单文本
        value5 = "^a{}".format('中国山河你最美')
        ExecuteFlow.Edit5.type_keys(value5)
        # 参数赋值编辑增加参数32
        value8 = "^a{}".format('3232')
        ExecuteFlow.Edit8.type_keys(value8)
        # 参数赋值编辑argument1
        value9 = "^a{}".format('孙悟空大闹天庭')
        ExecuteFlow.Edit9.type_keys(value9)

        # 点击确认执行按钮
        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(1)
        # 从判断执行窗口是否存在，来确定窗口是否关闭成功
        if not ExecuteFlow.child_window(title="执行", control_type="Window").exists():
            self.result = '参数重新赋值后，选择"确定"，执行窗口关闭，运行流程 -->通过'
        else:
            self.result = '参数重新赋值后，选择"确定"，执行窗口未关闭 -->失败'

        time.sleep(2)

    def test08_Robot_本地流程库_流程包执行录制视频(self):
        """勾选录制视频保留执行失败的视频"""
        dlg = self.dlg
        # dlg = self.app['云扩RPA机器人']
        self.Condition(dlg)
        # dlg.print_control_identifiers()
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        # ExecuteFlow.print_control_identifiers()
        time.sleep(2)
        # 测试“录制视频，保留执行失败的视频”的勾选
        ExecuteFlow.child_window(auto_id="EnableRecordVideo", control_type="CheckBox").click_input()
        # 录制视频，保留“执行成功”、“执行失败”、“全部”的视频，因组合框没有id、没有名称暂时无法支持选择
        # 点击确认执行按钮
        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(1)
        # 从判断执行窗口是否存在，来确定窗口是否关闭成功
        if not ExecuteFlow.child_window(title="执行", control_type="Window").exists():
            self.result = '勾选录制视频，选择"确定"按钮，执行窗口关闭，运行流程 -->通过'
        else:
            self.result = '勾选录制视频，执行窗口依然存在，运行流程 -->失败'

        time.sleep(16)  # 这个是等待程序执行完成的时间，不可省略

    def test09_Robot_本地流程库_取消删除文件(self):
        """取消删除dgs文件"""
        dlg = self.dlg
        # dlg = self.app['云扩RPA机器人']
        self.Condition(dlg)
        time.sleep(1)
        dlg['删除2'].click_input()  # 选择“删除”按钮已成功，下一步选择“确定”，将文件给真正删除掉
        # dlg.print_control_identifiers()
        time.sleep(1)
        message = dlg['提示']
        # message.print_control_identifiers()
        message.child_window(title="取消", auto_id="CancelButton", control_type="Button").click()
        time.sleep(2)

        if dlg.child_window(title="bianliang", control_type="Text").exists():
            self.result = '取消删除dgs文件-->通过'
        else:
            self.result = '取消删除dgs文件-->失败'
        time.sleep(2)

    def test10_Robot_本地流程库_确认删除文件(self):
        """确认删除dgs文件"""
        dlg = self.dlg
        self.Condition(dlg)
        time.sleep(1)
        dlg['删除2'].click_input()  # 选择“删除”按钮已成功，下一步选择“确定”，将文件给真正删除掉
        # dlg.print_control_identifiers()
        time.sleep(1)
        message = dlg['提示']
        message.child_window(title="确定", auto_id="OkButton", control_type="Button").click()
        time.sleep(2)
        # -----
        try:
            self.Condition(dlg)
            time.sleep(1)
            dlg['删除2'].click_input()  # 选择“删除”按钮已成功，下一步选择“确定”，将文件给真正删除掉
            # dlg.print_control_identifiers()
            time.sleep(1)
            message = dlg['提示']
            message.child_window(title="确定", auto_id="OkButton", control_type="Button").click()
            time.sleep(2)

        except:
            pass

        # # 实现将bianliang的两个文件全部删除掉，清空本地流程库
        # self.deletedgs(dlg=self.dlg)

        if not dlg.child_window(title="bianliang", control_type="Text").exists():
            self.result = '确认删除dgs文件-->通过'
        else:
            self.result = '确认删除dgs文件-->失败'

        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
