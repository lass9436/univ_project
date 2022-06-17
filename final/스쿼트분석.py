import numpy as np
import math

#스쿼트 넘파이 배열 분석

#넘파이배열 불러오기
data=np.load('./final_project/스쿼트.npy')


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
x = 7
r = 0
g = 0

while n < 86 :
    a1 = data[x][2][0]
    a2 = data[x+1][2][0]
    a3 = data[x][5][0]
    a4 = data[x+1][5][0]
    a5 = data[x][2][1]
    a6 = data[x+1][2][1]
    
    b1 = data[x][9][0]
    b2 = data[x+1][9][0]
    b3 = data[x][12][0]
    b4 = data[x+1][12][0]
    
    tx = (data[x][8][0]-data[x][11][0])/2
    ty = (data[x][8][1]-data[x][11][1])/2
    tz = (data[x][8][2]-data[x][11][2])/2
    l1 = (data[x][14][1]-ty)/(data[x][14][2]-tz)+0.0001
    l2 = (data[x][14][1]-data[x][1][1])/(data[x][14][2]-data[x][1][2])+0.0001

    n += 1
    
    if 0.8<a1/a2+0.0001<1.2 and 0.8<a3/a4+0.0001<1.2 :
        print(r,"오1")
        r += 1
        
    if 0.8<b1/b2+0.0001<1.2 and 0.8<b3/b4+0.0001<1.2 :
        print(r,"오2")
        r += 1
        
    if l1 <= l2 :
        print(r,"오3")
        r += 1
        
    if r == 3 :
        print(r,"성공")
        g += 1
        r = 0
    else :
        print(r,"망")
        r = 0
        
    x += 1
    
if g > 85*0.7 :
    print(g,"스쿼트")
    
else :
    print(g,"실패")
    
    
#가동범위 및 경고

wdata = []
nn = 0
z = 0

while nn < len(data)-1 :
    u0 = (data[0][8][1] + data[0][11][1])/2
    u1 = (data[0][9][1] + data[0][12][1])/2
    u2 = (data[z][8][1] + data[z][11][1])/2
    u3 = (data[z][9][1] + data[z][12][1])/2
    p = (1-(u0-u1)/(u2-u3))*100
    
    k1 = data[0][12][0] - data[0][9][0]
    k2 = data[z][12][0] - data[z][9][0]
    
    n1 = data[0][9][0]
    n2 = data[z][9][0]
    n3 = data[0][12][0]
    n4 = data[z][12][0]
    
    tx = (data[z][8][0]-data[z][11][0])/2
    ty = (data[z][8][1]-data[z][11][1])/2
    tz = (data[z][8][2]-data[z][11][2])/2
    l1 = (data[z][14][1]-ty)/(data[z][14][2]-tz)+0.0001
    l2 = (data[z][14][1]-data[z][1][1])/(data[z][14][2]-data[z][1][2])+0.0001
    
    if p <= 0 :
        print("하양")
        pp = 0
    elif 0 < p < 100 :
        print("초록")
        pp = 1
    else :
        print("빨강")
        pp = 2
    
    print(p)
    
    if k1 < k2 :
        print("무릎경고")
        w1 = 1
    else :
        print("무릎통과")
        w1 = 0
        
    if 0.8<n1/n2+0.0001<1.2 and 0.8<n3/n4+0.0001<1.2 :
        print("어깨통과")
        w2 = 0
    else :
        print("어깨경고")
        w2 = 1
        
    if l1 > l2 :
        print("척추경고")
        w3 = 1
    else :
        print("척추통과")
        w3 = 0
    nn += 1
    wdata.append([pp,w1,w2,w3])
    z += 1
    
wdata    
