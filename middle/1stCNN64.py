from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import numpy as np

#저장해 놓은 넘파이 배열 불러오기

train_images=np.load('C:\\python\\DeepLearning\\numpydata\\train_images64.npy')
train_labels=np.load('C:\\python\\DeepLearning\\numpydata\\train_labels64.npy')
test_images=np.load('C:\\python\\DeepLearning\\numpydata\\test_images64.npy')
test_labels=np.load('C:\\python\\DeepLearning\\numpydata\\test_labels64.npy')

#모델 설정

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(3, (8, 8), strides=1, kernel_initializer='he_uniform', 
                           activation='relu', input_shape=(64, 64, 3)),
    tf.keras.layers.Conv2D(6, (8, 8), strides=1, kernel_initializer='he_uniform', 
                           activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(9, (8, 8), strides=1, kernel_initializer='he_uniform', 
                           activation='relu'), 
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10,activation='softmax'),
])

#모델 요약

model.summary()

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(train_images, train_labels, epochs=5, 
                    validation_data=(test_images, test_labels))

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

model.save('C:\\python\\DeepLearning\\model\\1stCNN64.h5')

print("test loss : ", test_loss)
print("test accuracy : ", test_acc)

#kernel_initializer='random_uniform',
#bias_initializer='zeros'
#kernel_initializer='glorot_uniform',
#bias_initializer='ones'
#kernel_initializer='he_uniform',
#loss='mean_squared_error',
#loss='sparse_categorical_crossentropy', loss='mean_absolute_error',
#loss='mean_squared_logarithmic_error'
#optimizer='adam'
# metrics=['mse'] metrics=['accuracy'])
# lr=0.005, decay=0
# tf.keras.layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True,
#                                       beta_initializer='zeros', gamma_initializer='ones', moving_mean_initializer='zeros',
#                                      moving_variance_initializer='ones', beta_regularizer=None, gamma_regularizer=None,
#                                      beta_constraint=None, gamma_constraint=None),