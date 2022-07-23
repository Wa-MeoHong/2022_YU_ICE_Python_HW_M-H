
# 파일명 : Handwritten Digits.py
# 프로그램 목적 및 기능: 파이썬 필기체 프로그램
# 프로그램 작성자 : 신대홍(2022년 6월 5일)
# 최종 Update : Version 1.0.0, 2022년 6월 5일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/06/05     v1.0.0       최초작성

import tensorflow as tf
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
#from keras.utils import to_categorical

kr_utils = tf.keras.utils
from keras import backend as k
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#keras 라이브러리에서 데이터 셋 로드
print("Loading MNIST data . . . .")
mnist_npz_path = 'C://MyPyPackage//MNIST//mnist.npz'
(X_train, y_train), (X_test, y_test) = mnist.load_data(path= mnist_npz_path)

digit_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
plt.figure(figsize=(10,5))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_train[i], cmap="gray")
    plt.title(digit_names[y_train[i]])
    plt.axis('off')
plt.show()

# reshape format [samples][width][height][channels]
print("Reshaping format . . . .")
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32')

print("Converting class vector . . . .")
# 2진 클래스 행렬로 벡터를 전환
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)

# input 정상화
X_train = X_train / 255
X_test = X_test / 255

print("Preparing a CNN model . . . .")
# CNN모델 정의
num_classes = 10
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')])
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print("Fitting the model . . . .")
# 모델 맞추기
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20,
batch_size=200, verbose=2)
print("The model has successfully trained")

# 모델 저장
model.save("/content/drive/MyDrive/mnist.npz")
print("The model has successfully saved !!")
model.summary() # 모델 출력

# 모델 평가
scores = model.evaluate(X_test, y_test, verbose=0)
print("CNN error: %.2f%%" %(100 - scores[1]*100))