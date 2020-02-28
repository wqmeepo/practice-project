def save(student):
    with open('./student.txt', 'a+') as f:
        for info in student:
            f.write(str(info) + '\n')


def insert():
    studentList = []
    mark = True
    while mark:
        init = input('即将开始录入学生信息，输入0回到主界面')
        if init == '0':
            break
        id = input('请输入6位ID（例如000001）：')
        name = input('请输入姓名（例如0张三）：')
        english = input('请输入英文成绩（请输入数字）:')
        python = input('请输入python成绩（请输入数字）:')
        c = input('请输入c语言成绩（请输入数字）:')
        if not id or not name or not english or not python or not c:
            print("请不要输出空值，请重新输入")
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'c': c}
        studentList.append(student)
        inputMark = input('是否继续输入{y/n}：')
        if inputMark == 'y' or inputMark == 'Y':
            mark = True
        if inputMark == 'n' or inputMark == 'N':
            mark = False

    save(studentList)
    print('学生信息保存完毕！！')


def delete():
    mark = True
    studentList = []
    studentDic = []
    show()
    while mark:
        studentId = input('上列位所有学生信息，请输入要删除的学生id（输入0退出程序）：')
        if studentId == '0':
            break
        elif not studentId:
            print('不允许输入空值，请重新输入')
            continue
        else:
            with open('./student.txt', 'r') as f:
                for info in f.readlines():
                    info_dic = eval(info)
                    studentDic.append(info_dic['id'])
            if studentId not in studentDic:
                print('学生ID不在信息库内，请重新选择')
                continue
            else:
                print('学生ID在信息库内，正在删除,下列为删除后的信息')
                with open('./student.txt', 'r') as f:
                    for info in f.readlines():
                        info_dic = eval(info)
                        studentList.append(info_dic)
                with open('./student.txt', 'w') as f:
                    for info in studentList:
                        if info['id'] != studentId:
                            f.write(str(info) + '\n')
        show()
        inputMark = input('删除成功，是否继续删除{y/n}：')
        if inputMark == 'y' or inputMark == 'Y':
            mark = True
        if inputMark == 'n' or inputMark == 'N':
            mark = False


def show():
    with open('./student.txt', 'r') as f:
        for info in f.readlines():
            print(info)


def modify():
    show()
    studentId = input('上列为所有学生信息，请输入要修改的学生id（输入0退出程序）：')
    studentDic = []
    studentList = []
    mark = True
    while mark:
        if studentId == '0':
            break
        elif not studentId:
            print('不允许输入空值，请重新输入')
            continue
        else:
            with open('./student.txt', 'r') as f:
                for info in f.readlines():
                    info_dic = eval(info)
                    studentDic.append(info_dic['id'])
            if studentId not in studentDic:
                print('学生ID不在信息库内，请重新选择')
                continue
            else:
                print('学生ID在信息库内，请输入修改后的内容')
                name = input('姓名 name = ')
                english = input('英语成绩 = ')
                python = input('python成绩 = ')
                c = input('c语言成绩 = ')
                with open('./student.txt', 'r') as f:
                    for info in f.readlines():
                        info_dic = eval(info)
                        studentList.append(info_dic)
                with open('./student.txt', 'w') as f:
                    for info in studentList:
                        if info['id'] != studentId:
                            f.write(str(info) + '\n')
                        elif info['id'] == studentId:
                            info['name'] = name
                            info['english'] = english
                            info['python'] = python
                            info['c'] = c
                            f.write(str(info) + '\n')
        show()
        inputMark = input('删除成功，是否继续删除{y/n}：')
        if inputMark == 'y' or inputMark == 'Y':
            mark = True
        if inputMark == 'n' or inputMark == 'N':
            mark = False


def search():
    TODO


def sort():
    TODO


def total():
    TODO
