class menu(object):
    def __init__(self):
        self.name = 'menu'

    def menu(self):
        # 输出菜单
        print(''' 
            ================= 功能菜单 ==================
            
            1、 录入学生信息
            2、 查找学生信息
            3、 删除学生信息
            4、 修改学生信息
            5、 排序
            6、 统计学生总数
            7、 显示所有学生信息
            8、 退出系统
            
            =============================================
        ''')


if __name__ == '__main__':
    menu().menu()
