import cv2
import numpy as np
from matplotlib import pyplot

#img = cv2.imread('lena.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#img = cv2.imread('salt-and-pepperr.jfif')
img = cv2.imread('salt-and-pepper.jfif')

kernel = np.ones((5, 5), np.float32)/25
destImage = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gaussianBlur = cv2.GaussianBlur(img, (5, 5), 0)
medianBlur = cv2.medianBlur(img, 3)
bilateralFilter = cv2.bilateralFilter(img, 5, 75, 75)

titles = ['image', '2D Convolution', 'blur',
          'gaussianBlur', 'medianBlur', 'bilateralFilter']
images = [img, destImage, blur, gaussianBlur, medianBlur, bilateralFilter]

for i in range(6):
    pyplot.subplot(2, 3, i+1), pyplot.imshow(images[i], 'gray')
    pyplot.title(titles[i])
    pyplot.xticks([]), pyplot.yticks([])

pyplot.show()
