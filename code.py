import cv2
import numpy as np
import scipy
from matplotlib.pyplot import imread
import pickle as pickle
from scipy import spatial
import random
import os
import math
import matplotlib.pyplot as plt

# Feature extractor
def extract_features(image_path, vector_size=32):
    image = imread(image_path)
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print ('Error: ', e)
        return None
    #print(dsc)
    
    return dsc

result = {}


def batch_extractor(images_path):
    folders = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    i = 0
    for f in folders:
        print ('Extracting features from image %s' % f)
        name = f.split('/')[-1]
        #print(name)
        result[name] = extract_features(f)

    
def show_img(path):
    img = imread(path)
    plt.imshow(img)
    plt.show()

# fungsi distance
def dist(vec1, vec2):
    result = 0;
    for i in range(len(vec1)):
        result+= (vec1[i]-vec2[i])*(vec1[i]-vec2[i])
    return math.sqrt(result)

# fungsi cosine similarity 
def CosSimilarity(vec1,vec2):
    result = 0;
    dotProduct = 0;
    
    for i in range(len(vec1)):
        dotProduct+=vec1[i]*vec2[i];
        
    skalarVec1  = 0;
    for e in vec1:
        skalarVec1 += e*e;
    skalarVec1 = math.sqrt(skalarVec1)
    
    skalarVec2  = 0;
    for e in vec2:
        skalarVec2 += e*e;
    skalarVec2 = math.sqrt(skalarVec2)
    
    return dotProduct/(skalarVec1*skalarVec2)


pathFolder = 'D:/download/pins-face-recognition/PINS/PINS/'

batch_extractor('D:/download/pins-face-recognition/PINS/PINS/pins_Jon Bernthal')


imageTarget = 'D:/download/pins-face-recognition/PINS/PINS/pins_Jon Bernthal/Jon Bernthal0_2150.jpg'
vectorTarget = extract_features(imageTarget)

'''
for k in dictVector:
    print(dictVector[k])
'''

metode = print("Masukkan pilihan netode (1.Cos Similarity 2.Euclidan Distance)")

resultComparison = []

if (metode==1):
    for key in result:
        hasil = CosSimilarity(result[key],vectorTarget)
        resultComparison.append((hasil,key))
else if (metode==2):
    for key in result:
        hasil = dist(result[key],vectorTarget)
        resultComparison.append((hasil,key))
    
show_img(imageTarget)    

resultComparison.sort();
print(len(resultComparison))
for i in range(10):
    print(resultComparison[i][0]);
    print(resultComparison[i][1]);
    show_img(os.path.join(pathFolder,resultComparison[i][1] ));
    
