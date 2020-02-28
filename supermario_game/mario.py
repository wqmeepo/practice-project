import pygame, random
from pygame.locals import *  # 导入pygame中的常量
import sys
from itertools import cycle  # 导入迭代工具

screenWidth = 800
screenHeight = 199
FPS = 60


class MyMap(object):
    def __init__(self, x, y):
        self.bg = pygame.image.load('images/bg.png').convert_alpha()  # 加载背景图片
        self.x = x
        self.y = y

    def map_rolling(self):
        if self.x < -800:  # 小于-790说明地图移动出屏幕
            self.x = 800  # 给地图一个新的坐标
        else:
            self.x -= 5  # 向左移动5像素

    def map_update(self):
        screen.blit(self.bg, (self.x, self.y))  # 更新地图


class Mario(object):
    def __init__(self):  # 初始化马里奥
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.jumpState = False  # 跳跃状态
        self.jumpHeight = 130  # 跳跃高度
        self.lowest_y = 140  # 最低坐标
        self.jumpValue = 0  # 跳跃增变量
        # 马里奥动图索引
        self.marioIndex = 0
        self.marioIndexGen = cycle([0, 1, 2])
        # 加载马里奥图片
        self.adventure_img = (pygame.image.load('images/adventure1.png').convert_alpha(),
                              pygame.image.load('images/adventure2.png').convert_alpha(),
                              pygame.image.load('images/adventure3.png').convert_alpha(),)
        self.jump_audio = pygame.mixer.Sound('audio/jump.wav')  # 跳音效
        self.rect.size = self.adventure_img[0].get_size()
        self.x = 50  # mario x坐标
        self.y = self.lowest_y  # mario y坐标
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.jumpState = True

    def move(self):
        if self.jumpState:  # 当起跳的时候
            if self.rect.y >= self.lowest_y:
                self.jumpValue = -5
            if self.rect.y <= self.lowest_y - self.jumpHeight:
                self.jumpValue = 5
            self.rect.y += self.jumpValue
            if self.rect.y >= self.lowest_y:
                self.jumpState = False

    def draw_mario(self):
        marioIndex = next(self.marioIndexGen)
        screen.blit(self.adventure_img[marioIndex], (self.x, self.rect.y))


