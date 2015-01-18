import libsvm
import argparse
from cPickle import load
from  Extractor import Extractor

HISTOGRAMS_FILE = 'testdata.svm'
MODEL_FILE = 'trainingdata.svm.model'
FEATURE_TYPE = 'hog'

def parse_arguments():
    parser = argparse.ArgumentParser(description='classify images with a visual bag of words model')
    parser.add_argument('-m', help='path to the model  file', required=False, default=MODEL_FILE)
    parser.add_argument('input_images', help='images to classify', nargs='+')
    args = parser.parse_args()
    return args


print "---------------------"
print "## extract features"

args = parse_arguments()
model_file = args.m
fnames = args.input_images
fnames = fnames[0]

print 'fnames is %s' % fnames


extractor = Extractor()
extractor.setImgPath(fnames)
fv = extractor.extract_feature(0, FEATURE_TYPE)
print fv
print "---------------------"
print "## test data with svm"
print MODEL_FILE
f = open('test', 'w')
f.write(fv[2:])
f.close()
print libsvm.test('test', MODEL_FILE)

