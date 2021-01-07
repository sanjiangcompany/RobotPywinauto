# 本地流程库执行窗口中的管理员权限执行流程、执行窗口截图、超时时间功能
import unittest
import time
import pywinauto
from pywinauto import Application
from pywinauto.keyboard import send_keys
from Settings import Version
from Settings import Log
version = Version.RobotVersion()


class RobotBVT(unittest.TestCase):
    """机器人本地流程库，执行流程相关功能"""

    def setUp(self):

        Application(backend="uia").start(
            r"C:\Program Files (x86)\Encoo Robot\app-1.1.{}\Robot.exe".format(version))

        # 一定不要忘了运行Robot自动化一定要先结束一下进程
        self.app = pywinauto.Application(backend="uia").connect(
            path=r"C:\Program Files (x86)\Encoo Robot\app-1.1.{}\Robot.exe".format(version))

        self.dlg = self.app['云扩RPA机器人']

    def tearDown(self):
        self.dlg.close()

    def Condition2(self, dlg):
        dlg.maximize()  # 窗口最大化操作
        dlg.child_window(auto_id="Package").double_click_input()
        time.sleep(2)
        dlg.child_window(title="Encoo.Robot.Monitor.Views.PageModel", auto_id="PackageLocal").double_click_input()
        time.sleep(2)
        dlg.child_window(title="管理员权限可以访问的文件", control_type="Text").double_click_input()
        time.sleep(2)

    def test11_Robot_点击导入(self):
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
                send_keys(r'D:\变量参数')
                send_keys("{VK_RETURN}")
                # 打开桌面后，选中文件名输入框，传值文件的名字，然后回车键上传成功
                time.sleep(2)
                desktop["文件名(&N):Edit"].type_keys("管理员权限可以访问的文件.dgs")
                send_keys("{VK_RETURN}")

                # 问题2，我该怎么做文本校验，判断他导入成功呢？使用.texts()方法
                if (dlg.child_window(title="管理员权限可以访问的文件", control_type="Text").texts() == ['管理员权限可以访问的文件']):
                    print('上传只有管理员权限执行才能成功的dgs文件-->通过')
                else:
                    print('上传只有管理员权限执行才能成功的dgs文件-->失败')
            else:
                print('流程库入口不存在，无法进行下一步的操作')
            time.sleep(1)
        except:
            pass

    def test12_Robot_本地流程库_管理员权限文件上传(self):
        '''上传只有管理员权限执行才能成功的文件到本地流程库中'''
        dlg = self.dlg
        dlg.maximize()  # 窗口最大化操作
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
            desktop["文件名(&N):Edit"].type_keys("管理员权限可以访问的文件.dgs")
            send_keys("{VK_RETURN}")

            # 问题2，我该怎么做文本校验，判断他导入成功呢？使用.texts()方法
            if (dlg.child_window(title="管理员权限可以访问的文件", control_type="Text").texts() == ['管理员权限可以访问的文件']):
                print('上传只有管理员权限执行才能成功的dgs文件-->通过')
            else:
                print('上传只有管理员权限执行才能成功的dgs文件-->失败')
        else:
            print('流程库入口不存在，无法进行下一步的操作')
        time.sleep(1)

    def test13_Robot_本地流程库_管理员权限执行流程(self):
        """勾选管理员权限，确定执行流程"""
        dlg = self.dlg
        self.Condition2(dlg)
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

    def test14_Robot_本地流程库_执行窗口关闭功能(self):
        """执行窗口通过点击右上角的X 实现窗口的关闭"""
        dlg = self.dlg
        self.Condition2(dlg)
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

    def test15_Robot_本地流程库_未勾选以管理员权限运行流程(self):
        """未勾选管理员权限流程执行失败"""
        dlg = self.dlg
        self.Condition2(dlg)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        # 不勾选以管理员权限运行流程，直接点击确认执行按钮
        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(3)
        self.Condition2(dlg)
        time.sleep(3)
        if dlg.child_window(title="失败", control_type="Text").exists():
            print('未勾选以管理员权限运行流程，流程执行失败 -->通过')
        else:
            print('未勾选以管理员权限运行流程， -->失败')

        time.sleep(1)

    def test16_Robot_本地流程库_管理员权限运行校验结果(self):
        """勾选以管理员权限执行流程"""
        dlg = self.dlg
        self.Condition2(dlg)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        ExecuteFlow.child_window(auto_id="RunAsAdmin", control_type="CheckBox").click_input()

        # 勾选以管理员权限运行流程，直接点击确认执行按钮
        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(2)
        self.Condition2(dlg)  # 加这个重复的步骤是为了避免不必要的情况发生
        time.sleep(2)
        if dlg.child_window(title="成功", control_type="Text").exists() == True:
            print('以管理员权限运行流程，流程执行成功 -->通过')
        else:
            print('以管理员权限运行流程，流程执行失败 -->失败')

        time.sleep(1)

    def test17_Robot_本地流程库_执行过程截图(self):
        """勾选执行过程截图，确定执行流程"""
        dlg = self.dlg
        self.Condition2(dlg)
        dlg['执行'].click_input()
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        # ExecuteFlow.print_control_identifiers()
        # 执行过程截图
        ExecuteFlow.child_window(auto_id="EnableScreenshot", control_type="CheckBox").click_input()
        # 点击确认执行按钮
        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(2)
        # 从判断执行窗口是否存在，来确定窗口是否关闭成功
        if ExecuteFlow.child_window(title="执行", control_type="Window").exists() == False:
            print('选择"确定"按钮，执行窗口关闭，运行流程 -->通过')
        else:
            print('执行窗口依然存在运行流程 -->失败')

        time.sleep(2)

    def test18_Robot_本地流程库_判断执行过程截图运行结果(self):
        """非管理员权限,选择执行截图查看流程运行结果"""
        dlg = self.dlg
        self.Condition2(dlg)
        dlg['执行'].click_input()  # 选择“执行”按钮已成功，
        # dlg.print_control_identifiers()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        ExecuteFlow.child_window(auto_id="EnableScreenshot", control_type="CheckBox").click_input()

        ExecuteFlow.child_window(title="确认", auto_id="BtnOk", control_type="Button").click()
        time.sleep(1)
        self.Condition2(dlg)  # 加这个重复的步骤是为了避免不必要的情况发生
        time.sleep(3)
        if dlg.child_window(title="失败", control_type="Text").exists() == True:
            print('非管理员权限，勾选执行过程截图,最终执行状态为失败,与实际结果相同 -->通过')
        else:
            print('非管理员权限，勾选执行过程截图,最终执行状态为成功,与实际结果相反 -->失败')
        time.sleep(2)

    def test19_Robot_本地流程库_判断执行过程截图运行结果(self):
        """打开日志的操作,界面展示操作结果"""
        dlg = self.dlg
        self.Condition2(dlg)
        # dlg['日志'].click_input()  # 做一个打开日志的操作
        Log.LogFile()
        time.sleep(2)

    def test20_Robot_本地流程库_获取截图数量(self):
        """判断Screenshots文件是否存在，有文件就获取截图数量"""
        dlg = self.dlg
        self.Condition2(dlg)
        # dlg['日志'].click_input()  # 做一个打开日志的操作
        Log.LogFile()
        time.sleep(2)

    def test21_Robot_本地流程库_判断是否有log日志(self):
        """获取文件内容，判断是否产生log日志文件"""
        dlg = self.dlg
        self.Condition2(dlg)
        dlg['日志'].click_input()  # 做一个打开日志的操作
        Log.LogFile()
        time.sleep(2)

    def test22_Robot_本地流程库_超时时间(self):
        """用管理员权限运行,勾选超时时间，确定执行流程"""
        dlg = self.dlg
        self.Condition2(dlg)
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
        if ExecuteFlow.child_window(title="执行", control_type="Window").exists() == False:
            print('选择"确定"按钮，执行窗口关闭，运行流程 -->通过')
        else:
            print('执行窗口依然存在运行流程 -->失败')

        time.sleep(2)
        self.Condition2(dlg)  # 加这个重复的步骤是为了避免不必要的情况发生
        time.sleep(1)
        if dlg.child_window(title="成功", control_type="Text").exists() == True:
            print('以管理员权限运行流程，在指定时间内，流程执行成功 -->通过')
        else:
            print('以管理员权限运行流程，在指定时间内，流程执行失败 -->失败')

        time.sleep(1)

    def test23_Robot_本地流程库_删除管理员权限运行的流程(self):
        """确认删除管理员运行文件"""
        dlg = self.dlg
        self.Condition2(dlg)
        time.sleep(1)
        dlg['删除2'].click_input()  # 选择“删除”按钮已成功，下一步选择“确定”，将文件给真正删除掉
        # dlg.print_control_identifiers()
        time.sleep(1)
        message = dlg['提示']
        message.child_window(title="确定", auto_id="OkButton", control_type="Button").click()
        time.sleep(2)
        # -----
        try:
            self.Condition2(dlg)
            time.sleep(1)
            dlg['删除2'].click_input()  # 选择“删除”按钮已成功，下一步选择“确定”，将文件给真正删除掉
            # dlg.print_control_identifiers()
            time.sleep(1)
            message = dlg['提示']
            message.child_window(title="确定", auto_id="OkButton", control_type="Button").click()
            time.sleep(2)

        except:
            pass

        if dlg.child_window(title="管理员权限可以访问的文件", control_type="Text").exists() == False:
            print('确认删除dgs文件-->通过')
        else:
            print('确认删除dgs文件-->失败')

        time.sleep(1)


if __name__ == '__main__':
    unittest.main()





