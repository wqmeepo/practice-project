finish = False  # 游戏是否结束
flagNum = 1  # 当前下棋者标记
flagCh = '*'  # 当前下棋者棋子
x = 0  # 当前棋子横坐标
y = 0  # 当前棋子纵坐标
print('\033[1;37;41m------ 简易五子棋(控制台版) -----\033[0m')

# 棋盘初始化
checkerboard = []
for i in range(10):
    checkerboard.append([])
    for j in range(10):
        checkerboard[i].append('-')


def show():
    print('\033[1;30;46m--------------------------------')
    print('   1  2  3  4  5  6  7  8  9  10')  # 输出行标号
    for i in range(len(checkerboard)):
        print(chr(i + ord('A')) + ' ', end=' ')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + ' ', end=' ')
        print()
    print('--------------------------------\033[0m')


def msg():
    # 输出棋局结束后的棋盘
    show()
    #  输出胜者
    if flagNum == 1:
        print('\033[32m *棋胜利！！\033[0m')
    else:
        print('\033[32m o棋胜利！！\033[0m')


while not finish:
    show()
    if flagNum == 1:
        flagCh = '*'
        print('\033[1;37;44m 请*输入棋子坐标：\033[0m', end=' ')  # 粉字黑底
    else:
        flagCh = 'o'
        print('\033[1;30;42m 请o输入棋子坐标：\033[0m', end=' ')  # 黑底绿字
    point = input()  # 输入棋子坐标
    ch = point[0]
    x = ord(ch) - 65
    y = int(point[1]) - 1

    if x < 0 or x > 9 or y < 0 or y > 9:
        print('\033[31m 棋子范围超出边界  \033[0m')
        continue

    if checkerboard[x][y] == '-':
        if flagNum == 1:
            checkerboard[x][y] = '*'
        else:
            checkerboard[x][y] = 'o'
    else:
        print('\033[31m 您输入的位置已经有其他棋子，请重新输入 \033[0m')
        continue

    show()

    if y - 4 >= 0:
        if checkerboard[x][y - 1] == flagCh and checkerboard[x][y - 2] == flagCh and checkerboard[x][y - 3] == flagCh \
                and checkerboard[x][y - 4] == flagCh:
            finish = True
            msg()
    elif y + 4 <= 9:
        if checkerboard[x][y + 1] == flagCh and checkerboard[x][y + 2] == flagCh and checkerboard[x][y + 3] == flagCh \
                and checkerboard[x][y + 4] == flagCh:
            finish = True
            msg()
    elif x - 4 >= 0:
        if checkerboard[x - 1][y] == flagCh and checkerboard[x - 2][y] == flagCh and checkerboard[x - 3][y] == flagCh \
                and checkerboard[x - 4][y] == flagCh:
            finish = True
            msg()
    elif x + 4 <= 9:
        if checkerboard[x + 1][y] == flagCh and checkerboard[x + 2][y] == flagCh and checkerboard[x + 3][y] == flagCh \
                and checkerboard[x + 4][y] == flagCh:
            finish = True
            msg()

    flagNum *= -1