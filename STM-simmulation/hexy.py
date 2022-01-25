import numpy as np
import math

hexago=np.array([['x','y','m']])

centri = np.array([400.0,41.0,1.0])##### 90 crossi
# ~ centri = np.array([400.0,24.0,1.0])###### 50 crossi

matconstx=.565325
matconsty=.565325


crossi= 91.0/matconstx

crossihalf = crossi/2
print (crossihalf)

crossiq= crossi/4

res=2.0
linires = int(math.ceil(crossihalf/res))

punktos= np.array([0.0,0.0,0.0])



for face in range(6):
	lini=0
	#face = 2
	#print face
	for lini in range(0,linires,1):
		print (lini)
		angli = 2*(math.pi)*((face*60.0+30.0)/360.0)
		print (angli)
		punktos =centri + ([crossihalf*np.cos((math.pi)/6.0)*np.cos(angli), crossihalf*np.cos((math.pi)/6.0)*np.sin(angli),0])+([-(crossiq-(lini*res*1.0))*np.sin(angli),(crossiq-(lini*res*1.0))*np.cos(angli),0])
		print (punktos)
		punktosff=(np.floor(punktos[0]),np.floor(punktos[1]),punktos[2])
		hexago=np.append(hexago,[punktosff],axis=0)
		punktoscc=(np.ceil(punktos[0]),np.ceil(punktos[1]),punktos[2])
		hexago=np.append(hexago,[punktoscc],axis=0)
		punktosfc=(np.floor(punktos[0]),np.ceil(punktos[1]),punktos[2])
		hexago=np.append(hexago,[punktosfc],axis=0)
		punktoscf=(np.ceil(punktos[0]),np.floor(punktos[1]),punktos[2])
		hexago=np.append(hexago,[punktoscf],axis=0)
		
print (hexago)

for j in range(1,hexago.shape[0]):
	hexago[j]=[float(hexago[j,0])*matconstx,float(hexago[j,1])*matconsty,float(hexago[j,2])]

print(hexago)


np.savetxt("hexagony.txt", hexago,fmt='%s', delimiter=';', newline='\n', header='', footer='', comments='# ', encoding=None)
