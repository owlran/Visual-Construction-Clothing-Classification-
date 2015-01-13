# Visual-Construction-Clothing-Classifier


### Example use:
  
You train the classifier for a specific dataset with: 

    python learn.py -d path_to_folders_with_images

To classify images use:

    python classify.py -m path_to_folders_with_images/trainingdata.svm.model images_you_want_to_classify

The dataset should have following structure, where all the images belonging to one class are in the same folder:

    .
    |-- path_to_folders_with_images
    |    |-- class1
    |    |-- class2
    |    |-- class3
    ...
    |    └-- classN


## Prerequisites:

To install the necessary libraries run following code from working directory:

    # installing libsvm
    wget -O libsvm.tar.gz http://www.csie.ntu.edu.tw/~cjlin/cgi-bin/libsvm.cgi?+http://www.csie.ntu.edu.tw/~cjlin/libsvm+tar.gz
    tar -xzf libsvm.tar.gz
    mkdir libsvm
    cp -r libsvm-*/* libsvm/
    rm -r libsvm-*/
    cd libsvm
    make
    cp tools/grid.py ../grid.py
    cd ..
    
