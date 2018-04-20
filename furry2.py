import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

samples=1000
F1=7
F2=5
fig, ax = plt.subplots(figsize=(15, 15))

x = np.linspace(0, 2*F1, samples)
sig=np.sin(2*np.pi*.05*x)+np.cos(.1*x)
t= np.linspace(0,2*F1,samples)


X2,T2=np.meshgrid(x,t)
colors=X2
scat = plt.scatter(X2,T2,c=colors)
ax.set(xlim=(-3, 3), ylim=(-3, 3))

def animate(i):
    x_i=X2[i,:]
    y_i=T2[i,:]

    scat.set_offsets(np.c_[((np.sin(F1 * X2[i,:]) + np.cos(F2 * X2[i,:])) * np.cos(X2[i,:] * T2[i,:]),      (np.sin(F1 * X2[i,:]) + np.cos(F2 * X2[i,:])) * np.sin(X2[i,:] * T2[i,:]))])


anim = FuncAnimation(
fig, animate, interval=20, frames=len(x)-1)

plt.draw()
plt.show()
