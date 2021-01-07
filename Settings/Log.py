import os

filepath = r'C:\Users\bqm66\AppData\Local\Encoo\Encoo Robot\JobLogs\local\管理员权限可以访问的文件\1.0.0'

filelist = []


class LogFile:
    try:
        if os.path.exists(filepath):
            pathDir = os.listdir(filepath)
            for allDir in pathDir:
                child = os.path.join('%s%s' % (filepath, allDir))
                # print('打印文件', child)
                filelist.append(child)
                # print('所有文件', filelist)
            '''
            1.拿到最后一个（即最新的执行时间的文件）
            2.需要做字符串取值，拿到后14个字符
            3.做字符串拼接，获取到真正正确的路径，可输入文件位置直接打开的文件有效路径
            4.校验log文件是否存在
            5.校验截图文件是否存在，获取文件中的截图数量，打印输出结果
            '''
            endfile_name = filelist[-1]
            # print(type(endfile_name), endfile_name)
            # print('拿到后14个字符', endfile_name[-14:])
            new_file = endfile_name[-14:]
            rod = f'\{new_file}'
            # 我是最后转换的正确路径
            correct_path = filepath + rod
            # print('我是最后转换的正确路径', correct_path)
            # 进行文件夹内容循环获取
            pathDir = os.listdir(correct_path)
            for allDir in pathDir:
                child = os.path.join('%s%s' % (filepath, allDir))
                # print('打印正确的文件', type(child), child)
                correctlogname = 'job-' + new_file + '.log'
                jietu = 'Screenshots'
                if correctlogname and jietu in child:
                    print('日志文件已存在,Screenshots文件已存在')
            # 截图路径
            jietu_road = '\Screenshots'
            correct_jietu_road = correct_path + jietu_road
            # print('我是最后转换的正确路径', correct_jietu_road)
            pathDir = os.listdir(correct_jietu_road)
            child_list = []
            for allDir in pathDir:
                child = os.path.join('%s%s' % (filepath, allDir))
                # print('打印正确的文件', type(child), child)
                child_list.append(child)
                jietu_num = len(child_list)
                # print('我最后的值是', len(child_list), child_list)
                if 'jpg' in child:
                    print(f'执行截图功能通过,总共有{jietu_num}张截图')
        else:
            print('文件路径不存在请通过Robot界面选择日志查看正确的文件路径地址')

    except:

        pass




