#tubes
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
import csv

result = {}

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
        result+= ((vec1[i])-(vec2[i]))*((vec1[i])-(vec2[i]))
    return math.sqrt(result)

# fungsi cosine similarity 
def CosSimilarity(vec1,vec2):
    result = 0.0;
    dotProduct = 0.0;
    
    for i in range(len(vec1)):
        dotProduct+=(vec1[i])*(vec2[i]);
        
    skalarVec1  = 0;
    for e in vec1:
        skalarVec1 += (e)*(e);
    skalarVec1 = math.sqrt(skalarVec1)
    
    skalarVec2  = 0;
    for e in vec2:
        skalarVec2 += (e)*(e);
    skalarVec2 = math.sqrt(skalarVec2)
    
    return dotProduct/(skalarVec1*skalarVec2)



def saveToCsv():
    with open('result_file.csv', mode='w') as result_file:
        result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for key in result:
            temp = []
            for e in result[key]:
                temp.append(str(e))
            temp= [key] + temp
            result_writer.writerow(temp)

def readFromCsv():
    with open('result_file.csv', mode='r') as result_file:
        csv_reader = csv.reader(result_file, delimiter=',')
        line_count = 0
        #result = {}
        print(csv_reader)
        for row in csv_reader:
            #print(row)
            if (len(row)==0): continue
            key = row[0];
            row.pop(0);
            temp = []
            for e in row:
                temp.append(float(e))
            result[key] = temp;


pathFolder = input("Masukkan directory yang lengkap:")

batch_extractor(pathFolder+'Reference')
saveToCsv();

imageTargetName = input("Masukkan nama file image yang ingin dicompare")

imageTarget = pathFolder+'Test'+imageTargetName
vectorTarget = extract_features(imageTarget)


readFromCsv();

print("Pilihan metode\n1.Cos Similarity\n2.Euclidan Distance")
metode = int(input("Masukkan input : "))

print(result)
resultComparison = []
if (metode==1):
    for key in result:
        hasil = CosSimilarity(result[key],vectorTarget)
        resultComparison.append((hasil,key))
    resultComparison.sort(reverse = True);
elif(metode==2):
    for key in result:
        hasil = dist(result[key],vectorTarget)
        resultComparison.append((hasil,key))
    resultComparison.sort();
    
show_img(imageTarget)    

print(len(resultComparison))
for i in range(10):
    print(resultComparison[i][0]);
    print(resultComparison[i][1]);
    show_img(os.path.join(pathFolder,resultComparison[i][1]));
    
