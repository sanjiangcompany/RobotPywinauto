import time
import pywinauto
from pywinauto import Application
from Settings import Version

version = Version.RobotVersion()


class Excute:
    def Condition2(self, dlg):
        dlg.maximize()  # 窗口最大化操作
        dlg.child_window(auto_id="Package").double_click_input()
        time.sleep(2)
        dlg.child_window(title="Encoo.Robot.Monitor.Views.PageModel", auto_id="PackageLocal").double_click_input()
        time.sleep(2)
        dlg.child_window(title="管理员权限可以访问的文件", control_type="Text").double_click_input()
        time.sleep(2)

    def excuteway(self, way):
        Application(backend="uia").start(
            r"C:\Program Files (x86)\Encoo Robot\app-1.1.{}\Robot.exe".format(version))

        self.app = pywinauto.Application(backend="uia").connect(
            path=r"C:\Program Files (x86)\Encoo Robot\app-1.1.{}\Robot.exe".format(version))

        self.dlg = self.app['云扩RPA机器人']
        dlg = self.dlg
        self.Condition2(dlg)
        time.sleep(1)
        dlg['执行'].click_input()
        time.sleep(1)
        ExecuteFlow = dlg['执行']
        # ExecuteFlow.print_control_identifiers()
        # 点击取消执行按钮
        ExecuteFlow.child_window(title=f"{way}", auto_id="BtnOk", control_type="Button").click()
        time.sleep(2)
        # 从判断执行窗口是否存在，来确定窗口是否关闭成功
        if not ExecuteFlow.child_window(title="执行", control_type="Window").exists():
            self.result = '选择"确定"按钮，执行窗口关闭，运行流程 -->通过'
        else:
            self.result = '执行窗口依然存在运行流程 -->失败'

        time.sleep(1)
