import numpy as np
import cv2
import matplotlib.pytplot as plt

### inbuilt function implementation
method = "telea"

flags = cv2.INPAINT_TELEA
if method == "ns":
	flags = cv2.INPAINT_NS

image = cv2.imread("C:/Users/student/PycharmProjects/220962432_lab6/.venv/Scripts/images/origInpaint.png")
image = cv2.resize(image, (300,200))
mask = cv2.imread("C:/Users/student/PycharmProjects/220962432_lab6/.venv/Scripts/images/mask.png", 0)
mask = cv2.resize(mask, (300,200))
# mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

output = cv2.inpaint(image, mask, 2, flags=flags)

cv2.imshow('win', output)
cv2.waitKey(0)
cv2.destroyAllWindows()