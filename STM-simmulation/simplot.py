import matplotlib.pyplot as plt
import numpy as np
import math

surf=np.loadtxt("surface.txt", comments='#', delimiter=";", converters=None, skiprows=1)

linescan=np.loadtxt("line.txt", comments='#', delimiter=";", converters=None, skiprows=1)

tipi=np.loadtxt("tipi.txt", comments='#', delimiter=";", converters=None, skiprows=1)

hexyplo=np.loadtxt("hexagony.txt", comments='#', delimiter=";", converters=None, skiprows=1)
#plt.plot(hexyplo[:,0],hexyplo[:,1])
# ~ plt.plot(tipi[:,0],tipi[:,1])
plt.scatter(tipi[:,0],tipi[:,1], label='tip')
#plt.scatter(hexyplo[:,0],hexyplo[:,1])
#plt.show()

#print linescan[:,0:2]
sta=int(linescan[0,0])
sto=int(math.ceil(linescan[-1,0]))
print (sta,sto)
sta=0
#plt.plot(surf[:,0:2])
#plt.plot(surf[:,0],surf[:,1])
#plt.plot(surf[sta:sto,0],surf[sta:sto,1])
plt.scatter(surf[sta:sto,0],surf[sta:sto,1],1,color='green', label='surface')


#plt.plot(linescan[:,0:2])
plt.plot(linescan[:,0],linescan[:,1],'r', label='scanline')

# ~ x= np.arange(0,4,.1)
# ~ plt.plot(x, x/x)
# ~ plt.plot(x, 2*np.exp(-x))
# ~ plt.plot(x, np.exp(-2*x))

g=1
V=4

n= np.arange(105,110,.1)
k=np.arange(100,105,.1)
#plt.plot(n, V*np.exp(-g*(n-105)))
#plt.plot(k, V*np.exp(g*(k-105)))


plt.xlabel('length in au')
plt.ylabel("z heigth in au")
plt.legend()
plt.show()
