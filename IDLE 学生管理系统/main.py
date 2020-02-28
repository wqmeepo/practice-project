import re
from menu import *
from do import *

def main():
    ctrl = True
    while ctrl:
        menu().menu()
        option = input("请选择：")
        option_str = re.sub('\D', '', option)
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:  # 退出系统
                print('您将退出学生信息管理系统')
                ctrl = False
            elif option_int == 1:  # 录入成绩
                insert()
            elif option_int == 2:  # 查找成绩
                search()
            elif option_int == 3:  # 删除成绩
                delete()
            elif option_int == 4:  # 修改成绩
                modify()
            elif option_int == 5:  # 排序
                sort()
            elif option_int == 6:  # 统计学生总数
                total()
            elif option_int == 7:  # 显示所有学生信息
                show()


if __name__ == '__main__':
    main()
