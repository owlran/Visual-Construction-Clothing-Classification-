from os.path import exists, isdir, basename, join, splitext
from glob import glob
from numpy import zeros, resize, sqrt, histogram, hstack, vstack, savetxt
from cPickle import dump, HIGHEST_PROTOCOL
import argparse

EXTENSIONS = [".jpg", ".bmp", ".png", ".tif", ".tiff"]
DATABASEPATH = '../dataset'
HISTOGRAMS_FILE = 'trainingdata.svm'


def parse_arguments():
    parser = argparse.ArgumentParser(description='train a visual bag of words model')
    parser.add_argument('-d', help='path to the dataset', required=False, default=DATABASEPATH)
    args = parser.parse_args()
    return args

def get_categories(datasetpath):
    cat_paths = [files
                 for files in glob(datasetpath + "/*")
                  if isdir(files)]
    cat_paths.sort()
    cats = [basename(cat_path) for cat_path in cat_paths]
    return cats


def get_imgfiles(path):
    all_files = []
    all_files.extend([join(path, basename(fname))
                    for fname in glob(path + "/*")
                    if splitext(fname)[-1].lower() in EXTENSIONS])
    return all_files



if __name__=="__main__":
    args = parse_arguments()
    datasetpath = args.d
    print 'dataset path is :', datasetpath

    print "---------------------"
    cats = get_categories(datasetpath)
    ncats = len(cats)
    print "searching for folders at " + datasetpath
    if ncats < 1:
        raise ValueError('Only ' + str(ncats) + ' categories found. Wrong path?')
    print "found following folders / categories:"
    print cats
    print "---------------------"

    all_files = []
    all_files_labels = {}
    all_features = {}
    cat_label = {}

    for cat, label in zip(cats, range(ncats)):
        print cat, label
#        cat_path = join(datasetpath, cat)
#        cat_files = get_imgfiles(cat_path)
#        cat_features = extractSift(cat_files)
#        all_files = all_files + cat_files
#        all_features.update(cat_features)
#        cat_label[cat] = label
#        for i in cat_files:
#            all_files_labels[i] = label

