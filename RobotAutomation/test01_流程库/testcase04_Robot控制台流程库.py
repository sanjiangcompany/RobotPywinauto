# 控制台流程库

import unittest
import pywinauto
from pywinauto import Application
from pywinauto.keyboard import send_keys
import time
from Settings import Version
from Settings import CommonExcute

version = Version.RobotVersion()


class RobotBVT(unittest.TestCase):
    """机器人控制台流程库"""

    def setUp(self):

        Application(backend="uia").start(
            r"C:\Program Files (x86)\Encoo Robot\app-1.1.{}\Robot.exe".format(version))

        self.app = pywinauto.Application(backend="uia").connect(
            path=r"C:\Program Files (x86)\Encoo Robot\app-1.1.{}\Robot.exe".format(version))

        self.dlg = self.app['云扩RPA机器人']

    def tearDown(self):
        self.dlg.close()

    def Condition(self, dlg):
        """控制台流程库运行的前置条件"""
        dlg.maximize()  # 窗口最大化操作
        dlg.child_window(auto_id="Package").double_click_input()
        time.sleep(2)
        dlg.child_window(title="Encoo.Robot.Monitor.Views.PageModel", auto_id="PackageConsole").double_click_input()
        time.sleep(2)
        dlg.child_window(title="变量参数含日志", control_type="Text").double_click_input()
        time.sleep(2)

    def test24_控制台流程库_确定执行流程(self):
        dlg = self.dlg
        self.Condition(dlg)
        time.sleep(1)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        # ExecuteFlow.print_control_identifiers()
        # 点击确认执行按钮
        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(2)
        # 从判断执行窗口是否存在，来确定窗口是否关闭成功
        if ExecuteFlow.child_window(title="执行", control_type="Window").exists() == False:
            self.result = '选择"确定"按钮，执行窗口关闭，运行流程 -->通过'
        else:
            self.result = '执行窗口依然存在运行流程 -->失败'

        time.sleep(1)

    def test25_控制台流程库_取消执行流程(self):
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
        if ExecuteFlow.child_window(title="执行", control_type="Window").exists() == False:
            self.result = '选择"取消"按钮，执行窗口关闭成功-->通过'
        else:
            self.result = '执行窗口依然存在未关闭成功-->失败'

        time.sleep(1)

    def test26_Robot_控制台流程库_执行窗口参数编辑(self):
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
        value1 = "^a{}".format('False')
        ExecuteFlow.Edit1.type_keys(value1)
        # 参数赋值编辑数字
        value2 = "^a{}".format('2020')
        ExecuteFlow.Edit2.type_keys(value2)
        # 参数赋值编辑系统32
        value3 = "^a{}".format('2021')
        ExecuteFlow.Edit3.type_keys(value3)
        # 参数赋值编辑系统64
        value4 = "^a{}".format('2022')
        ExecuteFlow.Edit4.type_keys(value4)
        # 参数赋值编辑单文本
        value5 = "^a{}".format('绿水青山')
        ExecuteFlow.Edit5.type_keys(value5)
        # 参数赋值编辑增加参数32
        value8 = "^a{}".format('320320')
        ExecuteFlow.Edit8.type_keys(value8)
        # 参数赋值编辑argument1
        value9 = "^a{}".format('金山银山')
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

    def test27_Robot_控制台流程库_流程包执行录制视频(self):
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
        if ExecuteFlow.child_window(title="执行", control_type="Window").exists() == False:
            self.result = '勾选录制视频，选择"确定"按钮，执行窗口关闭，运行流程 -->通过'
        else:
            self.result = '勾选录制视频，执行窗口依然存在，运行流程 -->失败'

        time.sleep(16)  # 这个是等待程序执行完成的时间，不可省略

    def test28_Robot_控制台流程库_管理员权限执行流程(self):
        """勾选管理员权限，确定执行流程"""
        dlg = self.dlg
        self.Condition(dlg)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        ExecuteFlow.child_window(auto_id="RunAsAdmin", control_type="CheckBox").click_input()  # 这一行不管用，暂时先放这

        # 点击确认执行按钮
        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(2)
        # 从判断执行窗口是否存在，来确定窗口是否关闭成功
        if ExecuteFlow.child_window(title="执行", control_type="Window").exists() == False:
            print('选择"确定"按钮，执行窗口关闭，运行流程 -->通过')
        else:
            print('执行窗口依然存在运行流程 -->失败')

        time.sleep(1)

    def test29_Robot_控制台流程库_执行窗口关闭功能(self):
        """执行窗口通过点击右上角的X 实现窗口的关闭"""
        dlg = self.dlg
        self.Condition(dlg)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        # ExecuteFlow.print_control_identifiers()
        time.sleep(1)
        # 关闭执行窗口
        ExecuteFlow.child_window(auto_id="CloseButtonImage", control_type="Image").click_input()
        time.sleep(1)
        if not ExecuteFlow.child_window(title="执行", control_type="Window").exists():
            print('选择"X"按钮，关闭执行窗口 -->通过')
        else:
            print('选择"X"按钮,执行窗口未能正常关闭 -->失败')
        time.sleep(1)

    def test30_Robot_控制台流程库_未勾选以管理员权限运行流程(self):
        """未勾选管理员权限流程执行失败"""
        dlg = self.dlg
        self.Condition(dlg)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        # 不勾选以管理员权限运行流程，直接点击确认执行按钮
        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(3)
        self.Condition(dlg)
        time.sleep(3)
        if dlg.child_window(title="成功", control_type="Text").exists():
            print('流程执行成功 -->通过')
        else:
            print('流程执行失败 -->失败')

        time.sleep(1)

    def test31_Robot_控制台流程库_管理员权限运行校验结果(self):
        """勾选以管理员权限执行流程"""
        dlg = self.dlg
        self.Condition(dlg)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        ExecuteFlow.child_window(auto_id="RunAsAdmin", control_type="CheckBox").click_input()

        # 勾选以管理员权限运行流程，直接点击确认执行按钮
        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(2)
        self.Condition(dlg)  # 加这个重复的步骤是为了避免不必要的情况发生
        time.sleep(2)
        if dlg.child_window(title="成功", control_type="Text").exists() == True:
            print('以管理员权限运行流程，流程执行成功 -->通过')
        else:
            print('以管理员权限运行流程，流程执行失败 -->失败')

        time.sleep(1)

    def test32_Robot_控制台流程库_超时时间(self):
        """用管理员权限运行,勾选超时时间，确定执行流程"""
        dlg = self.dlg
        self.Condition(dlg)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        # ExecuteFlow.print_control_identifiers()
        # 执行超时时间
        ExecuteFlow.child_window(auto_id="RunAsAdmin", control_type="CheckBox").click_input()
        time.sleep(1)
        ExecuteFlow.child_window(auto_id="HasTimeout", control_type="CheckBox").click_input()
        # 点击确认执行按钮
        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(2)
        # 从判断执行窗口是否存在，来确定窗口是否关闭成功
        if not ExecuteFlow.child_window(title="执行", control_type="Window").exists():
            print('选择"确定"按钮，执行窗口关闭，运行流程 -->通过')
        else:
            print('执行窗口依然存在运行流程 -->失败')

        time.sleep(2)
        self.Condition(dlg)  # 加这个重复的步骤是为了避免不必要的情况发生
        time.sleep(1)
        if dlg.child_window(title="成功", control_type="Text").exists():
            print('以管理员权限运行流程，在指定时间内，流程执行成功 -->通过')
        else:
            print('以管理员权限运行流程，在指定时间内，流程执行失败 -->失败')

        time.sleep(1)


if __name__ == '__main__':
    unittest.main()




