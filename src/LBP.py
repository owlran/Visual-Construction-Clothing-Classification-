import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage.feature import local_binary_pattern

class LBP(object):

    def img_isValid(self, img):
        # input img must be grayscale
        if len(img.shape) > 2:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img

    def compute_LBP_hist(self, img):

        img = self.img_isValid(img)

        LBP_type = 'nri_uniform'
        n_points = 8
        radius = 1
        LBP = local_binary_pattern(img, n_points,radius,LBP_type)

        hist, bins = np.histogram(LBP,59,[0,59])

        return hist

if __name__=="__main__":

    lbp = LBP()

    img = cv2.imread('runner.jpg', 0)

    LBP_hist = lbp.compute_LBP_hist(img)



    cv2.imshow('image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
