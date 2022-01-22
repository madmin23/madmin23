
import numpy as np

sizex=600

surf=np.array([['x','y','m']])

for i in range(200,sizex,1):
	b=1
	if i>105:
		b=1
	
	surf=np.append(surf,[[i,b,1]],axis=0)


# ~ surf=np.append(surf,[[200,1,1]],axis=0)

hexyplo=np.loadtxt("hexagony.txt", comments='#', delimiter=";", converters=None, skiprows=1)

surf=np.append(surf,hexyplo,axis=0)

print (surf.shape)

surf2=np.unique(surf, axis=0)

print (surf2.shape)

surf2=np.roll(surf2,1, axis=0)


np.savetxt("surface.txt", surf2,fmt='%s', delimiter=';', newline='\n', header='', footer='', comments='# ', encoding=None)
