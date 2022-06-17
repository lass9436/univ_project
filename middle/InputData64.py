import numpy as np
import PIL.Image as pilimg
from glob import glob

#훈련 이미지 데이터, 훈련 정답 레이블 만들기

#훈련 이미지의 모든 경로 불러오기
data_list01 = glob('C:\\python\\DeepLearning\\traindata64\\pose01\\*.jpg')
length01=len(data_list01)

data_list02 = glob('C:\\python\\DeepLearning\\traindata64\\poes02\\*.jpg')
length02=len(data_list02)

data_list03 = glob('C:\\python\\DeepLearning\\traindata64\\pose03\\*.jpg')
length03=len(data_list03)

data_list04 = glob('C:\\python\\DeepLearning\\traindata64\\pose04\\*.jpg')
length04=len(data_list04)

data_list05 = glob('C:\\python\\DeepLearning\\traindata64\\pose05\\*.jpg')
length05=len(data_list05)

data_list06 = glob('C:\\python\\DeepLearning\\traindata64\\pose06\\*.jpg')
length06=len(data_list06)

data_list07 = glob('C:\\python\\DeepLearning\\traindata64\\pose07\\*.jpg')
length07=len(data_list07)

data_list08 = glob('C:\\python\\DeepLearning\\traindata64\\pose08\\*.jpg')
length08=len(data_list08)

data_list09 = glob('C:\\python\\DeepLearning\\traindata64\\pose09\\*.jpg')
length09=len(data_list09)

data_list10 = glob('C:\\python\\DeepLearning\\traindata64\\pose10\\*.jpg')

length10=len(data_list10)

Data_length=length01+length02+length03+length04+length05+length06+length07+length08+length09+length10
train_images = np.zeros((Data_length, 64, 64, 3))

# 경로에서 훈련 이미지들을 불러와서 넘파이배열로 만들기

for i in range(0,10):
    if(i==0):
        for j in range(length01):
            train_images[j:,:,:]=(np.array(pilimg.open(data_list01[j])))/255.0
            print(i,j)
    elif(i==1):
        for j in range(length02):
            train_images[j+length01:,:,:]=(np.array(pilimg.open(data_list02[j])))/255.0
            print(i,j)
    elif(i==2):
        for j in range(length03):
            train_images[j+length01+length02:,:,:]=(np.array(pilimg.open(data_list03[j])))/255.0
            print(i,j)
    elif(i==3):
        for j in range(length04):
            train_images[j+length01+length02+length03:,:,:]=(np.array(pilimg.open(data_list04[j])))/255.0
            print(i,j)
    elif(i==4):
        for j in range(length05):
            train_images[j+length01+length02+length03+length04:,:,:]=(np.array(pilimg.open(data_list05[j])))/255.0
            print(i,j)
    elif(i==5):
        for j in range(length06):
            train_images[j+length01+length2+length03+length04+length05:,:,:]=(np.array(pilimg.open(data_list06[j])))/255.0
            print(i,j)
    elif(i==6):
        for j in range(length07):
            train_images[j+length01+length2+length03+length04+length05+length06:,:,:]=(np.array(pilimg.open(data_list07[j])))/255.0
            print(i,j)
    elif(i==7):
        for j in range(length08):
            train_images[j+length01+length2+length03+length04+length05+length06+length07:,:,:]=(np.array(pilimg.open(data_list08[j])))/255.0
            print(i,j)
    elif(i==8):
        for j in range(length09):
            train_images[j+length01+length2+length03+length04+length05+length06+length07+length08:,:,:]=(np.array(pilimg.open(data_list09[j])))/255.0
            print(i,j)
    elif(i==9):
        for j in range(length10):
            train_images[j+length01+length2+length03+length04+length05+length06+length07+length08+length09:,:,:]=(np.array(pilimg.open(data_list10[j])))/255.0
            print(i,j)        
    else:
        break
        

#훈련 정답 레이블 만들기

train_labels = [[0 for col in range(1)] for row in range(Data_length)]

for i in range(0,Data_length):
    if(i<length01):
        train_labels[i][0] = 0
    elif(i<length01+length02):
        train_labels[i][0] = 1
    elif(i<length01+length02+length03):
        train_labels[i][0] = 2
    elif(i<length01+length02+length03+length04):
        train_labels[i][0] = 3
    elif(i<length01+length02+length03+length04+length05):
        train_labels[i][0] = 4
    elif(i<length01+length02+length03+length04+length05+length06):
        train_labels[i][0] = 5
    elif(i<length01+length02+length03+length04+length05+length06+length07):
        train_labels[i][0] = 6
    elif(i<length01+length02+length03+length04+length05+length06+length07+length08):
        train_labels[i][0] = 7
    elif(i<length01+length02+length03+length04+length05+length06+length07+length08+length09):
        train_labels[i][0] = 8
    else:
        train_labels[i][0] = 9
     

train_labels = np.array(train_labels)



#시험 데이타 이미지, 시험 정답 레이블 만들기

data_list01 = glob('C:\\python\\DeepLearning\\testdata64\\pose01\\*.jpg')
length01=len(data_list01)

