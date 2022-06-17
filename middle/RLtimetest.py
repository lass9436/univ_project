from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import PIL.Image as pilimg
from PIL import ImageGrab
import numpy as np
import time
from glob import glob

from PIL import Image
import cv2


new_model = tf.keras.models.load_model('C:\\python\\DeepLearning\\model\\1stCNN64.h5')
new_model.summary ()


a = 1
b = 0
cap = cv2.VideoCapture(0)
while(a):
    _, frame = cap.read()
    
    
    frame1 = cv2.resize(frame, (64, 64))

    
    test1=np.array(frame1)
    test = []
    test.append(test1)
    
    test = (np.array(test, dtype=np.float64))/255.0
    #print(test.shape)
    
    awef = new_model.predict(test)
    #print(awef)
    result=awef[0]
    #print(result)
    res=result.tolist()
    #print(res)
    ff=max(res)
    fp=res.index(ff)
    #print(fp)
    if fp == 0:
        print("\n")
        print("0")
       
    elif fp == 1:
        print("\n")
        print("1")
       
    elif fp == 2:
        print("\n")
        print("2")
        
    elif fp == 3:
        print("\n")
        print("3")
        
    elif fp == 4:
        print("\n")
        print("4")
        
    elif fp == 5:
        print("\n")
        print("5")
        
    elif fp == 6:
        print("\n")
        print("6")
        
    elif fp == 7:
        print("\n")
        print("7")
        
    elif fp == 8:
        print("\n")
        print("8")
    else:
        print("\n")
        print("9")
    
    
    cv2.imshow('awef',frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break    
    print(awef)
    
    
predictions_single = model.predict(img)
print(predictions_single)
result=predictions_single[0]
print(result)
res=result.tolist()
print(res)
ff=max(res)
fp=res.index(ff)
print(fp)