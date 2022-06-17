from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from math import *

fig = plt.figure()
ax = Axes3D(fig)

data = np.load('./final_project/스쿼트.npy')
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
    p = (1-(u0-u1)/(u2-u3))*100
    
    k1 = data[0][12][0] - data[0][9][0]
    k2 = data[frame][12][0] - data[frame][9][0]
    
    n1 = data[0][2][0]
    n2 = data[frame][2][0]
    n3 = data[0][5][0]
    n4 = data[frame][5][0]
    
    tx = (data[frame][8][0]-data[frame][11][0])/2
    ty = (data[frame][8][1]-data[frame][11][1])/2
    tz = (data[frame][8][2]-data[frame][11][2])/2
    l1 = (data[frame][14][1]-ty)/((data[frame][14][2]-tz)+0.0001)
    l2 = (data[frame][14][1]-data[frame][1][1])/((data[frame][14][2]-data[frame][1][2])+0.0001)
    
    if -10 < p < 10 : # all
        #print("연두색")
        pp = 'greenyellow'
    elif -100 < p < 100 :
        #print("초록")
        pp = 'green'
    else :
        #print("빨강")
        pp = 'red'
    
    
        
    if k1 > k2 : # 9 and 12
        #print("무릎경고") 
        w1 = 1
    else :
        #print("무릎통과")
        w1 = 0
        
    if 0.7<n1/(n2+0.0001)<1.3 and 0.7<n3/(n4+0.0001)<1.3 : # 2 and 5
        #print("어깨통과")
        w2 = 0
    else :
        #print("어깨경고")
        w2 = 1
        
    if l1 > l2 : # 0 , 1 and 14
        #print("척추경고")
        w3 = 1
    else :
        #print("척추통과")
        w3 = 0
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim3d(-200,200)
    ax.set_ylim3d(200,-200)
    ax.set_zlim3d(400,0)
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
        for i in [2]:
            xs.append(data[frame][i][0])
            ys.append(data[frame][i][1])
            zs.append(data[frame][i][2]) 
            ax.plot3D(xs,zs,ys,c='red',marker='o')
        xs=[]
        ys=[]
        zs=[]
        for i in [5]:
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