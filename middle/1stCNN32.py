from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import numpy as np

#저장해 놓은 넘파이 배열 불러오기

train_images=np.load('C:\\python\\DeepLearning\\numpydata\\train_images32.npy')
train_labels=np.load('C:\\python\\DeepLearning\\numpydata\\train_labels32.npy')
test_images=np.load('C:\\python\\DeepLearning\\numpydata\\test_images32.npy')
test_labels=np.load('C:\\python\\DeepLearning\\numpydata\\test_labels32.npy')

#모델 설정

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(10, (4, 4), strides=1, padding='SAME', kernel_initializer='he_uniform', 
                           bias_initializer='ones', activation='relu', input_shape=(32, 32, 3)),
    tf.keras.layers.MaxPooling2D((4,4)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10,activation='softmax'),
])

#모델 요약

model.summary()

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

model.save('C:\\python\\DeepLearning\\model\\1stCNN32.h5')

print("test loss : ", test_loss)
print("test accuracy : ", test_acc)
