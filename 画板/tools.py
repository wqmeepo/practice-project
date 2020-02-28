import pygame
import math

class Menu(object):
    def __init__(self, screen):
        self.screen = screen  # 初始化窗口
        self.brush = None  # 初始化画笔
        self.colors = [
            (0xff, 0x00, 0xff), (0x80, 0x00, 0x80),
            (0x00, 0x00, 0xff), (0x00, 0x00, 0x80),
            (0x00, 0xff, 0xff), (0x00, 0x80, 0x80),
            (0x00, 0xff, 0x00), (0x00, 0x80, 0x00),
            (0xff, 0xff, 0x00), (0x80, 0x80, 0x00),
            (0xff, 0x00, 0x00), (0x80, 0x00, 0x00),
            (0xc0, 0xc0, 0xc0), (0x00, 0x00, 0x00),
            (0x80, 0x80, 0x80), (0x00, 0xc0, 0x80),
        ]
        self.eraser_color = (0xff, 0xff, 0xff)  # 初始颜色
        # 计算每个色块在画板中的坐标值，便于绘制
        self.colors_rect = []
        for (i, rgb) in enumerate(self.colors):  # 方块颜色表，创建调色板rect
            rect = pygame.Rect(10 + i % 2 * 32, 254 + i / 2 * 32, 32, 32)
            self.colors_rect.append(rect)
        self.pens = [
            pygame.image.load('img/pen.png').convert_alpha(),
        ]
        self.erasers = [
            pygame.image.load('img/eraser.png').convert_alpha(),
        ]
        self.erasers_rect = []
        for (i, img) in enumerate(self.erasers):  # 橡皮列表,创建橡皮的rect
            rect = pygame.Rect(10, 10 + (i + 1) * 64, 64, 64)
            self.erasers_rect.append(rect)
        self.pens_rect = []
        for (i, img) in enumerate(self.pens):  # 画笔列表，创建画笔的rect
            rect = pygame.Rect(10, 10 + i * 64, 64, 64)
            self.pens_rect.append(rect)
        self.sizes = [
            pygame.image.load('img/plus.png').convert_alpha(),
            pygame.image.load('img/minus.png').conver_alpha()
        ]
        # 计算坐标,便于绘制
        self.sizes_rect = []
        for (i, img) in enumerate(self.sizes):
            rect = pygame.Rect(10 + i * 32, 138, 32, 32)
            self.sizes_rect.append(rect)

    def set_brush(self, brush):  # 设置画笔对象
        self.brush = brush

    def draw(self):  # 绘制菜单栏
        for (i, img) in enumerate(self.pens):  # 绘制画笔样式按钮
            self.screen.blit(img, self.pens_rect[i].topleft)
        for (i, img) in enumerate(self.erasers):  # 绘制橡皮
            self.screen.blit(img, self.erasers_rect[i].topleft)
        for (i, img) in enumerate(self.sizes):  # 绘制 + - 号
            self.screen.blit(img, self.sizes_rect[i].topleft)
        # 绘制用于实时展示画笔的小窗口
        self.screen.fill((255, 255, 255), (10, 180, 64, 64))
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 180, 64, 64), 1)
        size = self.brush.get_size()
        x = 10 + 32
        y = 180 + 32
        # 在窗口中展示画笔
        pygame.draw.circle(self.screen, self.brush.get_color(), (x, y), int(size))
        for (i, rgb) in enumerate(self.colors):  # 绘制色块
            pygame.draw.rect(self.screen, rgb, self.colors_rect[i])

    def click_button(self, pos):  # 用来为菜单栏各个图标按钮绑定事件
        # 点击加号减号事件
        for (i, rect) in enumerate(self.sizes_rect):
            if rect.collidepoint(pos):
                if i:   # i == 1, size down
                    self.brush.set_size(self.brush.get_size() - 0.5)
                else:
                    self.brush.set_size(self.brush.get_size() + 0.5)
                return True
        # 点击颜色按钮事件
        for (i, rect) in enumerate(self.colors_rect):
            if rect.collidepoint(pos):
                self.brush.set_color(self.colors[i])
                return True
        # 点击橡皮按钮事件
        for (i, rect) in enumerate(self.erasers_rect):
            if rect.collidepoint(pos):
                self.brush.set_color(self.eraser_color)
                return True
        return False


class Brush(object):
    def __init__(self, screen):
        self.screen = screen
        self.color = (0, 0, 0)
        self.size = 1
        self.drawing = False    # 是否绘画
        self.last_pos = None    # 鼠标最后划过的位置
        self.space = 1
        self.brush = pygame.image.load('img/pen.png').convert_alpha()   # 画笔图片
        self.brush_now = self.brush.subsurface((0, 0), (1, 1))      # 初始化画笔对象

    # 开始绘画
    def start_drawing(self, pos):
        self.drawing = True
        self.last_pos = pos     # 记录鼠标的最后位置

    # 结束绘画
    def stop_drawing(self):
        self.drawing = False

    # 获取当前使用画笔
    def get_current_brush(self):
        return self.brush_now

    # 控制画笔尺寸
    def set_size(self, size):
        if size < 0.5:  # 画笔最小尺寸0.5
            size = 0.5
        elif size > 32: # 画笔最大尺寸 32
            size = 32
        self.size = size
        self.brush_now = self.brush.subsurface((0, 0), (size * 2, size * 2))

    # 获取画笔大小
    def get_size(self):
        return self.size

    # 设置画笔颜色
    def set_color(self, color):
        self.color = color
        for i in range(self.brush.get_width()):
            for j in range(self.brush.get_height()):
                # 以指定颜色显示画笔
                self.brush.set_at((i, j), color + (self.brush.get_at((i, j)).a,))

    # 获取画笔颜色
    def get_color(self):
        return self.color

    # 获取两点之间所有点位
    def _get_points(self, pos):
        points = [(self.last_pos[0], self.last_pos[1])]
        lenx = pos[0] - self.last_pos[0]
        leny = pos[1] - self.last_pos[1]
        length = math.sqrt(lenx ** 2 + leny ** 2)
        stepx = lenx / length
        stepy = leny / length
        for i in range(int(length)):
            points.append(
                (points[-1][0] + stepx, points[-1][1] + stepy)
            )

if __name__ == '__main__':
    main = Menu('screen')
