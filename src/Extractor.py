from __future__ import division
import cv2
import LBP
from skimage.feature import hog


class Extractor:
    def __init__(self):
        pass

    def help(self):
        print 'this module used to extract feautres and output svm format data'
        print 'usage is:'
        print 'extractor = Extractor()'
        print 'extractor.setImg(imgPath)'
        print 'extractor.extract_feature(label, feature_type)'
        print 'label starts from 1 index, then +2, +3 .. etc'
        print 'type is feature type, such as hue, saturation, lbp'

#    def setExtractionMode(self, mode):
#        if mode == 'helmet':
#            self.setScaleHeight = 70
#            self.setScaleWidth = 40
#        else:
#            self.setScaleHeight = 110
#            self.setScaleWidth = 70

#    def setScaleHeight(self, height):
#        self.scale_Height = height
#
#   def setScaleWidth(self, width):
#        self.scale_Width = width

    def setImgPath(self, imgPath):
        self.img = cv2.imread(imgPath)
        self.path = imgPath
        #print imgPath
        #self.img = cv2.resize(self.img, (self.scale_Height, self.scale_Width))

    def extract_feature(self, label, feature_type, h_bins=16, s_bins=16):
        # retun valus is a string which is a feature vector with label
        fv = '%s ' % label
        index = 1

        if feature_type == 'hs':
            hsvImg = cv2.cvtColor(self.img,cv2.COLOR_BGR2HSV)
            h_hist = cv2.calcHist([hsvImg], [0], None, [h_bins], [0, 180])
            s_hist = cv2.calcHist([hsvImg], [1], None, [s_bins], [0, 255])

            #normalize histogram
            h_hist = [element/sum(h_hist) for element in h_hist]
            s_hist = [element/sum(s_hist) for element in s_hist]

            for eachBin in h_hist:
                fv = fv + '%d:%f ' % (index, eachBin)
                index = index + 1

            for eachBin in s_hist:
                fv = fv + '%d:%f ' % (index, eachBin)
                index = index + 1

        elif feature_type == 'lbp':
            lbp = LBP.LBP()
            print self.path
            lbp_hist = lbp.compute_LBP_hist(self.img)

            for eachBin in lbp_hist:
                fv = fv + '%d:%f ' % (index, eachBin)
                index = index + 1

        elif feature_type == 'hs+lbp':
            hsvImg = cv2.cvtColor(self.img,cv2.COLOR_BGR2HSV)
            h_hist = cv2.calcHist([hsvImg], [0], None, [h_bins], [0,180])
            s_hist = cv2.calcHist([hsvImg], [1], None, [s_bins], [0,255])

            #normalize histogram
            h_hist = [element/sum(h_hist) for element in h_hist]
            s_hist = [element/sum(s_hist) for element in s_hist]

            lbp = LBP.LBP()
            lbp_hist = lbp.compute_LBP_hist(self.img)
            lbp_hist = [element/sum(lbp_hist) for element in lbp_hist]

            for eachBin in h_hist:
                fv = fv + '%d:%f ' % (index, eachBin)
                index = index + 1

            for eachBin in s_hist:
                fv = fv + '%d:%f ' % (index, eachBin)
                index = index + 1

            for eachBin in lbp_hist:
                fv = fv + '%d:%f ' % (index, eachBin)
                index = index + 1

        return fv
