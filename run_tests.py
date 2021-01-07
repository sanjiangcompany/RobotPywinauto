import sys

sys.path.append('./RobotAutomation')
from util.HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from util import Email_Project

# 指定Robot桌面应用程序测试用例为当前文件夹下的 RobotAutomation 目录
test_dir = './RobotAutomation'
testsuit = defaultTestLoader.discover(test_dir, pattern='testcase*.py')

if __name__ == "__main__":
    # 执行发送邮件功能
    Email_Project.Email()

    # 执行脚本文件入口
    filename = './report/' + 'result.html'
    fp = open(filename, 'wb')
    # Robot产品简介
    Build_Version = '1.1.2012.11'
    ReportContent = 'Build:{}'.format(Build_Version)

    runner = HTMLTestRunner(stream=fp,
                            title='Robot界面自动化测试报告',
                            description=f'{ReportContent}'
                            )
    runner.run(testsuit, rerun=0, save_last_run=False)
    fp.close()

