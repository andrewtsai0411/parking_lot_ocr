import easyocr
import cv2
import matplotlib.pyplot as plt

reader = easyocr.Reader(lang_list=['en'], gpu=False)
img_path = 'data/car_plate_1.jpg'
results = reader.readtext(img_path, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')

x_points = []
y_points = []
for xi, yi in results[0][0]:
    x_points.append(xi)
    y_points.append(yi)
# 取得左上、右下座標
left_top = (min(x_points), min(y_points))
right_buttom = (max(x_points), max(y_points))

img = cv2.imread(img_path)
cv2.rectangle(img, left_top, right_buttom, (0, 255, 0), 5)

plt.imshow(img)
plt.title(f'Plate number :{results[0][-2]}')
plt.show()
