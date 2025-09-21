import os
import numpy as np
from PIL import Image


def adaptive_thresholding(image, block_size=22, C=2):
    # 将 PIL 图像转换为 numpy 数组
    img_array = np.array(image, dtype=np.uint8)
    height, width = img_array.shape
    result = np.zeros((height, width), dtype=np.uint8)

    # 遍历图像的每个像素
    for y in range(height):
        for x in range(width):
            # 计算局部邻域的边界
            x1 = max(0, x - block_size // 2)
            x2 = min(width, x + block_size // 2 + 1)
            y1 = max(0, y - block_size // 2)
            y2 = min(height, y + block_size // 2 + 1)

            # 计算局部邻域内像素的总和
            neighborhood = img_array[y1:y2, x1:x2]
            total = np.sum(neighborhood)
            count = neighborhood.size

            # 计算局部均值
            if count > 0:
                mean = total / count
            else:
                mean = 0

            # 计算局部阈值
            threshold = mean - C

            # 进行二值化处理
            pixel = img_array[y, x]
            if pixel > threshold:
                result[y, x] = 255
            else:
                result[y, x] = 0

    # 将 numpy 数组转换回 PIL 图像
    return Image.fromarray(result)


# 输入图片所在文件夹路径
input_folder = 'E:\GitHub Code\lu932\image'
# 输出处理后图片的文件夹路径
output_folder = 'E:\GitHub Code\lu932\B2'

# 检查输出文件夹是否存在，不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中所有 JPG 图片的文件名
image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]

for image_file in image_files:
    try:
        # 构建完整的图片文件路径
        input_image_path = os.path.join(input_folder, image_file)
        # 打开图片并转换为灰度图
        image = Image.open(input_image_path).convert('L')

        # 进行自适应二值化处理
        binary_image = adaptive_thresholding(image)

        # 构建输出图片的完整路径
        output_image_path = os.path.join(output_folder, image_file)
        # 保存处理后的二值化图片
        binary_image.save(output_image_path)
        print(f"处理并保存 {input_image_path} 为 {output_image_path}")
    except Exception as e:
        print(f"处理图片 {image_file} 时出错: {e}")
