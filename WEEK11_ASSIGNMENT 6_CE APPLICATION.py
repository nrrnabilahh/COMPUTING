#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(0, 2)

linex = [0,0]
liney = [0,2]    
line, = ax.plot(0, 0)

# Spring data
k = 20
A = 1
v = 0.00125
w = 2*v * k**2

def plate(x3, t):
    global w, A
    return A * np.exp(-k*x3) * np.cos(w*t - k*x3)

counter = 0
def animation_frame(i):
    global counter
    
    x = np.zeros(21)
    y = np.zeros(21)
    for q in range(0, 21):
        x[q] = plate(q/100,counter)
        y[q] = q/10
    print('v(0,', round(i,1), ')/A = ',plate(0,counter)/A)
   
    line.set_xdata(x)    
    line.set_ydata(y)
    line.set_linewidth(3)
    plt.xlabel("v1 / A")
    plt.ylabel("kx3")
    plt.title("Flow Generated of Plate")
    plt.plot(linex, liney, color="black",ls="--",linewidth = 1.0)

    counter += 0.1
ani = FuncAnimation(fig,
                    animation_frame,
                    frames=np.arange(0.0, 6.3, 0.1),
                    interval=100)
plt.show()
ani.save('./plate_animation2.gif')


# In[ ]:




