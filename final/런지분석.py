import numpy as np
import math

#런지 넘파이 배열 분석

#넘파이배열 불러오기
data=np.load('./output/rdata.npy')


#유사한 프레임 찾기

count=10
set1=[]
set1.append(0)

while count<data.shape[0]-1:
    sum1=0
    sum2=0
    count += 1
    for i in range(8,14):
        sum1=sum1+abs((data[count][i][0]-data[0][i][0]))
        sum2=sum2+abs((data[count][i][1]-data[0][i][1]))
    if (sum1<30)and(sum2<30):
        set1.append(count)
        count+=35
        if count>data.shape[0]:
            break

#세트 프레임 출력

print(set1)
set1=np.array(set1)
set_count=set1.shape[0]
print(set_count-1)

#운동동작 인식

n = 0
x = 210
r = 0
g = 0

while n < 101 :
    z1 = data[x][9][0]
    z2 = data[x][12][0]
    
    a1 = data[x][9][0]
    a2 = data[x][10][0]
    a3 = data[x][12][0]
    a4 = data[x][13][0]
    
    b1 = data[x][10][0]
    b2 = data[x][13][0]
    
    h = data[x][0][0]

    n += 1
    
    if z1 <= z2 and 0.8<a3/a4+0.0001<1.2 :
        print(r,"오1a")
        r += 1
    elif z1 > z2 and 0.8<a1/a2+0.0001<1.2 : 
        print(r,"오1b")
        r += 1
        
    if z1 <= z2 and z2 <= b2 :
        print(r,"오2a")
        r += 1
    elif z1 > z2 and z1 <= b1 : 
        print(r,"오2b")
        r += 1
        
    if z1 <= z2 and z2 > h :
        print(r,"오3a")
        r += 1
    elif z1 > z2 and z1 > h : 
        print(r,"오3b")
        r += 1
        
    if r == 3 :
        print(r,"성공")
        g += 1
        r = 0
    else :
        print(r,"망")
        r = 0
        
    x += 1
    
if g > 100*0.7 :
    print(g,"런지")
    
else :
    print(g,"실패")
    
    
#가동범위 및 경고

rwdata = []
nn = 0
z = 0

while nn < len(data)-1 :
    u0 = (data[0][8][1] + data[0][11][1])/2
    u1 = (data[0][9][1] + data[0][12][1])/2
    u2 = (data[z][8][1] + data[z][11][1])/2
    u3 = (data[z][9][1] + data[z][12][1])/2
    p = (1-(u2-u3)/(u0-u1))*100
    
    z1 = data[z][9][0]
    z2 = data[z][12][0]
    
    a1 = data[z][9][0]
    a2 = data[z][10][0]
    a3 = data[z][12][0]
    a4 = data[z][13][0]
    
    b1 = data[z][10][0]
    b2 = data[z][13][0]
    
    h = data[z][0][0]
    
    if p <= 0 :
        print("하양")
        pp = 0
    elif 0 < p < 100 :
        print("초록")
        pp = 1
    else :
        print("빨강")
        pp = 2
    
    if z1 <= z2 and 0.8<a3/a4+0.0001<1.2 :
        print("무릎통과")
        w1 = 0
    elif z1 > z2 and 0.8<a1/a2+0.0001<1.2 : 
        print("무릎통과")
        w1 = 0
    else :
        print("무릎경고")
        w1 = 1
    if z1 <= z2 and z2 <= b2 :
        print("다리통과")
        w2 = 0
    elif z1 > z2 and z1 <= b1 : 
        print("다리통과")
        w2 = 0
    else :
        print("다리경고")
        w2 = 1
        
    if z1 <= z2 and z2 > h :
        print("상체통과")
        w3 = 0
    elif z1 > z2 and z1 > h : 
        print("상체통과")
        w3 = 0
    else :
        print("상체경고")
        w3 = 1
    nn += 1
    rwdata.append([pp,w1,w2,w3])
    z += 1
    
rwdata    
