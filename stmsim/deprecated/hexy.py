import numpy as np
import math

hexago=np.array([['x','y','m']])

centri = np.array([400.0,41.0,1.0])

crossi= 90.0

crossihalf = crossi/2
print crossihalf

crossiq= crossi/4

res=2.0
linires = int(math.ceil(crossihalf/res))

punktos= np.array([0.0,0.0,0.0])



for face in range(6):
	lini=0
	#face = 2
	#print face
	for lini in range(0,linires,1):
		print lini
		angli = 2*(math.pi)*((face*60.0+30.0)/360.0)
		print angli
		punktos =centri + ([crossihalf*np.cos((math.pi)/6.0)*np.cos(angli), crossihalf*np.cos((math.pi)/6.0)*np.sin(angli),0])+([-(crossiq-(lini*res*1.0))*np.sin(angli),(crossiq-(lini*res*1.0))*np.cos(angli),0])
		print punktos
		hexago=np.append(hexago,[punktos],axis=0)

np.savetxt("hexagony.txt", hexago,fmt='%s', delimiter=';', newline='\n', header='', footer='', comments='# ', encoding=None)
