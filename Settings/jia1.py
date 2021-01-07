def numincreate():
    # 流程部署避免重复名称，后缀加数字+1自增操作
    f = open(r'D:\RobotPywinauto\Settings\shuzi.txt', 'r+')
    data = f.read()
    new_data = int(data)
    new_data += 1
    f.seek(0)
    f.truncate()
    f.write(str(new_data))
    f.close()
    return new_data

