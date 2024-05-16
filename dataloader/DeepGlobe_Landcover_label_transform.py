import cv2
import numpy as np
import os

# DeepGlobe_Landcover label projection
color_to_gray_mapping = {
    (0, 255, 255):   0,   # urban_land
    (255, 255, 0):   1,   # agriculture_land
    (255, 0, 255):   2,   # rangeland
    (0, 255, 0):     3,   # forest_land
    (0, 0, 255):     4,   # water
    (255, 255, 255): 5,   # barren_land
    (0, 0, 0):       6,   # unknown
}


def label_transform(label_path):
    # 读取彩色标签图像
    color_label_image = cv2.imread(label_path)  # 替换为实际图像路径

    # 根据映射将彩色图像转换为灰度图像
    color_label_array = color_label_image[..., ::-1]  # BGR转RGB
    gray_label_array = np.zeros(color_label_array.shape[:2], dtype=np.uint8)

    for color, gray_value in color_to_gray_mapping.items():
        mask = np.all(color_label_array == color, axis=-1)
        gray_label_array[mask] = gray_value

    return gray_label_array


label_dir = './data'
# 遍历文件夹下的所有文件和子文件夹
for root, dirs, labels in os.walk(label_dir):
    for label in labels:
        if 'mask' in label:    
            label_path = os.path.join(root, label)
            print("label_path:", label_path)
            gray_label = label_transform(label_path)
            cv2.imwrite(label_path, gray_label)  # 替换为保存路径
