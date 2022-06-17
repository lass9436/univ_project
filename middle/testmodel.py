from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import PIL.Image as pilimg
import numpy as np
from PIL import Image


model=tf.keras.models.load_model('C:\\python\\DeepLearning\\model\\1stCNN32.h5')
img= (np.array(pilimg.open('C:\\python\\DeepLearning\\testdata32\\pose01\\0000.jpg')))/255.0
img = (np.expand_dims(img,0))
print(img.shape)

predictions_single = model.predict(img)
print(predictions_single)
result=predictions_single[0]
print(result)
res=result.tolist()
print(res)
ff=max(res)
fp=res.index(ff)
print(fp)