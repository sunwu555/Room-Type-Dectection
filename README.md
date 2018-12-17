# Room-Type-Dectection
Course project for EC500K1 Deep learning. A tool using CNN for detecting and bounding sepcific types from floor plan image. Created by Jialiang Shi, Jueru Jin and Wu Sun.

Introduction
---

Room type dection is a course project for EC500K1 deep learning. The goal is to to detect and recognize the certain types room from the raw dloor plan image.

![](https://github.com/sunwu555/Room-Type-Dectection/blob/master/demo.png)

The project is based on darknet framework, which is an open source neural network framework written in C and CUDA. For more information about darknet see here [Darknet project website](http://pjreddie.com/darknet).

Brief Instructions
---

### Testing
1, Clone our project from github

    git clone https://github.com/sunwu555/Room-Type-Dectection
    cd Room-Type-Dectection

2, Install the darknet

    make all

We managed the Makefile so it only use CPU for training and testing. However you can change the Makefile to use GPU and CUDNN for efficiency.

3, Download the pre-trained weight file [HERE](https://drive.google.com/file/d/1wnKuEaZjyvsb1QCPlAe05B-FqaGacX35/view?usp=sharing).

4, Run test

    ./darknet detector test  cfg/voc.data  cfg/yolov3-tiny.cfg  yolov3-tiny-final.weights  test_data/test_image.jpg

Some times the couldn't detect anything because the thresholds bar set to high, you can add

    -thresh 0.2

at the end of test command to change the detection thresholds.

### Training
If you want to add more data into dataset or training more batches, here's some the brief instructions for that.

1, Prepare the dataset

We used a visualized labeling tool called labelImg, you can find it [HERE](https://github.com/tzutalin/labelImg.git)

After labeled the images, the labelImg will generate the .xml files for each image.

You should prepare your files structure as shown below

    --VOC
        --Annotations   # all the .xml files
        --ImageSets
            --Main
        --JPEGImages    # all the .jpg files

Then run the script below to generate the data files for darknet network

    python /scripts/VOCdevkit/VOC2018/filelist.py
    python /scripts/voc_label.py

2, Run the training

You can change the training settings of yolov3-tiny network at

    cfg/yolov3-tiny.cfg

Run the training scripts

    ./darknet detector train cfg/voc.data cfg/yolov3-tiny.cfg

Reference
---

For the darknet framework 

>pjreddie/darknet (https://github.com/kayzhu/LSHash).

For the label tool labelImg 

> tzutalin/labelImg (https://github.com/stefankoegl/kdtree).