class Obstacle(object):
    score = 1  # 分数
    move = 5  # 移动距离
    obstacle_y = 150  # 障碍物的y坐标

    def __init__(self):  # 初始化障碍物矩形
        self.rect = pygame.Rect(0, 0, 0, 0)
        # 加载障碍物图片
        self.missile = pygame.image.load('images/missile.png').convert_alpha()
        self.pipe = pygame.image.load('images/pipe.png').convert_alpha()
        # 加载分数图片
        self.numbers = (pygame.image.load('images/0.png').convert_alpha(),
                        pygame.image.load('images/1.png').convert_alpha(),
                        pygame.image.load('images/2.png').convert_alpha(),
                        pygame.image.load('images/3.png').convert_alpha(),
                        pygame.image.load('images/4.png').convert_alpha(),
                        pygame.image.load('images/5.png').convert_alpha(),
                        pygame.image.load('images/6.png').convert_alpha(),
                        pygame.image.load('images/7.png').convert_alpha(),
                        pygame.image.load('images/8.png').convert_alpha(),
                        pygame.image.load('images/9.png').convert_alpha(),)
        # 加载加分音效
        self.score_audio = pygame.mixer.Sound('audio/score.wav')
        # 0和1随机数
        r = random.randint(0, 1)
        if r == 0:  # 如果随机数是0显示导入，相反显示管道
            self.image = self.missile
            self.move = 15  # 导弹移动速度加快
            self.obstacle_y = 100  # 导弹在天上，笛卡尔坐标系
        else:
            self.image = self.pipe  # 显示管道障碍物
        # 根据障碍物位图的宽高来设置矩形
        self.rect.size = self.image.get_size()
        # 获取位图宽高
        self.width, self.height = self.rect.size
        # 障碍物绘制坐标
        self.x = 800
        self.y = self.obstacle_y
        self.rect.center = (self.x, self.y)

    def obstacle_move(self):  # 障碍物移动
        self.rect.x -= self.move

    def draw_obstacle(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def get_score(self):        # 获取分数
        tmp = self.score
        if tmp == 1:
            self.score_audio.play()     # 播放加分音效
        self.score = 0
        return tmp

    def show_score(self, score):        # 显示分数
        self.scoreDigits = [int(x) for x in list(str(score))]
        totalWidth = 0      # 显示所有数字总宽度
        for digit in self.scoreDigits:
            # 获取积分图片宽度
            totalWidth += self.numbers[digit].get_width()
        # 分数横向位置
        Xoffset = (screenWidth - (totalWidth + 30))
        for digit in self.scoreDigits:
            screen.blit(self.numbers[digit], (Xoffset, screenHeight * 0.1))
            Xoffset += self.numbers[digit].get_width()


class MusicButton(object):
    is_open = True

    def __init__(self):
        self.open_img = pygame.image.load('images/btn_open.png').convert_alpha()
        self.close_img = pygame.image.load('images/btn_close.png').convert_alpha()
        self.bg_music = pygame.mixer.Sound('audio/bg_music.wav')

    # 判断鼠标是否在按钮的范围内
    def is_select(self):  # 获取鼠标的坐标
        pointx, pointy = pygame.mouse.get_pos()
        w, h = self.open_img.get_size()  # 获取图片按钮的大小
        # 判断鼠标位置
        in_x = pointx > 20 and pointx < 20 + w
        in_y = pointy > 20 and pointy < 20 + h
        return in_x and in_y


def game_over():
    bump_audio = pygame.mixer.Sound('audio/bump.wav')   # 撞击
    bump_audio.play()
    # 获取窗体宽/高
    screen_w = pygame.display.Info().current_w
    screen_h = pygame.display.Info().current_h
    # 加载游戏结束的图片
    over_img = pygame.image.load('images/gameover.png').convert_alpha()
    # 将游戏结束的图片绘制在窗体的中间位置
    screen.blit(over_img, (int(screen_w - over_img.get_width())/2, int(screen_h - over_img.get_height())/2 ))


def main_game():
    score = 0
    over = False
    global screen, FPSClock
    pygame.init()  # 初始化之后可以开始使用pygame
    FPSClock = pygame.time.Clock()  # 使用python时钟控制每个循环多长时间运行一次，在使用时钟前必须先创建clock对象的实例
    screen = pygame.display.set_mode((screenWidth, screenHeight))  # 创建窗体，与程序交互
    pygame.display.set_caption('Super Mario')  # 设置窗口标题
    bg1 = MyMap(0, 0)
    bg2 = MyMap(800, 0)
    mario = Mario()
    addobstacletime = 0  # 添加障碍物的时间
    obstaclelist = []  # 添加障碍物的对象列表
    music_button = MusicButton()
    btn_img = music_button.open_img
    music_button.bg_music.play(-1)
    while True:
        # 获取单击事件
        for event in pygame.event.get():  # 检测窗口关闭事件
            if event.type == QUIT:
                pygame.quit()  # 退出窗口
                sys.exit()  # 关闭窗口
            if event.type == KEYDOWN and event.key == K_SPACE:
                if mario.rect.y >= mario.lowest_y:
                    mario.jump_audio.play()
                    mario.jump()
            if event.type == pygame.MOUSEBUTTONUP:  # 判断鼠标事件
                if over is False:  # 判断游戏是否停止
                    if music_button.is_select():
                        if music_button.is_open:
                            btn_img = music_button.close_img
                            music_button.is_open = False
                            music_button.bg_music.stop()
                        else:
                            btn_img = music_button.open_img
                            music_button.is_open = True
                            music_button.bg_music.play(-1)
        if over is False:
            bg1.map_update()
            bg1.map_rolling()
            bg2.map_update()
            bg2.map_rolling()
            mario.move()
            mario.draw_mario()
        # 计算障碍物的间隔时间
        if addobstacletime >= 1300:
            r = random.randint(0, 100)
            if r > 40:
                # 创建障碍物对象
                obstacle = Obstacle()
                # 将障碍物添加进障碍物列表内
                obstaclelist.append(obstacle)
            # 重置添加障碍物时间
            addobstacletime = 0
        # 循环遍历障碍物
        for i in range(len(obstaclelist)):
            obstaclelist[i].obstacle_move()
            obstaclelist[i].draw_obstacle()
        # 判断是否碰撞
            if pygame.sprite.collide_rect(mario, obstaclelist[i]):
                over = True
                game_over()
                music_button.bg_music.stop()
            else:
                if obstaclelist[i].rect.x + obstaclelist[i].rect.width < mario.rect.x:
                    score += obstaclelist[i].get_score()
            obstaclelist[i].show_score(score)
        screen.blit(btn_img, (20, 20))
        addobstacletime += 20  # 增加障碍物时间
        pygame.display.update()  # 更新整个窗体
        FPSClock.tick(FPS)


if __name__ == '__main__':
    main_game()