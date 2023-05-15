import cv2
image = cv2.imread("cv4.webp", cv2.IMREAD_COLOR)
cv2.imshow("title", image)
scale_percent = 50
new_width = int(image.shape[1]*scale_percent/100)
new_height = int(image.shape[0]*scale_percent/100)
output = cv2.resize(image, (new_height, new_width))
cv2.imwrite('newimage.png', output)
cv2.waitKey(0)
