# # 杀掉Robot的进程，解决P0相关Pywinauto的连接问题
# 
# import unittest, time
# from Settings import Version
# 
# version = Version.RobotVersion()
# 
# 
# class RobotBVT(unittest.TestCase):
#     """机器人本地流程库"""
# 
#     def setUp(self):
#         pass
# 
#     def tearDown(self):
#         pass
# 
#     def test01_KillRobot(self):
#         import os
#         os.system('TASKKILL /F /IM Robot.exe')
#         time.sleep(6)
# 
# 
# if __name__ == '__main__':
#     unittest.main()
