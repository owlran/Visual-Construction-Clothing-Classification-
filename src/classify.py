from Extractor import *
import libsvm
import argparse

class classifier:
    def __init__(self):
        self.extractor = Extractor()
        self.fv = None
        self.target_type = None

    def setImgPath(self, imgPath):
        self.extractor.setImgPath(imgPath)

    def getHelmetFeature(self):
        fv = self.extractor.extract_feature('','hs+lbp',h_bins=8,s_bins=48)
        fv = fv.strip()
        return fv

    def getVestFeature(self):
        fv = self.extractor.extract_feature('','lbp+hs',h_bins=128,s_bins=32)
        fv = fv.strip()
        return fv

    def outputFeatureFile(self):
        fv_data = open('testingdata.svm', 'w')
        fv_data.write(self.fv)
        fv_data.close()

    def setTargetType(self,target_type):
        self.target_type = target_type

    def getResult(self):

        if self.target_type == 'helmet':
            self.fv = self.getHelmetFeature()
        else:
            self.fv = self.getVestFeature()

        self.outputFeatureFile()

        if self.target_type == 'helmet':
            test_result = libsvm.test('./testingdata.svm', './svm_model/helmet_data_8_48_lbp.model')
        else:
            test_result = libsvm.test('./testingdata.svm', './trainingdata.svm.model')

        return test_result

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", help="echo", default="Hello world")
    parser.add_argument("-p", "--path", help="image path of svm", \
                        default="./out/hat/frame117_hat.jpg")
    parser.add_argument("-t", "--target_type", help="type of svm model",\
                       default="helmet")
    args = parser.parse_args()
    return args

if __name__=='__main__':
    args = parse_arguments()
    imgPath = args.path
    target_type = args.target_type
    classifier = classifier()
    #imgPath = '/Users/owlran1088/Desktop/fog_0176.jpg'
    classifier.setImgPath(imgPath)
    classifier.setTargetType(target_type)

    if target_type == 'helmet':
        classifier.fv = classifier.getHelmetFeature()
    else:
        classifier.fv = classifier.getVestFeature()

    classifier.outputFeatureFile()
    test_result = classifier.getResult()

    print test_result
