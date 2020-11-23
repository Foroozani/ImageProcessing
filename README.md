# ImageProcessing

Recognition of handwritten characters is one of the most interesting topics in pattern recognition domain. For some scripts such as English, there are standard
datasets available and reviewed, such as  MNIST, CEDAR, CENPARMI.  

## Persian digit dataset

Although Farsi is a right to left script, its digits are written from left to right. Sample handwritten digits is shown in Persian, Arabic, Latin, Urdu.


![](https://github.com/Foroozani/ImageProcessing/blob/main/img/digit.png)

## HODA dataset 

This large dataset of Persian handwritten digits is called Hoda. Binary images of 102,352 digits were extracted from about 12,000 registration forms of two types, filled by B.Sc. and senior high school students. These forms were scanned at 200 dpi with a high speed scanner. A method for finding variety of handwritten digits in a typical dataset is proposed. Based on this method, training and test subsets are provided to facilitate sharing of results among researchers as well as performance comparison [Refrence to the dataset](https://www.sciencedirect.com/science/article/abs/pii/S0167865507000037).

Here different apporach is examined to classify the images. I took both **Hoda** and **MNIST** dataset to study the case. 

## MNIST dataset

The MNIST, modified NIST, 5 dataset (LeCun et al.,1995) was extracted from the NIST datasets SD3 and SD7. Samples are normalized into 20 * 20 gray-scale images with aspect ratio reserved, and the normalized images are located in a 28 * 28 frame. The dataset is available from LeCun. Number of training and test samples are 60,000 and 10,000 respectively.