data_list02 = glob('C:\\python\\DeepLearning\\testdata64\\poes02\\*.jpg')
length02=len(data_list02)

data_list03 = glob('C:\\python\\DeepLearning\\testdata64\\pose03\\*.jpg')
length03=len(data_list03)

data_list04 = glob('C:\\python\\DeepLearning\\testdata64\\pose04\\*.jpg')
length04=len(data_list04)

data_list05 = glob('C:\\python\\DeepLearning\\testdata64\\pose05\\*.jpg')
length05=len(data_list05)

data_list06 = glob('C:\\python\\DeepLearning\\testdata64\\pose06\\*.jpg')
length06=len(data_list06)

data_list07 = glob('C:\\python\\DeepLearning\\testdata64\\pose07\\*.jpg')
length07=len(data_list07)

data_list08 = glob('C:\\python\\DeepLearning\\testdata64\\pose08\\*.jpg')
length08=len(data_list08)

data_list09 = glob('C:\\python\\DeepLearning\\testdata64\\pose09\\*.jpg')
length09=len(data_list09)

data_list10 = glob('C:\\python\\DeepLearning\\testdata64\\pose10\\*.jpg')

length10=len(data_list10)

Data_length=length01+length02+length03+length04+length05+length06+length07+length08+length09+length10
test_images = np.zeros((Data_length, 64, 64, 3))

# 경로에서 시험 이미지들을 불러와서 넘파이배열로 만들기

for i in range(0,10):
    if(i==0):
        for j in range(length01):
            test_images[j:,:,:]=(np.array(pilimg.open(data_list01[j])))/255.0
            print(i,j)
    elif(i==1):
        for j in range(length02):
            test_images[j+length01:,:,:]=(np.array(pilimg.open(data_list02[j])))/255.0
            print(i,j)
    elif(i==2):  
        for j in range(length03):
            test_images[j+length01+length02:,:,:]=(np.array(pilimg.open(data_list03[j])))/255.0
            print(i,j)
    elif(i==3):
        for j in range(length04):
            test_images[j+length01+length02+length03:,:,:]=(np.array(pilimg.open(data_list04[j])))/255.0
            print(i,j)
    elif(i==4):
        for j in range(length05):
            test_images[j+length01+length02+length03+length04:,:,:]=(np.array(pilimg.open(data_list05[j])))/255.0
            print(i,j)
    elif(i==5):
        for j in range(length06):
            test_images[j+length01+length02+length03+length04+length05:,:,:]=(np.array(pilimg.open(data_list06[j])))/255.0
            print(i,j)
    elif(i==6):
        for j in range(length07):
            test_images[j+length01+length02+length03+length04+length05+length06:,:,:]=(np.array(pilimg.open(data_list07[j])))/255.0
            print(i,j)
    elif(i==7):
        for j in range(length08):
            test_images[j+length01+length02+length03+length04+length05+length06+length07:,:,:]=(np.array(pilimg.open(data_list08[j])))/255.0
            print(i,j)
    elif(i==8):
        for j in range(length09):
            test_images[j+length01+length02+length03+length04+length05+length06+length07+length08:,:,:]=(np.array(pilimg.open(data_list09[j])))/255.0
            print(i,j)
    elif(i==9):
        for j in range(length10):
            test_images[j+length01+length02+length03+length04+length05+length06+length07+length08+length09:,:,:]=(np.array(pilimg.open(data_list10[j])))/255.0
            print(i,j)        
    else:
        break
        

#시험 정답 레이블 만들기

test_labels = [[0 for col in range(1)] for row in range(Data_length)]

for i in range(0,Data_length):
    if(i<length01):
        test_labels[i][0] = 0
    elif(i<length01+length02):
        test_labels[i][0] = 1
    elif(i<length01+length02+length03):
        test_labels[i][0] = 2
    elif(i<length01+length02+length03+length04):
        test_labels[i][0] = 3
    elif(i<length01+length02+length03+length04+length05):
        test_labels[i][0] = 4
    elif(i<length01+length02+length03+length04+length05+length06):
        test_labels[i][0] = 5
    elif(i<length01+length02+length03+length04+length05+length06+length07):
        test_labels[i][0] = 6
    elif(i<length01+length02+length03+length04+length05+length06+length07+length08):
        test_labels[i][0] = 7
    elif(i<length01+length02+length03+length04+length05+length06+length07+length08+length09):
        test_labels[i][0] = 8
    else:
        test_labels[i][0] = 9
     

test_labels = np.array(test_labels)

## 훈련 이미지, 훈련 레이블, 시험 이미지, 시험 레이블을 모두 넘파이 배열로 데이터셋을 준비하였다.



# 각 데이터셋들을 확인한다.

print(train_images.shape)
print(train_labels.shape)
print(test_images.shape)
print(test_labels.shape)

np.save('C:\\python\\DeepLearning\\numpydata\\train_images64.npy', train_images)
np.save('C:\\python\\DeepLearning\\numpydata\\train_labels64.npy', train_labels)
np.save('C:\\python\\DeepLearning\\numpydata\\test_images64.npy', test_images)
np.save('C:\\python\\DeepLearning\\numpydata\\test_labels64.npy', test_labels)