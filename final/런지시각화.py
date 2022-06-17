from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from math import *

fig = plt.figure()
ax = Axes3D(fig)

data = np.load('./final_project/런지.npy')
len1=len(data)

xs=[]
ys=[]
zs=[]



def update(frame):
    ax.clear()

    u0 = (data[0][8][1] + data[0][11][1])/2
    u1 = (data[0][9][1] + data[0][12][1])/2
    u2 = (data[frame][8][1] + data[frame][11][1])/2
    u3 = (data[frame][9][1] + data[frame][12][1])/2
    p = (1-(u2-u3)/(u0-u1))*100
    
    z1 = data[frame][9][0]
    z2 = data[frame][12][0]
    
    a1 = data[frame][9][1]
    a2 = data[frame][10][1]
    a3 = data[frame][12][1]
    a4 = data[frame][13][1]
    
    b1 = data[frame][10][0]
    b2 = data[frame][13][0]
    
    h = data[frame][0][0]
    
    if p <= 10 :
        #print("연두")
        pp = 'greenyellow'
    elif 0 < p < 100 :
        #print("초록")
        pp = 'green'
    else :
        #print("빨강")
        pp = 'red'
    
    print(p)
    
    if z1 <= z2 and 0.8<a3/(a4+0.0001)<1.2 :
        #print("무릎통과")
        w1 = 0
    elif z1 > z2 and 0.8<a1/(a2+0.0001)<1.2 : 
        #print("무릎통과")
        w1 = 0
    else :
        #print("무릎경고")
        w1 = 1
    if z1 <= z2 and z2 <= b2 :
        #print("다리통과")
        w2 = 0
    elif z1 > z2 and z1 <= b1 : 
        #print("다리통과")
        w2 = 0
    else :
        #print("다리경고")
        w2 = 1
        
    if z1 <= z2 and z2 > h :
        #print("상체통과")
        w3 = 0
    elif z1 > z2 and z1 > h : 
        #print("상체통과")
        w3 = 0
    else :
        #print("상체경고")
        w3 = 1
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim3d(-100,200)
    ax.set_ylim3d(100,-200)
    ax.set_zlim3d(300,0)
    xs=[]
    ys=[]
    zs=[]
    for i in [0,1,14]:
        xs.append(data[frame][i][0])
        ys.append(data[frame][i][1])
        zs.append(data[frame][i][2]) 
        ax.plot3D(xs,zs,ys,c='{}'.format(pp),marker='o')
    xs=[]
    ys=[]
    zs=[]
    for i in [1,2,3,4]:
        xs.append(data[frame][i][0])
        ys.append(data[frame][i][1])
        zs.append(data[frame][i][2]) 
        ax.plot3D(xs,zs,ys,c='{}'.format(pp),marker='o')
    xs=[]
    ys=[]
    zs=[]
    for i in [1,5,6,7]:
        xs.append(data[frame][i][0])
        ys.append(data[frame][i][1])
        zs.append(data[frame][i][2]) 
        ax.plot3D(xs,zs,ys,c='{}'.format(pp),marker='o')
    xs=[]
    ys=[]
    zs=[]
    for i in [14,8,9,10]:
        xs.append(data[frame][i][0])
        ys.append(data[frame][i][1])
        zs.append(data[frame][i][2]) 
        ax.plot3D(xs,zs,ys,c='{}'.format(pp),marker='o')
    xs=[]
    ys=[]
    zs=[]
    for i in [14,11,12,13]:
        xs.append(data[frame][i][0])
        ys.append(data[frame][i][1])
        zs.append(data[frame][i][2]) 
        ax.plot3D(xs,zs,ys,c='{}'.format(pp),marker='o')

    if w1 == 1:
        xs=[]
        ys=[]
        zs=[]
        for i in [9]:
            xs.append(data[frame][i][0])
            ys.append(data[frame][i][1])
            zs.append(data[frame][i][2]) 
            ax.plot3D(xs,zs,ys,c='red',marker='o')
        xs=[]
        ys=[]
        zs=[]
        for i in [12]:
            xs.append(data[frame][i][0])
            ys.append(data[frame][i][1])
            zs.append(data[frame][i][2]) 
            ax.plot3D(xs,zs,ys,c='red',marker='o')
            
    if w2 == 1:
        xs=[]
        ys=[]
        zs=[]
        for i in [8,9,10]:
            xs.append(data[frame][i][0])
            ys.append(data[frame][i][1])
            zs.append(data[frame][i][2]) 
            ax.plot3D(xs,zs,ys,c='red',marker='o')
        xs=[]
        ys=[]
        zs=[]
        for i in [11,12,13]:
            xs.append(data[frame][i][0])
            ys.append(data[frame][i][1])
            zs.append(data[frame][i][2]) 
            ax.plot3D(xs,zs,ys,c='red',marker='o')
            
    if w3 == 1:
        xs=[]
        ys=[]
        zs=[]
        for i in [0,1,14]:
            xs.append(data[frame][i][0])
            ys.append(data[frame][i][1])
            zs.append(data[frame][i][2]) 
            ax.plot3D(xs,zs,ys,c='red',marker='o')
    
    

ani = animation.FuncAnimation(fig=fig, func=update, frames=len1, blit=False, interval=50, repeat=False)

plt.show()