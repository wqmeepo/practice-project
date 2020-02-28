from PIL import Image, ImageDraw, ImageFont
import numpy

scale = 1  # 设置缩放比例
default_char = '!@#$%^&*asdfghjkl田凌'  # 设置默认字符
'''
    该方法用于字符画图片的转换与生成
    import_img: 该参数指定图片的原路径
    export_img: 该参数指定图片转换为字符画后的输出路径
    input_char: 该参数指定自定义字符画中的字符内容，为空使用默认字符
    pix_distance: 该参数为字符画的字符密度，3 为清晰，4为一般，5为字符 
'''


def picture_conversion(import_img, export_img=None, input_char='', pix_distance=''):
    img = Image.open(import_img)
    img_pix = img.load()  # 获取图片像素
    img_weight = img.size[0]  # 获取图片宽度
    img_height = img.seze[1]  # 获取图片高度
    # 创建画布数组对象
    canvas_array = numpy.ndarray((img_height * scale, img_weight * scale, 3), numpy.uint8)
    canvas_array[:, :, :] = 255  # 设置画布的三原色255，255，255白色
    new_image = Image.fromarray(canvas_array)  # 根据画布创建图像
    img_draw = ImageDraw.Draw(new_image)  # 创建图像绘制对象
    font = ImageFont.truetype('simsun.ttc', 10)  # 字库类型
    # 判断字符画使用的字符
    if input_char == '':
        char_list = list(default_char)
    else:
        char_list = list(input_char)
    # 判断清晰度
    if pix_distance == '清晰':
        pix_distance = 3
    elif pix_distance == '一般':
        pix_distance = 4
    elif pix_distance == '字符':
        pix_distance = 5
    # 开始绘制
    pix_count = 0  # 记录绘制的字符像素点数量
    table_len = len(char_list)  # 字符长度
    for y in range(img_height):  # 根据图片高度获取y坐标
        for x in range(img_weight):  # 根据图片宽度获取x坐标
            if x % pix_distance == 0 and y % pix_distance == 0:  # 判断字符间隔位置
                # 实现根据图片像素绘制字符
                img_draw.text((x * scale, y * scale), char_list[pix_count % table_len], img_pix[x, y], font)
                # img_draw.text(坐标，内容，颜色，字体)
                pix_count += 1  # 叠加绘制字符像素点数量
        # 保存
    if export_img is not None:  # 判断是否设置了新图片保存的位置与路径
        new_image.save()  # 实现字符图片的保存
    return False  # 转换完毕
