import cv2
import os
import numpy as np


def combine(img1, img2):
    #combined_image = np.concatenate((img1, img2), axis = 1)
    combined_image = cv2.hconcat([img1, img2])
    return combined_image


image1  = cv2.imread("/users/satish/desktop/img1.png", cv2.IMREAD_COLOR)
image2 = cv2.imread("/users/satish/desktop/img2.png", cv2.IMREAD_COLOR)

image_3 = combine(image1, image2)

cv2.imshow("Output", image_3)
cv2.waitKey(0)
cv2.destroyAllWindows()
