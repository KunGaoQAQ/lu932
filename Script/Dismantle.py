from PIL import Image

def split_image_by_lines(input_image_path, output_folder):
    try:
        # 打开图片
        image = Image.open(input_image_path)

        # 转换为灰度图像
        gray_image = image.convert('L')
        gray_image.save('gray_image.jpg')


        # 二值化处理
        threshold = 225
        binary_image = gray_image.point(lambda p: 255 if p > threshold else 0)
        binary_image.save('binary_image.jpg')

        width, height = binary_image.size
        lines = []
        in_line = False
        start_y = 0

        # 行切分
        for y in range(height):
            line_empty = True
            for x in range(width):
                if binary_image.getpixel((x, y)) == 0:
                    line_empty = False
                    break
            if not in_line and not line_empty:
                in_line = True
                start_y = y
            elif in_line and line_empty:
                in_line = False
                lines.append((start_y, y))

        # 如果最后一行没有空白行结束，手动添加最后一行
        if in_line:
            lines.append((start_y, height))

        # 保存切分后的图片
        for i, (start_y, end_y) in enumerate(lines):
            line_image = image.crop((0, start_y, width, end_y))
            output_path = f"{output_folder}/line_{i + 1}.png"
            line_image.save(output_path)
            print(f"保存第 {i + 1} 行图片到 {output_path}")

    except Exception as e:
        print(f"处理图片时出现错误: {e}")

input_image_path = r"E:\GitHub Code\lu932\A2.1\tahiti.png"
output_folder = "E:\GitHub Code\lu932\A2.2"
split_image_by_lines(input_image_path, output_folder)