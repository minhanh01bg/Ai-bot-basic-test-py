import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize']=[10,8]
img = cv2.imread("F:\\picture\\abstract-nature-7680x4320-8k-21456.jpg",0)
h2 = np.histogram(img.ravel(),bins=256,range=[0,256])
print(h2[0].shape)
plt.plot(h2[0])
